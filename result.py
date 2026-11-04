
def sorted_teams(teams):
    sort_teams = sorted(teams,key=lambda t: (t["points"],t["goals_for"]-t["goals_against"],t["goals_for"],t["name"]),reverse=True)
    return sort_teams

def sort_attacking_team(teams):
    sort_att = sorted(teams,key=lambda t: t["goals_for"],reverse=True)
    return sort_att
def team_without_wins(teams):
    without_wins = list(filter(lambda t: t["wins"] ==0,teams))
    return without_wins
def shaw_success_rate(teams):
    new_team = []
    try:
        for team in teams:
            new_team.append((team["points"]/(team["played"]*3))*100)
    except ZeroDivisionError:
        new_team.append("No_games")
    return sorted(new_team,reverse=True) 
   
def Show_tournament_summary(teams):
    try:    
        num_grups = len(teams)
        num_played = 0
        num_goals_for = 0
        num_goals_agens = 0
        even_games = 0
        for team in teams:
            num_played +=team["played"]
            num_goals_for += team["goals_for"]
            num_goals_agens += team["goals_against"]
            even_games += team["draws"] /2
        avg_goals_of_game = (num_goals_for + num_goals_agens)/num_played
    except ZeroDivisionError:
            return "no played"
    return {"grups":num_grups,"sum played":num_played,"sum goals":num_goals_for,"avg goals":avg_goals_of_game,"club with no games":even_games}
