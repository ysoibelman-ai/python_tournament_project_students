def check_valid_num(num) -> bool:
    try:
        num = int(num)
    except:
        print ("invalid num, please re enter information")
        return False
    if  num > 0:
        return True
    else:
        return False

def check_valid_name(team_name) -> bool:
    if team_name.strip():
        return True
    return False

def check_not_equal(info1,info2) -> bool:
    if info1 == info2:
        return False
    return True


"""
teams = []
team = {
    "id": 1, "name": "Maccabi", "played": 0,
    "wins": 0, "draws": 0, "losses": 0,
    "goals_for": 0, "goals_against": 0, "points": 0
}

matches = [{"home_team_id": 1, "away_team_id": 2, "home_goals": 3, "away_goals": 1}]
"""


def check_if_exists(storage:list,info_type,info) -> bool:
    """
    if exists returns False
    """
    for part in storage:
        if part[info_type] == info:
            return False
    return True