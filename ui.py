import os


def print_menu(menu_list, name_menu="Menu:\n"):
    menu_list['(q)'] = "quit"
    os.system('clear')
    print(name_menu)
    # print(f"{'Num':<2}|Value|")
    # print('---------')
    for (key, value) in menu_list.items():
        print(f"{key:<3} {value}")
        # print('---------|')
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
        os.system('clear')
        print("Schedule a new meeting.\n")
        user_input([''], "Give title, duration and start time of the meeting:")
    if user_answers[0] == '(q)':
        os.sys.exit(0)
