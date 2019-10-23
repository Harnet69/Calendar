import os
import storage
import ui


def schedule_a_new_meeting(file_name):
    os.system('clear')
    print("Schedule a new meeting.\n 'Give title, duration and start time of the meeting: ")
    user_data = ui.user_input(['Enter meeting title: ', 'Enter duration in hours (1 or 2): ',
                    'Enter start time: '], "")
    storage.write_data_to_file(file_name, user_data)


def cancel_an_existing_meeting(file_name):
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


def sort_schedule(schedule):  # TODO not working with str values, fix after an implementation of validation
    sorted_schedule = schedule.sort(key=lambda x: x[2])
    return sorted_schedule


def str_to_num_conversion(user_str):
    try:
        user_num = str(user_str)
        return user_num
    except ValueError:
        return False
