
def add_team(team,teams):
    teams.append(team)
        
def get_info_team(id,name): 
    new_team = {
        "id": id, "name": name, "played": 0,
        "wins": 0, "draws": 0, "losses": 0,
        "goals_for": 0, "goals_against": 0, "points": 0}
    return new_team
