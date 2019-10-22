import os
import storage


def print_menu(menu_list, name_menu='Menu:'):
    menu_list['(q)'] = "quit"
    print(name_menu)
    for (key, value) in menu_list.items():
        print(f"{key:<3} {value}")
    print('\n')


def print_schedule(file_name):
    schedule = storage.get_data_from_file(file_name)
    print('Your schedule for the day:')
    # print(f"{'Begin':>2} - {'End':>2} {'Task':^10}")
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


def choose(user_answers):
    if user_answers[0] == 's':
        # os.system('clear')
        print("Schedule a new meeting.\n 'Give title, duration and start time of the meeting: ")
        user_data = user_input(['Enter meeting title: ', 'Enter duration in hours (1 or 2): ',
                     'Enter start time: '], "")
        storage.write_data_to_file('schedule.csv', user_data)
    if user_answers[0] == '(q)':
        os.sys.exit(0)
