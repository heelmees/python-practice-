import json
import csv
import sys

def json_to_csv(json_file_path):
    with open(json_file_path) as json_file:
        data = json.load(json_file)

    root_name = json_file_path.split('.')[0]

    csv_file_path = f"{root_name}.csv"

    employees_data = data.get('Employees')

    with open(csv_file_path, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(employees_data[0].keys())
        for emp in employees_data:
            csv_writer.writerow(emp.values())

json_file_path = sys.argv[1]
json_to_csv(json_file_path)
