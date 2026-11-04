from outputs import show_main_menu,show_teams,show_standings_table,show_tournament_summary
from teams_file import add_team
from matches_file import add_match
from standings import sort_teams,get_top_team,get_best_attacking_team,get_teams_without_wins,get_tournament_summary,get_team_success_rate

def run_application():
    teams = []
    matches = []

    while True:
        menu_selection = show_main_menu()
        while True:
            match menu_selection:
                    case "1":
                        add_team(teams)
                        inner_selection = application_inner_selection()
                        match inner_selection:
                            case "1": continue
                            case "2": break
                            case _: exit()

                    case "2":
                            show_teams(teams)
                            inner_selection = application_inner_selection()
                            match inner_selection:
                                case "1": continue
                                case "2": break
                                case _: exit()
                                
                                  
                                    
                    case "3":
                            add_match(teams,matches)
                            inner_selection = application_inner_selection()
                            match inner_selection:
                                case "1": continue
                                case "2": break
                                case _: exit()
                    case "4":
                            show_standings_table(sort_teams(teams))
                            inner_selection = application_inner_selection()
                            match inner_selection:
                                case "1": continue
                                case "2": break
                                case _: exit()
                    case "5":
                            show_teams(get_top_team(sort_teams(teams)))
                            inner_selection = application_inner_selection()
                            match inner_selection:
                                case "1": continue
                                case "2": break
                                case _: exit()
                    case "6":
                            if teams != []:
                                show_teams(get_best_attacking_team(teams))
                                inner_selection = application_inner_selection()
                                match inner_selection:
                                    case "1": continue
                                    case "2": break
                                    case _: exit()
                            else:
                                  print ("no teams returning to main menu")
                                  break
                    case "7":
                            show_teams(get_team_success_rate(teams,matches))
                            inner_selection = application_inner_selection()
                            match inner_selection:
                                case "1": continue
                                case "2": break
                                case _: exit()
                    case "8":
                            show_teams(get_teams_without_wins(teams))
                            inner_selection = application_inner_selection()
                            match inner_selection:
                                case "1": continue
                                case "2": break
                                case _: exit()
                    case "9":
                            show_tournament_summary(get_tournament_summary(teams,matches))
                            inner_selection = application_inner_selection()
                            match inner_selection:
                                case "1": continue
                                case "2": break
                                case _: exit()

                    case "0":
                            exit()
                    case _:
                        print("invalid input try again")
                        break


def application_inner_selection():
        inner_selection = input("""
1. repeat selection
2. return to main menu
ANY OTHER KEY -> exit application
""")
        return inner_selection