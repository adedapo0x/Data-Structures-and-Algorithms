import csv
import math

def parse_csv_to_dict(filepath, key_field):
    data = {}
    with open(filepath, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data[row[key_field]] = row
    return data

def calculate_speed(stride_length, leg_length):
    speed = ((stride_length / leg_length) - 1 * math.sqrt(leg_length * 9.8))
    return speed
    
    
def main(filepath_1, filepath_2):
    filepath_dict_1 = parse_csv_to_dict(filepath_1, "NAME")
    filepath_dict_2 = parse_csv_to_dict(filepath_2, "NAME")
    dinosaurs = []
    
    for name, filepath_2_info in filepath_dict_2.items():
        if name in filepath_dict_1:
            stance = filepath_2_info["STANCE"].strip().lower()
            if stance != bipedal:
                continue
            stride_length = float(filepath_2_info["STRIDE_LENGTH"])
            leg_length = float(filepath_dict_1[name]["LEG_LENGTH"])
            speed = calculate_speed(stride_length, leg_length)
            dinosaurs.append((name, speed))
    
    dinosaurs.sort(key=lambda x: x[1], reverse=True)
    
    for name, _ in dinosaurs:
        print(name)