
def check_not_empty(item):
    if item.strip():
        return True
    else:
        return False

def check_if_team_exict(item,teams):
    for team in teams:
        if team[item] == item:
            return False    
    return True

def validate_id_Positive(id):
    if id < 0:
        return False
    else:
        return True