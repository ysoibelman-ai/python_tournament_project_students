def check_valid_num(num) -> bool:
    try:
        num = int(num)
    except:
        print ("invalid input, please re enter")
        return False
    if  num >= 0:
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

def check_if_exists(storage:list,info_type,info) -> bool:
    """
    if exists returns False
    """
    for part in storage:
        if part[info_type] == info:
            return False
    return True

def check_played_already(matches,home_team_id,away_team_id):
    for match in matches:
        if (match["home_team_id"] == home_team_id and match[away_team_id] == away_team_id) or (match["home_team_id"] == away_team_id and match[away_team_id] == home_team_id):
            return False
    return True