
"""
Data Analytics Project 3
Data Processing and Analysis Module

This module demonstrates fetching data from various web sources, processing it using 
"""
 

######
# Import modules
######

# Standard Library Imports
import csv
import pathlib
import json
import logging
import collections
from collections import Counter
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


#####
# Function Definitions Text
#####

# Fetch txt data from a url and write it to a file
def fetch_and_write_txt_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        file_path = pathlib.Path(folder_name) / 'data.txt'
        with open(file_path, 'w') as file:
            file.write(response.text)
        print(f"Text data saved to {file_path}")

    except requests.exceptions.HTTPError as errh:
        print(f"Http Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Error Connecting: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Oops: Something Else: {err}")
    except IOError as e:
        print(f"I/O error({e.errno}): {e.strerror}")

# Write text data from the given URL
def write_txt_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).join_path(filename)
    with file_path.open('w') as file:
        file.write(data)
        print(f"Text data saved to {file_path}")

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
    
    with open(output_filename, 'w') as output_file:
        output_file.write(f"Total Words: {total_words}")
        output_file.write(f"Unique Words: {unique_words}")
        output_file.write(f"Word Frequency: {word_frequency}")
        for word, count in word_frequency.items():
            file.write(f"{word}: {count}")
   
    print(f"Text process completed. Data saved to {output_filename}")
    
except FileNotFoundError: 
    logging.error(f"Error: The file {filename} does not exist.")
except Exception as e:
    logging.error(f"An error occured {e}")


#######
# Function Definitions CSV
#######

# Fetch CSV data from a url and write it to a file
def fetch_and_write_csv_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
    # Call your write function to save response content
    else:
        print(f"Failed to fetch CSV data:{response.status_code}")

# Write CSV data to a file
def write_csv_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).join_path(filename)
    with file_path.open('w') as file:
        file.write(data)
        print(f"CSV data saved to {file_path}")

######
# Function Definitions Excel
######

# Fetch Excel data from a url and write it to a file
def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
    # Call your write function to save response content
    else:
        print(f"Failed to fetch Excel data:{response.status_code}")

def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).join_path(filename)
    with file_path.open('w') as file:
        file.write(data)
        print(f"Excel data saved to {file_path}")

########
# Function Definitions JSON
########

# Fetch JSON data from a url and write it to a file
def fetch_and_write_json_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
    # Call your write function to save response content
    else:
        print(f"Failed to fetch JSON data:{response.status_code}")

# Write JSON data to a file
def write_json_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).join_path(filename)
    with file_path.open('w') as file:
        file.write(data)
        print(f"JSON data saved to {file_path}")






# Main function to demonstrate module capabilities.
def main():

    # Print byline from imported module
    print(f"Byline: {seabaugh_utils.byline}")
    
    # Define the prefix for the folders
    prefix = 'data-'

    # Define the folder names for each data type
    folder_names = ['txt', 'csv', 'excel', 'json']

    # Create folders using the prefixed naming
    result = nickelias_project_setup.create_prefixed_folders(folder_names, prefix)
    print(result)

    # Define the base directory relative to the script's location
    base_dir = pathlib.Path(__file__).parent.joinpath('data')

    # Define URLs for data fetching
    txt_url = 
    csv_url = 
    excel_url = 
    json_url = 
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