
def val_not_empty(item):
    if item.strip():
        return True
    else:
        return False

def val_if_team_exict(item,teams):
    for team in teams:
        if team[item] == item:
            return False    
    return True

def val_id_Positive(id):
    if id < 0:
        return False
    else:
        return True