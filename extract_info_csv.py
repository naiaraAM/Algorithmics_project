import os

def convert_to_csv():
    with open("Data/stops.txt", 'r') as file:
        lines = file.readlines()
        with open('stops.csv', 'w') as new_file:
            for line in lines:
                new_file.write(line.replace(',', ';'))

def extract_relevant_info():
    with open("stops.csv", 'r') as file:
        lines = file.readlines()
        with open('tartu_stops.csv', 'w') as new_file:
            # write header
            new_file.write(lines[0])
            for line in lines:
                if line.split(';')[-1] == "Tartu LV\n": # filter ny Tartu Linn
                    new_file.write(line)

    # remove stops.csv
    os.remove("stops.csv")

def obtain_tartu_stops():
    convert_to_csv()
    extract_relevant_info()
    print(f"File tartu_stops.csv created in {os.getcwd()}")
