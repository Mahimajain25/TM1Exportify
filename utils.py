import csv
import pandas as pd
import openpyxl
import configparser
from TM1py.Services import TM1Service  # Ensure TM1Service is imported here

# Function to write data to a CSV file
def write_to_csv(filename, header, data):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)  # Writing the header
        for row in data:
            writer.writerow(row)  # Writing the data rows

# Function to write DataFrame to Excel
def write_to_excel(filename, df):
    df.to_excel(filename, index=False)

# Function to write data to Excel with multiple sheets
def write_to_excel_multiple_sheets(filename, sheet_data):
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        for sheet_name, df in sheet_data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)

# Function to get TM1 service connection (move from app.py)
def get_tm1_service():
    config = configparser.ConfigParser()
    config.read('config.ini')  # Ensure you have a valid 'config.ini' file
    return TM1Service(**config['tm1srv01'])  # Ensure 'tm1srv01' section exists in config.ini
