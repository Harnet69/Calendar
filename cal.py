import os
import ui
import scripts


def choose(user_answers, file_name):
    if user_answers[0] == 's':
        scripts.schedule_a_new_meeting(file_name)
    if user_answers[0] == 'c':
        scripts.cancel_an_existing_meeting(file_name)
    if user_answers[0] == 'q':
        os.sys.exit(0)


def main():
    while True:
        file_name = 'schedule.csv'
        menu_list = {'(s)': 'schedule a new meeting', '(c)': 'cancel an existing meeting', '(q)': 'quit'}
        ui.print_schedule(file_name)
        ui.print_menu(menu_list)
        user_answers = ui.user_input([''], "Make a choice:")
        try:
            choose(user_answers, file_name)
        except KeyError as err:
            print(str(err))


if __name__ == "__main__":
    main()
