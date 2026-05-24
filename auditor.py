import csv
import os

# Ye code isi folder mein 'tasks.csv' ko dhoondhega
file_path = 'tasks.csv'

def run_auditor():
    if not os.path.exists(file_path):
        print("Error: 'tasks.csv' file nahi mili.")
        return

    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        print("--- Nexus Audit ---")
        for row in reader:
            print(f"Task: {row['Task']} | Status: {row['Status']}")

run_auditor()