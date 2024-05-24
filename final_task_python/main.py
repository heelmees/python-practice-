import csv
import os
import random


def load_csv(filename, separator=','):
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=separator)
        data = [row for row in reader]
    return data


def show(data, view_type='top', num_rows=5):
    header = data[0]
    rows = data[1:]

    if len(rows) < num_rows:
        print(f"В таблице недостаточно строк. Всего строк: {len(rows)}")
        num_rows = len(rows)

    if view_type == 'top':
        data_to_show = rows[:num_rows]
    elif view_type == 'bottom':
        data_to_show = rows[-num_rows:]
    elif view_type == 'random':
        data_to_show = random.sample(rows, num_rows)

    print_table([header] + data_to_show)


def print_table(data):
    col_widths = [max(len(str(value)) for value in column) for column in zip(*data)]
    row_format = ' | '.join(f'{{:<{width}}}' for width in col_widths)

    print(row_format.format(*data[0]))
    for row in data[1:]:
        print(row_format.format(*row))


def info(data):
    header = data[0]
    rows = data[1:]
    num_rows = len(rows)
    num_cols = len(header)

    print(f"{num_rows}x{num_cols}")
    column_info = []
    for col_index, column_name in enumerate(header):
        # Подсчет количества непустых значений в столбце
        non_null_count = sum(1 for row in rows if row[col_index].strip())
        # Определение типа данных для столбца
        col_type = infer_type([row[col_index] for row in rows if row[col_index].strip()])
        # Добавление информации о столбце в список
        column_info.append(f"{column_name}: {non_null_count} ненулевых значений, type: {col_type}")

    for info in column_info:
        print(info)


def infer_type(values):
    for value in values:
        try:
            int(value)
            return "int"
        except:
            try:
                float(value)
                return "float"
            except:
                return "str"
    return "str"


def del_nan(data):
    header = data[0]
    rows = data[1:]
    initial_rows = len(rows)
    rows = [row for row in rows if all(field.strip() for field in row)]
    remaining_rows = len(rows)
    print(f"Удалено строк: {initial_rows - remaining_rows}")
    return [header] + rows


def make_ds(data):
    if not os.path.exists('workdata'):
        os.makedirs('workdata')
    if not os.path.exists('workdata/Learning'):
        os.makedirs('workdata/Learning')
    if not os.path.exists('workdata/Testing'):
        os.makedirs('workdata/Testing')

    header = data[0]
    rows = data[1:]

    train_size = int(len(rows) * 0.7)
    train_data = random.sample(rows, train_size)
    test_data = [row for row in rows if row not in train_data]

    save_csv('workdata/Learning/train.csv', [header] + train_data)
    save_csv('workdata/Testing/test.csv', [header] + test_data)
    print("Данные успешно разделены и сохранены.")


def save_csv(filename, data, separator=','):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, delimiter=separator)
        writer.writerows(data)


filename = 'Titanic.csv'
separator = ','

data = load_csv(filename, separator)
show(data, view_type='top', num_rows=5)
info(data)
data_cleaned = del_nan(data)
make_ds(data_cleaned)