from validations import check_if_exists,check_not_equal,check_valid_name,check_valid_num
from input_file import get_input

def add_team(teams:list) -> list:    
    while True:
        team_name = get_input("Enter team name")
    
        if not check_valid_name(team_name):
            print ("invalid name")
            continue

        if not check_if_exists(teams,"name",team_name):
                print ("team name already exists")
                continue
        break

    while True:
        team_id = get_input("Enter team id")
         
        if not check_valid_num(team_id):
            print ("Invalid id")
            continue
        
        if not check_if_exists(teams,"id",team_id):
            print ("Team id already exists")
            continue
        break
   
    team = create_new_team(team_name,team_id)
    teams.append(team)

def create_new_team(team_name,team_id) -> dict:
    team = {
    "id": team_id, "name": team_name, "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0
    }
    return team