import csv


def get_list_to_insert(process_row):
    list_to_insert = []
    with open('./Electric_Vehicle_Population_Data.csv', 'r') as file:
        csvreader = csv.reader(file, delimiter=',')
        row_counter = 0
        for row in csvreader:
            if row_counter == 0:
                row_counter = row_counter + 1
                continue

            process_row(list_to_insert, row)
            row_counter = row_counter + 1
    return list_to_insert


def get_factories_to_insert(process_row):
    factories_to_insert = []
    with open('./factories.csv', 'r') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            process_row(factories_to_insert, row)
        return factories_to_insert
