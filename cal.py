import os
import ui
import storage


def schedule_a_new_meeting(file_name):
    os.system('clear')
    print("Schedule a new meeting.\n 'Give title, duration and start time of the meeting: ")
    user_data = ui.user_input(['Enter meeting title: ', 'Enter duration in hours (1 or 2): ',
                    'Enter start time: '], "")
    storage.write_data_to_file(file_name, user_data)


def cancel_an_existing_meeting(file_name):
    # os.system('clear')
    print("Cancel an existing meeting.\n")
    user_time = ui.user_input(['Enter the start time: '], "")
    time_to_delete = str(user_time[0])
    schedules_list = storage.get_data_from_file(file_name)
    schedules_list_after_deleting = []
    deleted_task = 0
    for task in schedules_list:
        start_time = task[2]
        if time_to_delete == str(start_time):
            deleted_task += 1
            continue
        schedules_list_after_deleting.append(task)
    if deleted_task == 0:
        print(f"ERROR: There is no meeting starting at the {time_to_delete} o'clock")
        input('Press enter to continue...')
        os.system('clear')
        cancel_an_existing_meeting(file_name)
    storage.write_data_to_file(file_name, schedules_list_after_deleting, False)


def choose(user_answers, file_name):
    if user_answers[0] == 's':
        schedule_a_new_meeting(file_name)
    if user_answers[0] == 'c':
        cancel_an_existing_meeting(file_name)
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
