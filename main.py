from shaw_menu import *
from inputs import *
from teams import *
from matches import *
from val import *
def main():
    matches = []
    teams = [{
    "id": 1, "name": "Maccabi", "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0}]
    while True:
        shaw_menu()
        choice = get_num("Choose an option(0-10) ")
        if isinstance(choice, bool):
            continue
        if choice == 1:
            while True:    
                team_id = get_num("enter team id for adding ")
                if isinstance(team_id, bool):
                    continue
                team_name = get_name("enter team name for adding ")
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
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            pass
        elif choice== 8:
            pass
        elif choice == 9:
            pass
        elif choice == 10:
            pass
        elif choice ==0:
            break

main()    
