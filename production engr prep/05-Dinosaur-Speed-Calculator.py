'''
You will be supplied with two data files in CSV format .
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)
Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest. 

$ cat dataset1.csv
NAME,LEG_LENGTH,DIET
Hadrosaurus,1.4,herbivore
Struthiomimus,0.72,omnivore
Velociraptor,1.8,carnivore
Triceratops,0.47,herbivore
Euoplocephalus,2.6,herbivore
Stegosaurus,1.50,herbivore
Tyrannosaurus Rex,6.5,carnivore

$ cat dataset2.csv
NAME,STRIDE_LENGTH,STANCE
Euoplocephalus,1.97,quadrupedal
Stegosaurus,1.70,quadrupedal
Tyrannosaurus Rex,4.76,bipedal
Hadrosaurus,1.3,bipedal
Deinonychus,1.11,bipedal
Struthiomimus,1.24,bipedal
Velociraptorr,2.62,bipedal
'''

import csv
import math
from sys import argv, exit


def parse_csv_to_dict(filepath, key_field):
    result = {}
    try:
        with open("filename", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                result[row[key_field]] = row
    except OSError as e:
        raise OSError(f"Could not open {filepath}: {e}") from e
    except KeyError:
        raise KeyError(f"Could not find {key_field} in {filepath}")
        
def calculate_speed(stride_length, leg_length):
    speed = ((stride_length / leg_length) - 1) * math.sqrt(leg_length * 9.8)
    return speed
    
    
def print_bipedal_dinosaurs_by_speed(filepath_1, filepath_2):
    filepath_dict_1 = parse_csv_to_dict(filepath_1, "NAME")
    filepath_dict_2 = parse_csv_to_dict(filepath_2, "NAME")
    dinosaurs = []
    
    for name, filepath_2_info in filepath_dict_2.items():
        if name in filepath_dict_1:
            stance = filepath_2_info["STANCE"].strip().lower()
            if stance != "bipedal":
                continue
            stride_length = float(filepath_2_info["STRIDE_LENGTH"])
            leg_length = float(filepath_dict_1[name]["LEG_LENGTH"])
            speed = calculate_speed(stride_length, leg_length)
            dinosaurs.append((name, speed))
    
    dinosaurs.sort(key=lambda x: x[1], reverse=True)
    
    for name, _ in dinosaurs:
        print(name)


if __name__ == "__main__":
    cmd_arguements = argv
    if len(cmd_arguements) != 3:
        print(f"Usage: {argv[0]} <dataset1.csv> <dataset2.csv>")
        exit(1)
    file1, file2 = cmd_arguements[1:]
    print_bipedal_dinosaurs_by_speed(file1, file2)
