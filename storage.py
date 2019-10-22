import csv


def get_data_from_file(file_name):
    try:
        with open(file_name) as f:
            user_data = csv.reader(f, delimiter(','))
            return user_data
    except FileNotFoundError as e:
        print(e)


def write_data_to_file(file_name, user_data):
    with open(file_name, 'w') as f:
        schedule_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        schedule_writer.writerow(user_data)
    print('Meeting added.')
