
"""
Data Analytics Project 3
Data Processing and Analysis Module

This module demonstrates fetching data from various web sources, processing it using 
"""
 

################
# Import modules
################

# Standard Library Imports
import csv
import pathlib
import json
import logging
from collections import Counter
from collections import defaultdict
import re

# External Library Imports
import requests
import pandas as pd

# Local Module Imports
import seabaugh_utils
import seabaugh_project_setup

# Configure Logging to track events and errors
logging.basicConfig(filename='text_analysis.log', 
  level=logging.INFO, 
  filemode='w', 
  format='%(name)s.%(levelname)s.%(message)s')


###########################
# Function Definitions Text
###########################

# Fetch txt data from a url and write it to a file
def fetch_and_write_txt_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_txt_file(folder_name, filename, response.text)
    except requests.RequestException as e:
        logging.error(f"Failed to fetch dta from {url}: {e}")

# Write text data from the given URL
def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).join_path(filename)
    with file_path.open('w') as file:
        file.write(data)
    logging.info(f"Text data saved to {file_path}")

# Processes text Data and generates statistics. Formats to a text file. 
def process_text_data(folder_name, filename, output_filename):
    
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
   # Read the entire text from input file
        with open(file_path, 'r') as file:
            text = file.read()

       # Normalize text to lowercase and split into words
        words = re.findall(r'\b\w+\b', text.lower())

       # Calculate total word count and unique word count
        total_words = len(words)
        unique_words = len(set(words))

       # Calculate frequency of words 
        word_frequency = Counter(words)
    
    # Write results to output file
        with open(output_filename, 'w') as output_file:
            output_file.write(f"Total Words: {total_words}")
            output_file.write(f"Unique Words: {unique_words}")
            output_file.write(f"Word Frequency: {word_frequency}")
        for word, count in word_frequency.items():
            output_file.write(f"{word}: {count}")
   
    except FileNotFoundError: 
        logging.error(f"Error: The file {filename} does not exist.")
    
    except Exception as e:
        logging.error(f"An error occured {e}")


##########################
# Function Definitions CSV
##########################

# Fetch CSV data from a url and write it to a file
def fetch_and_write_csv_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_csv_file(folder_name, filename, response.text)
    except requests.RequestException as e:
        logging.error(f"Failed to fetch CSV data from {url}: {e}")

# Write CSV data to a file
def write_csv_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open('w', newline='') as file:
        file.write(data)
    logging.info(f"CSV data saved to {file_path}")

# Processes CSV data to generate statistics and summaries. Saves results to an output file. 
def process_csv_data(folder_name, filename, output_filename):
    
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        # Initialize data storage
        column_data = defaultdict(list)
        column_count = defaultdict(int)

        # read CSV data
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader) # Get headers from the first row

            # Process each row 
            for row in reader:
                for header, value in zip(headers, row):
                    column_data[header].append(value)
                    column_count[header] += 1
        # Analyze Data
        summary = []
        for header in headers:
            values = column_data[header]
            total_values = len(values)
            unique_values = len(set(values))
            summary.append(f"Column '{header}:\n")
            summary.append(f"  Total Values: {total_values}\n")
            summary.append(f"  Unique values: {unique_values}\n")
        # Write results to the output file
        with open(output_filename, 'w') as file:
            file.write("CSV Data Analysis\n")
            file.write("\n".join(summary))
        logging.info(f"CSV processing completed. Data saved to {output_filename}")
    
    except FileNotFoundError:
        logging.error(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        logging.error(f"An error occured {e}")



############################
# Function Definitions Excel
############################

# Fetch Excel data from a url and write it to a file
def fetch_and_write_excel_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_excel_file(folder_name, filename, response.content)
    except requests.exceptions.RequestException as err:
        logging.error(f"Error fetching Excel data: {err}")

# Write Excel file to a file
def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open('wb') as file:
        file.write(data)
    logging.info(f"Excel data saved to {file_path}")

# Process an Excel file to generate statistics and summaries. Saves results to an output file.
def process_excel_data(folder_name, filename, output_filename):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
         # Read Excel file into a DataFrame
        df = pd.read_excel(file_path, sheet_name=None)
        sheet_names= df.keys()
        # Prep the summary of each sheet
        summary = []
        for sheet_name in sheet_names:
            data = df[sheet_name]
        
            summary.append(f"Sheet: {sheet_name}\n")
            summary.append(f"Number of Rows: {data.shape[0]}\n")
            summary.append(f"Number of Columns: {data.shape[1]}\n")
            summary.append(f"Columns: {', '.join(data.columns)}\n")
            summary.append("\nSummary Statistics:\n")
            summary.append(data.describe(include='all').to_string())
            summary.append("\n\n")
    
    # Write results to the output file
        with open(output_filename, 'w') as file:
            file.write("Excel Data Analysis:\n")
            file.write("\n".join(summary))
        logging.info(f"Excel processing complete. Data saved to {output_filename}")
    except FileNotFoundError:
        logging.error(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        logging.error(f"An error occure: {e}")



###########################
# Function Definitions JSON
###########################

# Fetch JSON data from a url and write it to a file
def fetch_and_write_json_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_json_file(folder_name, filename, response.json())
    except requests.exceptions.RequestException as err:
        logging.error(f"Error fetching JSON data: {err}")
   
# Write JSON data to a file
def write_json_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).joinpath(filename)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open('w') as file:
        json.dump(data, file, indent=4)
    logging.info(f"JSON data saved to {file_path}")

# Process a JSOn file to extract data and save results to an output file.
def process_json_data(folder_name, filename, output_filename):
    
    file_path = pathlib.Path(folder_name).joinpath(filename)
    try:
        # Read JSON data from the input file
        with open(file_path, 'r') as file:
            data = json.load(file)
        # Prepare the summary of the JSON data
        summary = []
        def process_dict(d, indent_level=0):
            
            # Recursively process a dictionary to create a human-readable summary.
            
            for key, value in d.items():
                indent = '  ' * indent_level
                if isinstance(value, dict):
                    summary.append(f"{indent}{key}:")
                    process_dict(value, indent_level + 1)
                elif isinstance(value, list):
                    summary.append(f"{indent}{key}:")
                    process_list(value, indent_level + 1)
                else:
                    summary.append(f"{indent}{key}: {value}")

        def process_list(lst, indent_level=0):
            
            # Recursively process a list to create a human-readable summary.
            
            for item in lst:
                if isinstance(item, dict):
                    summary.append('  ' * indent_level + '-')
                    process_dict(item, indent_level + 1)
                elif isinstance(item, list):
                    summary.append('  ' * indent_level + '-')
                    process_list(item, indent_level + 1)
                else:
                    summary.append('  ' * indent_level + f"- {item}")

        # Process the JSON data
        if isinstance(data, dict):
            process_dict(data)
        elif isinstance(data, list):
            process_list(data)
        else:
            summary.append(str(data))

        # Write results to the output file
        with open(output_filename, 'w') as file:
            file.write("JSON Data Summary:\n")
            file.write("\n".join(summary))
        
        logging.info(f"JSON processing completed. Data saved to {output_filename}")

    except FileNotFoundError:
        logging.error(f"Error: The file {file_path} does not exist.")
    except json.JSONDecodeError:
        logging.error(f"Error: The file {file_path} does not contain valid JSON.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")



###################################################
# Main function to demonstrate module capabilities.
###################################################
def main():

    # Print byline from imported module
    print(f"Byline: {seabaugh_utils.byline}")
    
    # Define the prefix for the folders
    prefix = 'data-'

    # Define the folder names for each data type
    folder_names = ['txt', 'csv', 'excel', 'json']

    # Create folders using the prefixed naming
    result = seabaugh_project_setup.create_prefixed_folders(folder_names, prefix)
    print(result)

    # Define the base directory relative to the script's location
    base_dir = pathlib.Path(__file__).parent.joinpath('data')

    # Define URLs for data fetching
    txt_url = 'https://shakespeare.mit.edu/hamlet/full.html'
    csv_url = 'https://raw.githubusercontent.com/LearnDataSci/articles/master/Python%20Pandas%20Tutorial%20A%20Complete%20Introduction%20for%20Beginners/IMDB-Movie-Data.csv'
    excel_url = 'https://github.com/bharathirajatut/sample-excel-dataset/raw/master/cattle.xls'
    json_url =  'http://api.open-notify.org/astros.json'

    # Define filenames for data storage
    txt_filename = 'data.txt'
    csv_filename = 'data.csv'
    excel_filename = 'data.xls'
    json_filename = 'data.json'

    # Define full paths for each folder
    txt_folder = pathlib.Path(base_dir).joinpath(f'{prefix}txt')
    csv_folder = pathlib.Path(base_dir).joinpath(f'{prefix}csv')
    excel_folder = pathlib.Path(base_dir).joinpath(f'{prefix}excel')
    json_folder = pathlib.Path(base_dir).joinpath(f'{prefix}json')

    # Fetch and write data to files
    fetch_and_write_txt_data(txt_folder, txt_filename, txt_url)
    fetch_and_write_csv_data(csv_folder, csv_filename, csv_url)
    fetch_and_write_excel_data(excel_folder, excel_filename, excel_url)
    fetch_and_write_json_data(json_folder, json_filename, json_url)

    # Process the fetched data
    process_text_data(txt_folder, txt_filename, 'results_txt.txt')
    process_csv_data(csv_folder, csv_filename, 'results_csv.txt')
    process_excel_data(excel_folder, excel_filename, 'results_xls.txt')
    process_json_data(json_folder, json_filename, 'results_json.txt')

    print("Data fetching and processing complete.")


if __name__ == "__main__":
    main()