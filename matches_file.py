from validations import check_valid_num,check_valid_name,check_not_equal,check_if_exists,check_played_already
from input_file import get_input
from update_team import update_teams

def add_match(teams,matches):
    while True:

        home_team_id = get_input("Enter home team id")
        away_team_id = get_input("Enter away team id")

        if check_if_exists(teams,"id",home_team_id):
            print("home team id doesn't exists, please re-enter id's")
            continue
            
        if check_if_exists(teams,"id",away_team_id):
            print("away team id doesn't exists, please re-enter id's")
            continue

        if not check_not_equal(home_team_id,away_team_id):
            print ("same id's entered. please re-enter id's")
            continue
        
        if not check_played_already(matches,home_team_id,away_team_id):
            print ("teams already played")
            continue
        break

    while True:
        home_goals = get_input("Enter home goals")
        away_goals = get_input("Enter away goals")

        if not (check_valid_num(home_goals) and check_valid_num(away_goals)):
            print ("invalid goals")
            continue

        home_goals = int(home_goals)
        away_goals = int(away_goals)
        
        match = create_new_match(home_team_id,away_team_id,home_goals,away_goals)
        matches.append(match)
        update_teams(teams,match)
        break


def create_new_match(home_team_id,away_team_id,home_goals,away_goals):
    match = {"home_team_id": home_team_id, "away_team_id": away_team_id, "home_goals": home_goals, "away_goals": away_goals}
    return match