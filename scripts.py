import os
import storage
import ui
import scripts


# add a new meeting
def schedule_a_new_meeting(file_name):
    os.system('clear')
    print("Schedule a new meeting.\n 'Give title, duration and start time of the meeting: ")
    user_data = ui.get_user_input(['Enter meeting title: ', 'Enter duration in hours (1 or 2): ',
                    'Enter start time: '], "")
    converted_user_input = scripts.convert_user_input(user_data)  # Validate and convert user input 
    is_duration_valid = scripts.is_duration(converted_user_input)  # is duration is 1 ot 2 hour
    is_time_free = scripts.is_time_free(converted_user_input)
    if converted_user_input and is_duration_valid and is_time_free:
        storage.write_data_to_file(file_name, user_data)
    else:
        input('inappropriate time. Press enter to try again...')
        schedule_a_new_meeting(file_name)


# cancel a meeting
def cancel_a_meeting(file_name):
    print("Cancel an existing meeting.\n")
    user_time = ui.get_user_input(['Enter the start time: '], "")
    meeting_time_to_calcell = str(user_time[0])
    schedules_list = storage.get_data_from_file(file_name)
    schedules_list_after_cancellation = []
    cancelled_meetings = 0
    for task in schedules_list:
        start_time = task[2]
        if meeting_time_to_calcell == str(start_time):
            cancelled_meetings += 1
            continue
        schedules_list_after_cancellation.append(task)
    if not cancelled_meetings:
        print(f"ERROR: There is no meeting starting at the {time_to_delete} o'clock")
        input('Press enter to continue...')
        os.system('clear')
        cancel_a_meeting(file_name)
    storage.write_data_to_file(file_name, schedules_list_after_cancellation, False)


# sort schedule by start time
def sort_schedule(schedule):
    sorted_schedule = sorted(schedule, key=lambda x: x[2])
    return sorted_schedule


# convert user inputs to appropriate format
def convert_user_input(user_input):
    converted_user_input = []
    activity = user_input[0]
    converted_user_input.append(activity)
    try:
        duration = int(user_input[1])
        converted_user_input.append(duration)
        start_time = int(user_input[2])
        converted_user_input.append(start_time)
        return converted_user_input
    except ValueError:
        return False


#  Convert schedules list to appropriate format
def convert_schedule(schedule):
    converted_schedule = []
    for meeting in schedule:
        converted_meeting = convert_user_input(meeting)
        converted_schedule.append(converted_meeting)
    return converted_schedule


# validate a meeting duration
def is_duration(user_input):
    meeting_duration = user_input[1]
    if meeting_duration == 1 or meeting_duration == 2:
        return True


# check if time isn't occupied
def is_time_free(user_input):
    return True
