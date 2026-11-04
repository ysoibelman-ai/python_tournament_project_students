import json
from teams_file import add_team
from matches_file import add_match

def main_menu(teams,matches):
    # while True:
        menu_choice = input("""
========== TOURNAMENT MANAGER ==========
1. Add team
2. Show all teams
3. Add match result
4. Show standings
5. Show leading team
6. Show best attacking team
7. Show team success rate
8. Show teams without wins
9. Show tournament summary
10. Check championship potential
0. Exit
Choose an option:
""")
        match menu_choice:
            case "1":
                add_team(teams)
            case "2":
                show_teams(teams)
            case "3":
                add_match(matches)
            case "4":
                        pass
            case "5":
                        pass
            case "6":
                        pass
            case "7":
                        pass
            case "8":
                        pass
            case "9":
                        pass
            case "10":
                        pass
            case "0":
                        pass

def show_teams(teams):
    print (json.dumps(teams, indent=2))