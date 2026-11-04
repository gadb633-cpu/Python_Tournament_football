
def sorted_teams(teams):
    sort_teams = sorted(teams,key=lambda t: (t["points"],t["goals_for"]-t["goals_against"],t["goals_for"],t["name"]),reverse=True)
    return sort_teams

def sort_attacking_team(teams):
    sort_att = sorted(teams,key=lambda t: t["goals_for"],reverse=True)
    return sort_att
def team_without_wins(teams):
    without_wins = list(filter(lambda t: t["wins"] ==0,teams))
    return without_wins