from shaw_menu import *
from inputs import *
from teams import *


def main():
    matchs = []
    teams = [{
    "id": 1, "name": "Maccabi", "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0}]
    while True:
        shaw_menu()
        choice = get_id("Choose an option(0-10) ")
        if isinstance(choice, bool):
            continue
        if choice == 1:
            team_id = get_id("enter team id for adding: ")
            if isinstance(choice, bool):
                continue
            team_name = get_name("enter team name for adding: ")
            new_team = get_info_team(team_id,team_name)
            add_team(new_team,teams)
        elif choice == 2:
            if teams ==[]:
                print("teams is empty!!")
            else:    
                print(teams)
        elif choice == 3:
            pass
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
