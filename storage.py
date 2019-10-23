import csv


def get_data_from_file(file_name):
    try:
        with open(file_name, newline='') as f:
            user_data = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            schedule_list = []
            for item in user_data:
                schedule_list.append(item)
            return schedule_list
    except FileNotFoundError as e:
        print(e)


def write_data_to_file(file_name, user_data, write_one_row='True'):
    try:
        if write_one_row:
            with open(file_name, 'a') as f:
                schedule_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                schedule_writer.writerow(user_data)
        else:
            with open(file_name, 'w') as f:
                schedule_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                schedule_writer.writerows(user_data)
    except FileNotFoundError as e:
        print(e)
