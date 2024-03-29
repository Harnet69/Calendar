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
    is_working_time = scripts.is_working_time(converted_user_input)  # is meeting in workhours
    is_duration_valid = scripts.is_duration(converted_user_input)  # is duration is 1 ot 2 hour
    is_time_free = scripts.is_time_free(converted_user_input, file_name)

    if converted_user_input and is_working_time and is_duration_valid and is_time_free:
        storage.write_data_to_file(file_name, user_data)
    else:
        input('inappropriate time. Press enter to try again...')
        schedule_a_new_meeting(file_name)


# cancel a meeting
def edit_a_meeting(file_name, edit_mode="cancell"):
    print("Cancel an existing meeting.\n")
    user_time = ui.get_user_input(['Enter the start time: '], "")
    meeting_time_to_change = str(user_time[0])
    schedules_list = storage.get_data_from_file(file_name)
    schedules_list_after_editing = []

    if_meeting_exists = False
    for meeting in schedules_list:
        start_time = meeting[2]
        if meeting_time_to_change == str(start_time) and edit_mode == "cancell":
            if_meeting_exists = True
            continue
        schedules_list_after_editing.append(meeting)
    if not if_meeting_exists:
        print(f"ERROR: There is no meeting starting at the {time_to_delete} o'clock")
        input('Press enter to continue...')
        os.system('clear')
        edit_a_meeting(file_name)
    storage.write_data_to_file(file_name, schedules_list_after_editing, False)


# sort schedule by start time
def sort_schedule(schedule):
    sorted_schedule = sorted(schedule, key=lambda x: x[2])
    return sorted_schedule


# convert user inputs to appropriate format
def convert_user_input(user_input):
    converted_user_input = []
    try:
        activity = user_input[0].strip()
        converted_user_input.append(activity)
        duration = int(user_input[1])
        converted_user_input.append(duration)
        start_time = int(user_input[2])
        converted_user_input.append(start_time)
        return converted_user_input
    except ValueError:
        return False


#  convert schedules list to appropriate format
def convert_schedule(schedule):
    converted_schedule = []
    for meeting in schedule:
        converted_meeting = convert_user_input(meeting)
        converted_schedule.append(converted_meeting)
    return converted_schedule


# check is meeting is in worktime (between 8 and 18)
def is_working_time(user_input):
    meeting_start = user_input[2]
    meeting_duration = user_input[1]
    meeting_finish = meeting_start + meeting_duration
    if meeting_start >= 8 and meeting_finish <= 18:
        return True


# validate a meeting duration
def is_duration(user_input):
    meeting_duration = user_input[1]
    if meeting_duration == 1 or meeting_duration == 2:
        return True


# get meeting time from schedule
def get_meeting_timeline(schedule):
    schedule_timeline = []
    for meeting in schedule:
        meeting_start = int(meeting[2])
        meeting_duration = int(meeting[1])
        schedule_timeline.extend(range(meeting_start, meeting_start + meeting_duration))
    return schedule_timeline


# check if time isn't occupied
def is_time_free(user_input, file_name):
    schedule = sort_schedule(convert_schedule(storage.get_data_from_file(file_name)))
    meeting_hours = get_meeting_timeline([user_input])
    existing_meeting_timeline = get_meeting_timeline(schedule)
    if any(elem in existing_meeting_timeline for elem in meeting_hours):  # check if time is free
        return False
    return True
