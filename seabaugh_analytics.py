
"""
Data Analytics Project 3
Data Processing and Analysis Module

This module demonstrates fetching data from various web sources, processing it using 
"""
 



# Standard Library Imports
import csv
import pathlib
import json
import logging
import collections

# External Library Imports
import requests


# Local Module Imports
import seabaugh_utils
import seabaugh_project_setup

#Configure Logging to track events and errors
logging.basicConfig(level=logging.INFO)



#Function Definitions Text
def fetch_and_write_txt_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
    # Call your write function to save response content
    else:
        print(f"Failed to fetch txt data: {response.status_code}")


#Function Definitions CSV
def fetch_and_write_CSV_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
    # Call your write function to save response content
    else:
        print(f"Failed to fetch CSV data:{response.status_code}")
#Function Definitions Excel
def fetch_and_write_excel_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
    # Call your write function to save response content
    else:
        print(f"Failed to fetch Excel data:{response.status_code}")

#Function Definitions JSON

def fetch_and_write_JSON_data(folder_name, filename, url):
    response = requests.get(url)
    if response.status_code == 200:
    # Call your write function to save response content
    else:
        print(f"Failed to fetch JSON data:{response.status_code}")