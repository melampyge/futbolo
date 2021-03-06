# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:46:31 2016

@author: melampyge
"""

import numpy as np
import pandas as pd

#############################################################################

class Player:
    """ data structure for keeping player attributes"""
    
    def __init__(self, defc, ps, dr, sh, st):
        
        self.defence = defc
        self.passing = ps
        self.dribbling = dr
        self.shooting = sh
        self.stamina = st
        
        return
        
#############################################################################

def gen_matchday_squad(players, database):
    """ create the matchday squad as a pandas dataframe structure"""
    
    attributes = ['defence', 'passing', 'dribbling', 'shooting', 'stamina']

    matchday_squad = pd.DataFrame(columns=players, index=attributes)
    for player in players:
        matchday_squad[player]['defence'] = database[player].defence
        matchday_squad[player]['passing'] = database[player].passing
        matchday_squad[player]['dribbling'] = database[player].dribbling
        matchday_squad[player]['shooting'] = database[player].shooting
        matchday_squad[player]['stamina'] = database[player].stamina

    return matchday_squad

#############################################################################

def get_index(att):
    """ get the index of the attribute"""

    if att == 'defence':
        return 0
    elif att == 'passing':
        return 1
    elif att == 'dribbling':
        return 2
    elif att == 'shooting':
        return 3
    elif att == 'stamina':
        return 4

#############################################################################
        
def reinforce_min_attribute(team, team_attributes, squad, choice_number, which):
    """ reinforce the team on its minimum attribute with the player highest in that attribute"""
    
    ## choose the minimum attribute of the team
    
    min_att = team_attributes.idxmin()
    min_att_index = get_index(min_att)
    
    ## choose the player with the maximum attribute in the weakest link of the team
    
    new_player = squad.iloc[min_att_index,:].idxmax()

    ## add the player and delete the player from the remaining list

    team.append( new_player )
    team_attributes = (team_attributes + squad[team[choice_number]])/2.0
    del squad[team[choice_number]]
    
    ## print the player choice information
    
    if which == 1:
        print team[0], " realizes that the team 1 sucks in ", min_att, " so to compensate, he gets ", team[choice_number], " as his ", choice_number, " choice." 
    elif which == 2:
        print team[0], " realizes that the team 2 sucks in ", min_att, " so to compensate, he gets ", team[choice_number], " as his ", choice_number, " choice."  
    elif which == 3:
        print team[0], " realizes that the team 3 sucks in ", min_att, " so to compensate, he gets ", team[choice_number], " as his ", choice_number, " choice."  
        
    return squad, team_attributes

#############################################################################

def divide_into_2_teams(squad):
    """ Divide the current matchday squad into 2 teams"""
    
    ## if number of teams is 2 
        
    ## 2 people with maximum overall attributes are captains
    
    max_overall = squad.mean()
    top_6_players_ind = max_overall.argsort()[-6:][::-1]
    top_6_players = max_overall[top_6_players_ind]
    captains = [squad.iloc[:,top_6_players_ind[0]].name, squad.iloc[:,top_6_players_ind[1]].name]        
    team_1 = [captains[0]]
    team_2 = [captains[1]]
    
    print "***************************\n"    
    print "*** Top 6 players ***\n\n", top_6_players, "\n\n"
    print "***************************\n"    
    print "*** Captains ***\n\n", captains, "\n\n"
    print "***************************\n"    
    
    ## second captain chooses the player with maximum overall point
    ## then first captain chooses a player with maximum overall point
    
    print " TEAM CHOICE STARTS! "
    print "***************************\n\n"    
    
    team_2.append( squad.iloc[:,top_6_players_ind[2]].name ) 
    team_2_attributes = (squad[team_2[0]] + squad[team_2[1]])/2.0
    print "The second captain ", team_2[0], " chose ", team_2[1], " as his 1st choice."
           
    team_1.append( squad.iloc[:,top_6_players_ind[3]].name )
    team_1_attributes = (squad[team_1[0]] + squad[team_1[1]])/2.0
    print "The first captain ", team_1[0], " chose ", team_1[1], " as his 1st choice."
    
    team_2.append( squad.iloc[:,top_6_players_ind[4]].name ) 
    team_2_attributes = (squad[team_2[0]] + squad[team_2[2]])/2.0
    print "The second captain ", team_2[0], " chose ", team_2[2], " as his 2nd choice."

    team_1.append( squad.iloc[:,top_6_players_ind[5]].name )
    team_1_attributes = (squad[team_1[0]] + squad[team_1[2]])/2.0
    print "The first captain ", team_1[0], " chose ", team_1[2], " as his 2nd choice."
    
    ## delete the players already chosen to compare the rest of the players 

    del squad[team_1[0]]
    del squad[team_1[1]]
    del squad[team_1[2]]
    del squad[team_2[0]]
    del squad[team_2[1]]
    del squad[team_2[2]]
 
    ## second captain makes his third choice
 
    squad, team_2_attributes = reinforce_min_attribute(team_2, team_2_attributes, squad, 3, 2)
    
    ## first captain makes his third choice

    squad, team_1_attributes = reinforce_min_attribute(team_1, team_1_attributes, squad, 3, 1)

    ## second captain makes his fourth choice

    squad, team_2_attributes = reinforce_min_attribute(team_2, team_2_attributes, squad, 4, 2)

    ## first captain makes his fourth choice

    squad, team_1_attributes = reinforce_min_attribute(team_1, team_1_attributes, squad, 4, 1)
        
    return team_1, team_2, team_1_attributes, team_2_attributes
 
#############################################################################
 
def divide_into_3_teams(squad):
    """ Divide the current matchday squad into 3 teams"""
    
    ## if number of teams is 3
        
    ## 3 people with maximum overall attributes are captains
    
    max_overall = squad.mean()
    top_7_players_ind = max_overall.argsort()[-7:][::-1]
    top_7_players = max_overall[top_7_players_ind]
    captains = [squad.iloc[:,top_7_players_ind[0]].name, \
        squad.iloc[:,top_7_players_ind[1]].name, squad.iloc[:,top_7_players_ind[2]].name]        
    team_1 = [captains[0]]
    team_2 = [captains[1]]
    team_3 = [captains[2]]
    
    print "***************************\n"    
    print "*** Top 7 players ***\n\n", top_7_players, "\n\n"
    print "***************************\n"    
    print "*** Captains ***\n\n", captains, "\n\n"
    print "***************************\n"    
    
    ## third captain chooses the player with maximum overall point
    ## then second captain chooses the player with maximum overall point
    ## then first captain chooses 2 players with maximum overall points
    
    print " TEAM CHOICE STARTS! "
    print "***************************\n\n"    
    
    team_3.append( squad.iloc[:,top_7_players_ind[3]].name ) 
    team_3_attributes = (squad[team_3[0]] + squad[team_3[1]])/2
    print "The third captain ", team_3[0], " chose ", team_3[1], " as his 1st choice."
           
    team_2.append( squad.iloc[:,top_7_players_ind[4]].name )
    team_2_attributes = (squad[team_2[0]] + squad[team_2[1]])/2
    print "The second captain ", team_2[0], " chose ", team_2[1], " as his 1st choice."
    
    team_1.append( squad.iloc[:,top_7_players_ind[5]].name )
    team_1_attributes = (squad[team_1[0]] + squad[team_1[1]])/2
    print "The first captain ", team_1[0], " chose ", team_1[1], " as his 1st choice."

    team_1.append( squad.iloc[:,top_7_players_ind[6]].name )
    team_1_attributes = (squad[team_1[0]] + squad[team_1[2]])/2
    print "The first captain ", team_1[0], " chose ", team_1[2], " as his 2nd choice."
    
    ## delete the players already chosen to compare the rest of the players 

    del squad[team_1[0]]
    del squad[team_1[1]]
    del squad[team_1[2]]
    
    del squad[team_2[0]]
    del squad[team_2[1]]
    
    del squad[team_3[0]]
    del squad[team_3[1]]

    ## third captain adds a player based on the minimum attribute of the team, and it goes on until we run out of players
 
    squad, team_3_attributes = reinforce_min_attribute(team_3, team_3_attributes, squad, 2, 3)
    squad, team_2_attributes = reinforce_min_attribute(team_2, team_2_attributes, squad, 2, 2)
    ## note that team 1 already did the 2nd choice
    
    ## third choices
 
    squad, team_1_attributes = reinforce_min_attribute(team_1, team_1_attributes, squad, 3, 1)     ## note that team 1 is making the 3rd choice   
    squad, team_3_attributes = reinforce_min_attribute(team_3, team_3_attributes, squad, 3, 3)
    squad, team_2_attributes = reinforce_min_attribute(team_2, team_2_attributes, squad, 3, 2)
    
    ## fourth choices

    squad, team_1_attributes = reinforce_min_attribute(team_1, team_1_attributes, squad, 4, 1)      
    squad, team_3_attributes = reinforce_min_attribute(team_3, team_3_attributes, squad, 4, 3)
    squad, team_2_attributes = reinforce_min_attribute(team_2, team_2_attributes, squad, 4, 2)
        
    return team_1, team_2, team_3, team_1_attributes, team_2_attributes, team_3_attributes
    
#############################################################################

def main():
    
    ## create a database of players with attributes
    ## player database is a dictionary with name of the player as 'key'
    ## and the object containing attributes as 'value'
    ## attributes are listed in the following order :
    ## DEFENCE - PASSING - DRIBBLING - SHOOTING - STAMINA
    
    player_database = {}
    player_database['Luca'] = Player(5, 3, 5, 2, 5)
    player_database['Ozer'] = Player(1, 5, 2, 2, 2)
    player_database['Sebastian'] = Player(2, 4, 3, 5, 1)
    player_database['Thomas'] = Player(3, 2, 5, 2, 5)
    player_database['Varun'] = Player(1, 3, 2, 5, 1)
    player_database['Arvind'] = Player(4, 5, 3, 3, 5)
    player_database['Fabrizio'] = Player(5, 5, 5, 5, 4)
    player_database['Maggi'] = Player(5, 5, 5, 4, 5)
    player_database['Shibananda'] = Player(5, 2, 2, 1, 2)
    player_database['Nicolo'] = Player(5, 3, 3, 3, 4)
    player_database['Claire'] = Player(4, 1, 1, 1, 1)
    player_database['Manuel'] = Player(5, 5, 4, 4, 3)
    player_database['Elisa'] = Player(4, 1, 1, 1, 1)
    player_database['Dip'] = Player(5, 4, 4, 3, 5)
    player_database['Andy'] = Player(4, 3, 3, 3, 2)
    player_database['Emiliano'] = Player(5, 4, 4, 4, 4)
    player_database['Ali'] = Player(5, 4, 4, 5, 1)
            
    ## OPTION WITH 10 PLAYERS:
    
    ## create the overall matchday squad as a pandas dataframe structures
    ## columns are players, attributes are index
    
    matchday_players = ['Luca', 'Ozer', 'Sebastian', \
        'Shibananda', 'Ali', 'Emiliano', 'Claire', 'Varun', 'Nicolo', 'Arvind']
    matchday_squad = gen_matchday_squad(matchday_players, player_database)

    print "\n***************************\n"        
    print '*** MATCHDAY SQUAD ***\n\n', matchday_squad, '\n\n'
    
    ## divide the squad into teams
    
    team_1, team_2, team_1_attributes, team_2_attributes = divide_into_2_teams(matchday_squad)
    
    print "\n***************************\n"        
    print '*** TEAM 1 ***\n\n', team_1, '\n', team_1_attributes, '\n\n'
    print '*** TEAM 2 ***\n\n', team_2, '\n', team_2_attributes, '\n\n'
    
    ## OPTION WITH 15 PLAYERS:
    ## do the same with 15 players
    
#    matchday_players = ['Luca', 'Ozer', 'Sebastian', \
#        'Thomas', 'Varun', 'Arvind', 'Fabrizio', 'Maggi', 'Shibananda', 'Nicolo', \
#        'Claire', 'Manuel', 'Elisa', 'Dip', 'Andy']
#    matchday_squad = gen_matchday_squad(matchday_players, player_database)
#    
#    print "\n***************************\n"        
#    print '*** MATCHDAY SQUAD ***\n\n', matchday_squad, '\n\n'
#        
#    team_1, team_2, team_3, team_1_attributes, team_2_attributes, team_3_attributes = divide_into_3_teams(matchday_squad)    
#
#    print "\n***************************\n"        
#    print '*** TEAM 1 ***\n\n', team_1, '\n', team_1_attributes, '\n\n'
#    print '*** TEAM 2 ***\n\n', team_2, '\n', team_2_attributes, '\n\n'
#    print '*** TEAM 3 ***\n\n', team_3, '\n', team_3_attributes, '\n\n'
    
    return
    
  
#############################################################################
    
if __name__ == "__main__":
    main()

#############################################################################