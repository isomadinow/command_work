import csv
from datetime import datetime
import json

data = {}
with open('n.csv') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if len(row) > 0:  # Check if the row is not empty
            date = f"{row[0]}.09"
            times = row[1:]
            data[date] = times

# Convert the data dictionary to JSON format
formatted_data = json.dumps(data)

# Write the formatted data to a JSON file
with open('kems.json', 'w') as f:
    f.write(formatted_data)
