
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

# Configured Logger instance
logger = logging.getLogger()

#####
# Function Definitions Text
#####

# Fetch txt data from a url and write it to a file
def fetch_and_write_txt_data(folder_name, filename, url):
try:
    response = requests.get(url)
    if response.status_code == 200:
    else:
        print(f"Failed to fetch txt data: {response.status_code}")

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
    print(f"Error: The file {filename} does not exist.")
except Exception as e:
    print(f"An error occured {e}")


#######
# Function Definitions CSV
#######

# Fetch CSV data from a url and write it to a file
def fetch_and_write_CSV_data(folder_name, filename, url):
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
def fetch_and_write_JSON_data(folder_name, filename, url):
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