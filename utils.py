import csv
import pandas as pd
import openpyxl
import configparser
from TM1py.Services import TM1Service  # Ensure TM1Service is imported here

# Function to write data to a CSV file
import csv
import os

# Function to write data to a CSV file inside the 'Export' folder
def write_to_csv(filename, header, data):
    # Ensure the 'Export' directory exists
    if not os.path.exists('Export'):
        os.makedirs('Export')  # Create the directory if it doesn't exist

    # Create the full file path inside the 'Export' folder
    file_path = os.path.join('Export', filename)
    
    # Writing data to CSV
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)  # Writing the header
        for row in data:
            writer.writerow(row)  # Writing the data rows
    print(f"File saved to {file_path}")


# Function to write DataFrame to Excel
def write_to_excel(filename, df):
    # Ensure the 'Export' directory exists
    if not os.path.exists('Export'):
        os.makedirs('Export')  # Create the directory if it doesn't exist

    # Create the full file path inside the 'Export' folder
    file_path = os.path.join('Export', filename)
    
    # Write the DataFrame to an Excel file
    df.to_excel(file_path, index=False)
    print(f"File saved to {file_path}")


# Function to write data to Excel with multiple sheets
def write_to_excel_multiple_sheets(filename, sheet_data):
    # Ensure the 'Export' directory exists
    if not os.path.exists('Export'):
        os.makedirs('Export')  # Create the directory if it doesn't exist

    # Create the full file path inside the 'Export' folder
    file_path = os.path.join('Export', filename)
    
    # Write the DataFrame with multiple sheets
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        for sheet_name, df in sheet_data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    print(f"File saved to {file_path}")

# Function to get TM1 service connection (move from app.py)
def get_tm1_service():
    config = configparser.ConfigParser()
    config.read('config.ini')  # Ensure you have a valid 'config.ini' file
    return TM1Service(**config['tm1srv01'])  # Ensure 'tm1srv01' section exists in config.ini
