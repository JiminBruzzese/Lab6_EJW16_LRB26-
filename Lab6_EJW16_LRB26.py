# lab6_s24
# lab6_1
import csv

def read_csv_file(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
filename="birthplace.csv"
read_csv_file('birthplace.csv')

# lab6_2
import csv

def read_csv_as_list(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            csv_list = list(reader)
            return csv_list
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

filename = 'birthplace.csv' 
csv_content = read_csv_as_list(filename)
if csv_content:
    print(csv_content)
    
# lab6_3
import csv
def read_csv_as_dict(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            csv_dict = list(reader)
            return csv_dict
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


filename = 'birthplace.csv'  
csv_content = read_csv_as_dict(filename)
if csv_content:
    print(csv_content)

# lab6_4
mport csv

def read_csv_as_dict(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file, skipinitialspace=True)
            csv_dict = list(reader)
            return csv_dict
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


filename = 'birthplace.csv' 
csv_content = read_csv_as_dict(filename)
if csv_content:
    print(csv_content)

# lab6_5
import csv

def process_csv(filename, delimiter=','):
    processed_data = []
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file, delimiter=delimiter, skipinitialspace=True)
            for row in reader:
                processed_row = []
                for entry in row:
                    # Remove initial spaces and quotes
                    entry = entry.strip().strip('"')
                    processed_row.append(entry)
                processed_data.append(processed_row)
        return processed_data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

filename = 'birthplace.csv' 
processed_content = process_csv(filename)
if processed_content:
    print(processed_content)

# lab6_6
import csv

def read_specific_columns(filename, columns):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                selected_columns = [row[i] for i in columns]
                print(selected_columns)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IndexError:
        print("Error: Specified column index out of range.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

filename = 'birthplace.csv' 
columns_to_read = [0, 1]  # how many columns to read
read_specific_columns(filename, columns_to_read)

# lab6_7
import csv

def read_csv_without_header(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

filename = 'birthplace.csv'  
read_csv_without_header(filename)

# lab6_8
import csv

def write_csv(filename, data):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)
        print(f"Data has been written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred while writing to '{filename}': {str(e)}")

def read_csv_and_print(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while reading '{filename}': {str(e)}")


filename = 'birthplace.csv'


data_to_write = [
    ['Code', 'Birthplace', 'Census_night_population_count', 'Census_usually_resident_population_count'],
    ['1', 'At sea', '15', '15'],
    ['1000', 'Oceania and Antarctica (not further defined)', '0', '0'],
    ['1101', 'Australia', '83622', '75696'],
    ['1102', 'Norfolk Island', '114', '108'],
    ['1199', 'Australian External Territories nec', '0', '0'],
    ['1201', 'New Zealand', '3378357', '3370122'],
    ['1300', 'Melanesia (not further defined)', '0', '0'],
    ['1301', 'New Caledonia', '381', '318'],
    ['1302', 'Papua New Guinea', '1587', '1482']
]


write_csv(filename, data_to_write)


print("Data from CSV file:")
read_csv_and_print(filename)
# lab6_9
import csv

def write_list_of_lists_to_csv(filename, data):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Data has been written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred while writing to '{filename}': {str(e)}")

def read_csv_and_display_content(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while reading '{filename}': {str(e)}")


filename = 'birthplace.csv'

data_to_write = [
    ['Code', 'Birthplace', 'Census_night_population_count', 'Census_usually_resident_population_count'],
    ['1', 'At sea', '15', '15'],
    ['1000', 'Oceania and Antarctica (not further defined)', '0', '0'],
    ['1101', 'Australia', '83622', '75696'],
    ['1102', 'Norfolk Island', '114', '108'],
    ['1199', 'Australian External Territories nec', '0', '0'],
    ['1201', 'New Zealand', '3378357', '3370122'],
    ['1300', 'Melanesia (not further defined)', '0', '0'],
    ['1301', 'New Caledonia', '381', '318'],
    ['1302', 'Papua New Guinea', '1587', '1482']
]


write_list_of_lists_to_csv(filename, data_to_write)


print("Data from CSV file:")
read_csv_and_display_content(filename)
# lab6_10
import csv

def write_dict_to_csv(filename, data):
    try:
        with open(filename, 'w', newline='') as file:
            fieldnames = data[0].keys() if data else []
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data has been written to '{filename}' successfully.")
    except Exception as e:
        print(f"An error occurred while writing to '{filename}': {str(e)}")

def read_csv_and_display_content(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred while reading '{filename}': {str(e)}")


filename = 'birthplace.csv'  


data_to_write = [{'Code': '1', 'Birthplace': 'At sea', 'Census_night_population_count': '15', 'Census_usually_resident_population_count': '15'}, {'Code': '1000', 'Birthplace': 'Oceania and Antarctica (not further defined)', 'Census_night_population_count': '0', 'Census_usually_resident_population_count': '0'}, {'Code': '1101', 'Birthplace': 'Australia', 'Census_night_population_count': '83622', 'Census_usually_resident_population_count': '75696'}, {'Code': '1102', 'Birthplace': 'Norfolk Island', 'Census_night_population_count': '114', 'Census_usually_resident_population_count': '108'}, {'Code': '1199', 'Birthplace': 'Australian External Territories nec', 'Census_night_population_count': '0', 'Census_usually_resident_population_count': '0'}, {'Code': '1201', 'Birthplace': 'New Zealand', 'Census_night_population_count': '3378357', 'Census_usually_resident_population_count': '3370122'}, {'Code': '1300', 'Birthplace': 'Melanesia (not further defined)', 'Census_night_population_count': '0', 'Census_usually_resident_population_count': '0'}, {'Code': '1301', 'Birthplace': 'New Caledonia', 'Census_night_population_count': '381', 'Census_usually_resident_population_count': '318'}, {'Code': '1302', 'Birthplace': 'Papua New Guinea', 'Census_night_population_count': '1587', 'Census_usually_resident_population_count': '1482'}]



write_dict_to_csv(filename, data_to_write)


print("Data from CSV file:")
read_csv_and_display_content(filename)

# lab6_11

import csv

def read_csv_without_header(filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Define other functions for programs 2-10 similarly

def main():
    # Example usage of each function
    filename = 'example.csv'
    read_csv_without_header(filename)
    # Call other functions here with appropriate arguments

if __name__ == "__main__":
    main()

-----------------------------------
from csv_operations.operations import birthplace


read_csv_without_header('birthplace.csv')
# lab6_12
import sys
import os
import csv_operations.operations as csv_ops


module_dir = os.path.abspath('csv_operations')
sys.path.append(module_dir)

def display_menu():
    """Display the menu options."""
    print("\nMenu:")
    print("1. Read CSV without header")
    print("2. Write data to CSV")
    print("3. Read specific columns from CSV")
    print("4. Read CSV as list of lists")
    print("5. Read CSV as list of dictionaries")
    print("6. Write list of lists to CSV")
    print("7. Write list of dictionaries to CSV")
    print("8. Read and print specific columns from CSV")
    print("9. Read CSV and skip header")
    print("0. Exit")

def read_csv_without_header_menu():
    """Menu for reading CSV without header."""
    filename = input("Enter the filename: ")
    csv_ops.read_csv_without_header(filename)

def write_data_to_csv_menu():
    """Menu for writing data to CSV."""
    filename = input("Enter the filename: ")
    data = eval(input("Enter the data as a list of lists: "))
    csv_ops.write_data_to_csv(filename, data)


def main():
    """Main function to run the program."""
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        
        if choice == '1':
            read_csv_without_header_menu()
        elif choice == '2':
            write_data_to_csv_menu()
        # Add other function calls for other menu options similarly
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
