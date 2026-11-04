from tabulate import tabulate
import json

def show_main_menu():
    # while True:
        menu_selection = input("""
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
0. Exit
Choose an option:
""")
        return menu_selection

def show_teams(teams):
    if teams == []:
        print ("----NO TEAMS----")
    else:     
        print (json.dumps(teams, indent=2))

def show_standings_table(sorted_teams):
    table = sorted_teams
    print (tabulate(table,headers="keys"))

def show_tournament_summary (tournament_summary):
        if tournament_summary == False:
             print ("no matches played in tournament")
             return
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