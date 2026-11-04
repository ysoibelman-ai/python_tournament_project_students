def sort_teams(teams):
    sorted_teams = sorted(teams,key = lambda t: (t["points"],int(t["goals_for"]) - int(t["goals_against"]),int(t["goals_for"]),t["name"]),reverse=True)
    return sorted_teams

def get_top_team(teams):
    sorted_teams = sort_teams(teams)
    top_team = sorted_teams[0]
    return top_team

def get_best_attacking_team(teams):
    top_attacking_team = {}
    top_attack = -1
    for team in teams:
        if team["goals_for"] > top_attack:
            top_attack = team["goals_for"]
            top_attacking_team = team
    return top_attacking_team

def get_team_success_rate(teams,matches):
    if matches == []:
        return "No Matches Played"
    teams_success_rate = []
    for team in teams:
        team_success = {team["name"]:f"Success rate is: {(int(team["points"] / (team["played"]*3 * 100)))}"}
        teams_success_rate.append(team_success)
    return teams_success_rate

def get_teams_without_wins(teams):
    teams_without_wins = []
    for team in teams:
        if team["wins"] == 0:
            teams_without_wins.append(team)
    return teams_without_wins

def get_tournament_summary(teams,matches):
    if matches == []:
        return False
    total_goals = 0
    number_of_teams = len(teams)
    number_of_games = len(matches)
   
    total_goals = sum(team["goals_for"] for team in teams)
    
    goal_avg_per_game = total_goals / len(matches)
    total_draw_games = sum(filter(lambda t: t["draws"] > 0, teams))
    leading_team = (sort_teams(teams)[1])
    return [number_of_teams,number_of_games,total_goals,goal_avg_per_game,total_draw_games,leading_team]