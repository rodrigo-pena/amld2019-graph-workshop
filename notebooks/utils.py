# -*- coding: utf-8 -*-


import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


# For the CH council data

def assign_party_to_names(party_membership_list_path, namelist):
    """ Adds a column containing the party membership of the councillors specified in namelist
    party_membership_list_path:     Path to a file that contains a list with names and parties
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


# For the airport data

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