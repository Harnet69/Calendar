import ui


def main():
    # menu_list = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven"}
    menu_list = {'(s)': 'schedule a new meeting', '(c)': 'cancel an existing meeting', '(q)': 'quit'}
    # sub_menu_list = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five"}
    ui.print_menu(menu_list)
    user_answers = ui.user_input([''], "Make a choice:")
    ui.choose(user_answers)


if __name__ == "__main__":
    main()
