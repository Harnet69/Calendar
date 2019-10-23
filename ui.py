import os
import storage


def print_menu(menu_list, name_menu='Menu:'):
    menu_list['(q)'] = "quit"
    print(name_menu)
    for (key, value) in menu_list.items():
        print(f"{key:<3} {value}")
    print('\n')


def print_schedule(file_name):
    os.system('clear')
    schedule = storage.get_data_from_file(file_name)
    print('Your schedule for the day:')
    for task in schedule:
        activity = task[0]
        start_time = int(task[2])
        duration = int(task[1])
        finish_time = start_time + duration
        print(f'{start_time:>2} - {finish_time:>2} {activity}')
    print('\n')


def user_input(user_question_list, message):
    user_answers = []
    for item in user_question_list:
        print(message)
        user_item = input(f'{item}')
        user_answers.append(user_item)
    return user_answers
