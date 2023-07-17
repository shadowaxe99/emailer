# This is the utilities module

# Import necessary libraries
import os
import json
import csv
import pandas as pd
from datetime import datetime
import logging
import sys

# Define a function to read a JSON file

def read_json_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError('File not found: {}'.format(file_path))

    # Open the file and load the JSON data
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Return the data
    return data

# Define a function to write data to a JSON file

def write_json_file(file_path, data):
    # Open the file and dump the JSON data
    with open(file_path, 'w') as file:
        json.dump(data, file)

# Define a function to read a CSV file using pandas

def read_csv_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError('File not found: {}'.format(file_path))

    # Read the CSV data into a pandas DataFrame
    data = pd.read_csv(file_path)

    # Return the DataFrame
    return data

# Define a function to write data to a CSV file using pandas

def write_csv_file(file_path, data):
    # Convert the data to a pandas DataFrame
    df = pd.DataFrame(data)

    # Write the DataFrame to a CSV file
    df.to_csv(file_path, index=False)

# Define a function to get the current date and time

def get_current_datetime():
    # Get the current date and time
    now = datetime.now()

    # Return the current date and time as a string
    return now.strftime('%Y-%m-%d %H:%M:%S')

# Define a function to set up logging

def setup_logging(log_file):
    # Set up logging
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s %(message)s')

    # Return the logger
    return logging.getLogger()

# Define a function to exit the program

def exit_program():
    # Print a goodbye message
    print('Goodbye!')

    # Exit the program
    sys.exit()

# Define a function to convert a DataFrame to a list of dictionaries

def df_to_list_of_dicts(df):
    # Convert the DataFrame to a list of dictionaries
    data = df.to_dict('records')

    # Return the list of dictionaries
    return data

# Define a function to convert a list of dictionaries to a DataFrame

def list_of_dicts_to_df(data):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(data)

    # Return the DataFrame
    return df