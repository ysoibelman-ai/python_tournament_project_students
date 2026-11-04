# from validations import check_valid_name,check_valid_num,check_if_exists,check_not_equal
from teams_file import add_team
from matches_file import add_match
from outputs import show_teams

"""
teams = []
team = {
    "id": 1, "name": "Maccabi", "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0
}

matches = [{"home_team_id": 1, "away_team_id": 2, "home_goals": 3, "away_goals": 1}]
"""

def main():
    teams = []
    matches = []
    add_team(teams)
    add_team(teams)
    add_match(teams,matches)
    show_teams (teams)
    


if __name__ == "__main__":
    main()

def show_menu():
    pass
def update_team():
    pass