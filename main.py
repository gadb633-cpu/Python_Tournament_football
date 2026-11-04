from shaw_menu import *
from inputs import *
from teams import *
from matches import *
from val import *
from result import *
import logging

def main():
    matches = []
    teams = []
    while True:
        shaw_menu()
        choice = get_num("Choose an option(0-10) ")
        if val_between_range(choice):
            continue
        if isinstance(choice, bool):
            continue
        if choice == 1:
            while True:    
                team_id = get_num("enter team id for adding ")
                if val_Positive_num(team_id) == False:
                    continue
                if isinstance(team_id, bool):
                    continue
                if val_if_team_exict(team_id,teams) == False:
                    continue
                team_name = get_name("enter team name for adding ")
                if val_not_empty(team_name):
                    continue
                if val_if_team_exict(team_name,teams) == False:
                    continue
                new_team = get_info_team(team_id,team_name)
                add_team(new_team,teams)
                break
        elif choice == 2:
            if teams ==[]:
                print("teams is empty!!")
            else:    
                print(teams)
        elif choice == 3:
            while True:
                if len(teams) ==1 or len(teams) ==0:
                    print("There aren't enough groups!!")
                    break
                home_team_id = get_num("enter home_team_id ")
                away_team_id = get_num("enter away_team_id ")
                home_goals = get_num("enter home_goals ")
                away_goals = get_num("enter away_goals ")
                new_match = get_info_match(home_team_id,away_team_id,home_goals,away_goals)
                if val_if_team_exict(home_team_id,teams) and val_if_team_exict(away_team_id,teams):
                    print("not exict")
                    continue
                if team_not_same(home_team_id,away_team_id) == False:
                    print("its the same")
                    continue
                if val_if_team_alredy_played(new_match,matches) == False:
                    print("them alrady played")
                    continue
                add_play(new_match,matches)
                add_info_match(new_match,teams)
                break
        elif choice == 4:
            if teams ==[]:
                print("teams is empty!!")
            else:    
                print(sorted_teams(teams))
        elif choice == 5:
            if teams ==[]:
                print("teams is empty!!")
            else:    
                print(sorted_teams(teams)[0])
        elif choice == 6:
            if teams ==[]:
                print("teams is empty!!")
            else:    
                print(sort_attacking_team(teams)[0])
        elif choice == 7:
            if teams ==[]:
                print("teams is empty!!")
            else:    
                list_teams = shaw_success_rate(teams)
                for team in list_teams:
                    print(f"{team}%")
        elif choice== 8:
            if teams ==[]:
                print("teams is empty!!")
            else:    
                print(team_without_wins(teams))
        elif choice == 9:
            if teams ==[]:
                print("teams is empty!!")
            else:    
                try:
                    list_summary = Show_tournament_summary(teams)
                    print(f"grups:{list_summary["grups"]} \nsum played:{list_summary["sum played"]} \nsum goals:{list_summary["sum goals"]} \navg goals:{list_summary["avg goals"]:.2f} \nclub with no games:{list_summary["club with no games"]}")
                except TypeError:
                    print(list_summary)    
        elif choice == 10:
            pass
        elif choice ==0:
            break

main()
