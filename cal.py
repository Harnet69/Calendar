import ui

import os


def main():
    menu_list = {'(s)': 'schedule a new meeting', '(c)': 'cancel an existing meeting', '(q)': 'quit'}
    os.system('clear')
    ui.print_schedule('schedule.csv')
    ui.print_menu(menu_list)
    user_answers = ui.user_input([''], "Make a choice:")
    ui.choose(user_answers)


if __name__ == "__main__":
    main()
