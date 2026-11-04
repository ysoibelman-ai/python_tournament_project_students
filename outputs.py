from tabulate import tabulate
from standings import sort_teams,get_top_team,get_best_attacking_team,get_team_success_rate,get_teams_without_wins,get_tournament_summary
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
                        show_standings_table(sort_teams(teams))
            case "5":
                        show_teams(get_top_team(sort_teams(teams)))
            case "6":
                        show_teams(get_best_attacking_team(teams))
            case "7":
                        show_teams(get_team_success_rate(teams))
            case "8":
                        show_teams(get_teams_without_wins(teams))
            case "9":
                        show_tournament_summary(get_tournament_summary(teams,matches))
            case "10":
                        pass
            case "0":
                        exit()

def show_teams(teams):
    print (json.dumps(teams, indent=2))

def show_standings_table(sorted_teams):
    table = sorted_teams
    print (tabulate(table,headers="keys"))

def show_tournament_summary (tournament_summary):
        number_of_teams,number_of_games,total_goals,goal_avg_per_game,total_draw_games,leading_team = tournament_summary
        print(f"""
---- TOURNAMENT SUMMARY ----
NUMBER OF TEAMS: {number_of_teams}
NUMBER OF GAMES: {number_of_games}
TOTAL GOALS: {total_goals}
GOAL AVG PER GAME: {goal_avg_per_game}
TOTAL DRAW GAMES: {total_draw_games}
LEADING TEAM: {show_teams(leading_team)}
""")