# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
import networkx as nx
import matplotlib as mpl
import matplotlib.pyplot as plt

###

# For the CH council data

def assign_party_to_names(party_membership_list_path, namelist):
    """ Adds a column containing the party membership of the councillors specified in namelist
    party_membership_list_path:     Path to a file that contains a spreadsheet with names and parties
                                    Example: '../data/Ratsmitglieder_1848_FR.csv'
    namelist:                       pd.DataFrame that contains a column of names of councillors
                                    whose party association should be found
    returns:
        namelist_with_parties:      pd.DataFrame identical to namelist but with an added column
                                    with the party associations"""

    if not isinstance(namelist, pd.DataFrame):
        raise TypeError("Namelist must be a pd.DataFrame")

    if not 'CouncillorName' in namelist.columns:
        raise KeyError("Namelist must contain a column labeled 'CouncillorName'")

    #List of all members with their party
    all_members_cn = pd.read_csv(party_membership_list_path, sep=';', lineterminator='\n')
    all_members_cn = all_members_cn[['FirstName', 'LastName', 'PartyAbbreviation']]
    #Concatenate first and last name

    all_members_cn['FullName'] = all_members_cn['LastName'].str.cat(all_members_cn['FirstName'], sep=' ')
    all_members_cn = all_members_cn.drop(columns=['LastName', 'FirstName'])
    #Remove duplicate
    all_members_cn = all_members_cn[['FullName', 'PartyAbbreviation']].drop_duplicates(subset=['FullName'])
    namelist_with_parties = namelist.join(all_members_cn.set_index('FullName'), on='CouncillorName')

    # Reassign parties if the party has merged with another one
    replace_these_parties = {'PRD':'PLR', 'GB':'PES', 'PLS':'PLR'}
    namelist_with_parties['PartyAbbreviation'] = namelist_with_parties['PartyAbbreviation'].replace(replace_these_parties)

    n_no_party = len(namelist_with_parties) - namelist_with_parties['PartyAbbreviation'].count()

    if n_no_party != 0:
        print("{0} councillors couldn't be associated to a party".format(n_no_party))
    return namelist_with_parties


def preprocess_swiss_council():

    # Load information from the 50th legislature
    adjacency = np.load('../data/council_adjacency.npy')
    node_indices = pd.read_csv('../data/council_node_info.csv', sep=',')
    names_with_parties = assign_party_to_names('../data/council_parties.csv', node_indices)

    # Map parties to colors
    parties_to_be_plotted = ['UDC',
                             'PSS',
                             'PDC',
                             'pvl',
                             'PLR',
                             'PES',
                             'PBD']
    party_colors = ['royalblue',
                    'r',
                    'orange',
                    'g',
                    'cyan',
                    'forestgreen',
                    'yellow']
    party_color_map = dict((key, value) for (key, value) in zip(parties_to_be_plotted, party_colors))

    np.save('../data/council_party_color_map.npy', party_color_map)

    # Assign a color to each council member, according to their parties
    member_colors = []
    for abbr in names_with_parties['PartyAbbreviation'].values:
        try:
            colorname = party_color_map[abbr]
        except KeyError:
            colorname = 'gray'
        member_colors.append(colorname)

    # Assemble final council dataframe
    council_df = names_with_parties.assign(Color=pd.Series(member_colors).values)

    return council_df, adjacency


def plot_council_with_party_colors(council_df, x_coords, y_coords,
                                   custom_colors=None):
    # Scatter plot of the council members, colored by party affiliation
    fig = plt.figure(figsize=(9,5))
    ax = fig.add_subplot(111)

    if custom_colors is None:
        ax.scatter(x_coords, y_coords, c=council_df['Color'], s=50, alpha=0.8)
        ax.set_title('2D Embedding of the Swiss National Council')
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        fig.tight_layout()

        party_color_map = np.load('../data/council_party_color_map.npy').item()
        fig = plt.figure(figsize=(9.6, 3))
        ax = fig.add_axes([0.05, 0.15, 0.9, 0.15])

        # Plot color dictionary for the party abbreviations
        cmap = mpl.colors.ListedColormap(party_color_map.values())
        cbar = mpl.colorbar.ColorbarBase(ax, cmap=cmap,
                                        ticks=range(len(party_color_map.values())),
                                        spacing='uniform',
                                        orientation='horizontal')

        cbar.ax.get_xaxis().set_ticks([])
        for j, lab in enumerate(party_color_map.keys()):
            cbar.ax.text((2 * j + 1) / 14.0, -.5, lab, ha='center', va='center', color='black')
        cbar.ax.get_xaxis().labelpad = 15
        cbar.ax.set_xlabel('Party Abbreviations')
        cbar.ax.xaxis.set_label_coords(0.5, -1)

    else:
        ax.scatter(x_coords, y_coords, c=custom_colors, s=50, alpha=0.8)
        ax.set_title('2D Embedding of the Swiss National Council')
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        fig.tight_layout()

###
        
# For the flight routes data

def preprocess_flight_routes():
    routes = pd.read_csv('../data/routes_clean.csv', low_memory=False)
    airports = pd.read_csv('../data/airports_clean.csv', index_col=0)

    G = nx.from_pandas_edgelist(routes, 'Source airport', 'Destination airport', ['Distance'])

    pos = {airport: (v['Longitude'], v['Latitude'])
        for airport, v in
        airports.to_dict('index').items()}

    return routes, airports, pos, G

def display_map(graph, pos, node_color=None):

    import cartopy.crs as ccrs

    deg = nx.degree(graph)
    node_sizes = [5 * deg[iata] for iata in graph.nodes]

    node_labels = {iata: iata if deg[iata] >= 200 else ''
                   for iata in graph.nodes}

    # Map projection
    fig, ax = plt.subplots(1, 1, figsize=(36, 24),
                           subplot_kw=dict(projection=ccrs.PlateCarree()))
    ax.coastlines()

    nx.draw_networkx(graph, ax=ax,
                     font_size=20,
                     alpha=.5,
                     width=.075,
                     node_size=node_sizes,
                     labels=node_labels,
                     pos=pos,
                     node_color=node_color)
    
###
