
def get_info_match(home_team_id,away_team_id,home_goals,away_goals):
    new_match = {"home_team_id":home_team_id ,"away_team_id": away_team_id,
                "home_goals": home_goals,"away_goals": away_goals}
    return new_match
def add_play(new_match,matchs:list):
    matchs.append((new_match["home_team_id"],new_match["away_team_id"]))

def add_info_match(new_match,teams):
    for team in teams:
        if new_match["home_team_id"] == team["id"]:
            team["goals_for"] +=new_match["home_goals"]
            team["goals_against"] +=new_match["away_goals"]
            team["played"] +=1
            if new_match["home_goals"] > new_match["away_goals"]:
                team["wins"] +=1
                team["points"] +=3
            elif new_match["home_goals"] == new_match["away_goals"]:
                team["draws"] +=1
                team["points"] +=1
            elif new_match["home_goals"] < new_match["away_goals"]:
                team["losses"] +=1
        if new_match["away_team_id"] == team["id"]:
            team["goals_for"] +=new_match["away_goals"]
            team["goals_against"] +=new_match["home_goals"]
            team["played"] +=1
            if new_match["away_goals"] > new_match["home_goals"]:
                team["wins"] +=1
                team["points"] +=3
            elif new_match["home_goals"] == new_match["away_goals"]:
                team["draws"] +=1
                team["points"] +=1
            elif new_match["away_goals"] < new_match["home_goals"]:
                team["losses"] +=1
            
