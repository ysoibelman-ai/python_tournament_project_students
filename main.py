
"""
teams = []
team = {
    "id": 1, "name": "Maccabi", "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0
}

matches = [{"home_team_id": 1, "away_team_id": 2, "home_goals": 3, "away_goals": 1}]
"""

teams = []
matches = []


def show_menu():
    pass


def add_team(teams:list) -> list:    
    team_name,team_id = get_team_info()
    team = create_new_team(team_name,team_id)
    teams.append(team)
    return teams

def get_team_info() -> tuple:
    team_name = input("enter team name: ")
    team_id = input ("Enter team id: ")
    return team_name,team_id

def create_new_team(team_name,team_id) -> dict:
    team = {
    "id": team_id, "name": team_name, "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0
    }
    return team
"""
matches = [{"home_team_id": 1, "away_team_id": 2, "home_goals": 3, "away_goals": 1}]
"""
def add_match(matches):
    home_team_id,away_team_id,home_goals,away_goals = get_match_info()
    match = create_new_match(home_team_id,away_team_id,home_goals,away_goals)
    matches.append(match)
    return matches

def get_match_info():
    home_team_id = input("Enter home team id: ")
    away_team_id = input("Enter away team id: ")
    home_goals = input("Enter home goals: ")
    away_goals = input("Enter away goals: ")
    return home_team_id,away_team_id,home_goals,away_goals

def create_new_match(home_team_id,away_team_id,home_goals,away_goals):
    match = {"home_team_id": home_team_id, "away_team_id": away_team_id, "home_goals": home_goals, "away_goals": away_goals}
    return match


def update_team():
    pass
def show_teams():
    pass
print (add_match(matches))