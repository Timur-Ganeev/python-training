from read_file import read_file_by_line_while_gen as read_file
import os

filePath = "automation/data/sensor_with_errors.csv"
dirPath = os.path.dirname(os.getcwd())
dataPath = os.path.join(dirPath, filePath)


def process_line_v1(line: str):
    data_list = []
    split_line = [word.strip() for word in line.split(",")]
    data_list.append(f"{split_line[0]} {split_line[1]}")
    for i in split_line[2:]:
        try:
            data_list.append(float(i))
        except ValueError:
            data_list.append(None)
    return data_list


def is_correct_value(value):
    return value is not None

log_data = [process_line_v1(line) for line in read_file(dataPath)]

col3_sum = 0.0
for index, item in enumerate(log_data):
    n = item[3]
    if is_correct_value(n):
        col3_sum += n
    else:
        print(f"Is not correct value! Id: {index} {n}")

print(log_data)
print(col3_sum)
