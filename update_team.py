"""
matches = [{"home_team_id": 1, "away_team_id": 2, "home_goals": 3, "away_goals": 1}]

team = {
    "id": 1, "name": "Maccabi", "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0
}

"""

def update_teams(teams,match):
    home_team_id = match["home_team_id"]
    away_team_id = match["away_team_id"]
    winner = check_winner(match)
    
    for team in teams:
        if team["id"] == home_team_id:
            home_team = team
        elif team["id"] == away_team_id:
            away_team = team
    update_played(home_team,away_team)
    update_wins(winner,home_team,away_team)
    update_points(winner,home_team,away_team)
    update_goals(match,home_team,away_team)

#update played
def update_played(home_team,away_team):
    home_team["played"] += 1
    away_team["played"] += 1
    
# update winner
def update_wins(winner,home_team,away_team):
    if winner == 0:
        home_team["wins"] += 1
    elif winner == 1:
        away_team["wins"] += 1
    elif winner == 2:
        home_team["draws"] += 1
        away_team["draws"] += 1
#update points
def update_points (winner,home_team,away_team):
    if winner == 0:
        home_team["points"] +=3
    elif winner == 1:
        away_team["points"] +=3
    elif winner == 2:
        home_team["points"] +=1
        away_team["points"] +=1

# update goals
def update_goals(match,home_team,away_team):
    home_team["goals_for"] += match["home_goals"]
    home_team["goals_against"] += match["away_goals"]
    away_team["goals_for"] += match["away_goals"]
    away_team["goals_against"] += match["home_goals"]

# checks who won
def check_winner(match) -> int:
    """
    returns 0 if home team won, 1 if away team won and 2 if it was a draw,
    """
    if match["home_goals"] > match ["away_goals"]:
        return 0
    elif  match ["away_goals"] > match["home_goals"]:
        return 1
    return 2