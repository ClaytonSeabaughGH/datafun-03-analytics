'''Data Project No 2!!

This project demonstrates proficiency in loops, project folder creation using pathlib, and importing modules.

This module provides functions for creating a series of project folders
'''

########## Import Modules ############


#Import modules from python libraries
import pathlib
import time
import os

#Import local modules
import seabaugh_utils

########## Declare Global Variables #########

# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

# Duration of time between folders
duration_secs = 5

###### Define functions for folder creation ########

# Function 1: Generates folders for a given range (years)
start_year = 2020
end_year = 2023
def create_folders_for_range(start_year: int, end_year: int) -> None:
    for year in range(start_year, end_year + 1 ):
        year_path = project_path.joinpath(str(year))
        year_path.mkdir(exist_ok=True)
        time.sleep(duration_secs)

 # Log the function call and its arguments using an f-string
print(f"FUNCTION CALLED: create_folders_for_range with start_year={start_year} and end_year={end_year}")


# Function 2: Creates folders from a list of names 
folder_id = ['data-csv', 'data-excel', 'data-json']
to_lowercase = True
remove_spaces = True
def create_folders_from_list(folder_list: list, to_lowercase = True, remove_spaces = True) -> None:
  for folder_id in folder_list:
     # Apply transformations if specified
      if to_lowercase == True:
        folder_id = folder_id.lower()
      if remove_spaces== True:
        folder_id = folder_id.replace(' ', '_')
        folder_path = project_path.joinpath(str(folder_id))
        folder_path.mkdir(exist_ok=True)
  time.sleep(duration_secs)
print(f"FUNCTION CALLED: create_folders_from_list with '{folder_id}'")


# Function 3: Creates prefixed folders by combinging a list of names with a prefix
folder_id = ['csv', 'excel', 'json']
prefix = 'data-'
def create_prefixed_folders(folder_list: list, prefix: str) -> None:
  for folder_id in folder_list:
  # Create the full folder name with prefix
    folder_path = project_path / f"{prefix}-{folder_id}"
    folder_path.mkdir(exist_ok=True)
time.sleep(duration_secs)
print(f"FUNCTION CALLED: create_folders_from_list with '{folder_id}'")


# Function 4: A While Loop that creates folders periodically

def create_folders_periodically(duration):
 #loop continously to create folders, until program is stopped
    folder_counter = 0
    
    while folder_counter < number_of_folders:
        # Define the folder path
        folder_path = project_path.joinpath(f"folder_{folder_counter}")
        
        # Create the folder if it doesn't already exist
        folder_path.mkdir(exist_ok=True)
        
        # Print a message indicating the folder creation
        print(f"Created folder: {folder_path}")
        
        # Wait for the specified duration
        time.sleep(duration_secs)
        
        # Increment the counter
        folder_counter += 1

print(f"FUNCTION CALLED: create_folders_periodically duration_seconds{duration_secs}")

########### Define Main Function ###########

def main():

  ''' Main function to demonstrate module capabilities. '''

print("#####################################")
print("# Starting execution of main()")
print("#####################################\n") 


# Print byline from imported module
print(f"Byline: {seabaugh_utils.byline}")

    # Call function 1 to create folders for a range (e.g. years)
create_folders_for_range(start_year=2020, end_year=2023)

    # Call function 2 to create folders given a list
folder_id = ['data-csv', 'data-excel', 'data-json']
create_folders_from_list(folder_id)

    # Call function 3 to create folders using comprehension
folder_id = ['csv', 'excel', 'json']
prefix = 'data-'
create_prefixed_folders(folder_id, prefix)

    # Call function 4 to create folders periodically using while
duration_secs = 5  # duration in seconds
number_of_folders = 5
folder_counter = 0
create_folders_periodically(duration_secs)

    # Add options e.g., to force lowercase and remove spaces 
    # to one or more of your functions (e.g. function 2) 
regions = [
      "North America", 
      "South America", 
      "Europe", 
      "Asia", 
      "Africa", 
      "Oceania", 
      "Middle East"
    ]
create_folders_from_list(regions, to_lowercase=True, remove_spaces=True)


# End of main execution
print("\n#####################################")
print("# Completed execution of main()")
print("#####################################")

# Conditional Script Execution
if __name__ == '__main__':
    main()



