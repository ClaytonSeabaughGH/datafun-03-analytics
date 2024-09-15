
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


#####
# Function Definitions Text
#####

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
            file.write(f"{word}: {count}")
   
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
    response.raise_for_status()
    

# Write CSV data to a file
def write_csv_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).join_path(filename)
    with file_path.open('w') as file:
        file.write(data)
        logging.info(f"CSV data saved to {file_path}")

# Processes CSV data to generate statistics and summaries. Saves results to an output file. 
def process_csv_file(folder_name, filename, output_filename):
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
        with open(output_filename, 'w') as file
            file.write("CSV Data Analysis\n")
            file.write("\n".join(summary))
        logging.info(f"CSV processing completed. Data saved to {output_filename}")
    except FileNotFoundError:
        logging.error(f"Error: The file {file_path} does not exist.")
    except Exception as e:
        logging.error(f"An error occured {e}")



######
# Function Definitions Excel
######

# Fetch Excel data from a url and write it to a file
def fetch_and_write_excel_data(folder_name, filename, url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        write_excel_file(folder_name, filename, response.content)
    except requests.excepts.RequestException as err:
        logging.error(f"Error fetching Excel data: {err}")

# Write Excel file to a file
def write_excel_file(folder_name, filename, data):
    file_path = pathlib.Path(folder_name).join_path(filename)
    with file_path.open('w') as file:
        file.write(data)
        logging.info(f"Excel data saved to {file_path}")

# Process an Excel file to generate statistics and summaries. Saves results to an output file.


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



