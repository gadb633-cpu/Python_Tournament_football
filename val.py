
def val_not_empty(item):
    if item.strip():
        return True
    else:
        return False

def val_if_team_exict(item,teams):
    for team in teams:
        if team["id"] == item:
            return False    
    return True

def val_id_Positive(id):
    if id < 0:
        return False
    else:
        return True

def team_not_same(home_team_id,away_team_id):
    if home_team_id == away_team_id:
        return False
    return True

def val_if_team_alredy_played(new_match,matches):
    for match in matches:
        if new_match["home_team_id"] == match["home_team_id"] and new_match["away_team_id"] == match["away_team_id"]:
            return False
        return True
