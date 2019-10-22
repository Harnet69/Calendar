import os


menu_list = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven"}
sub_menu_list = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}


def print_menu(menu_list, name_menu="Main menu:\n"):
    menu_list[0] = "Exit"
    os.system('clear')
    print(name_menu)
    print(f"{'Num':<2}|Value|")
    print('---------')
    for (key, value) in menu_list.items():
        print(f"{key:<3}|{value:>5}|")
        print('---------|')


def user_input(user_question_list, message):
    user_answers = []
    for item in user_question_list:
        print(message)
        user_item = input(f'{item}')
        user_answers.append(user_item)
    return user_answers


def choose(user_answers):
    if user_answers[0] == '1':
        print_menu(sub_menu_list, "First point menu:\n")
        user_input([''], "Make a choice:")
    if user_answers[0] == '0':
        os.sys.exit(0)


def main():
    user_question = ['name', 'age', 'city']
    print_menu(menu_list)
    user_answers = user_input([''], "Make a choice:")
    choose(user_answers)


if __name__ == "__main__":
    main()
