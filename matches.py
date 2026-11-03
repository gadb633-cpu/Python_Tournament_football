
def get_info_match(home_team_id,away_team_id,home_goals,away_goals):
    new_match = {"home_team_id":home_team_id , "away_team_id": away_team_id,
            "home_goals": home_goals, "away_goals": away_goals}
    return new_match

def add_info_match(new_match,teams):
    for team in teams:
        if new_match["home_team_id"] == team["id"]:
            pass
