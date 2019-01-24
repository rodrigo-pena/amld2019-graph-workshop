# -*- coding: utf-8 -*-


import pandas as pd


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

