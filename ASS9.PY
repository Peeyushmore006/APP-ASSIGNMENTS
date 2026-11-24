
# Experiment 9: CSV to JSON Conversion

import csv
import json

# Create a sample CSV file
with open("input.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Write column headings
    writer.writerow(["Name", "Age", "City"])

    # Write student records
    writer.writerow(["Alice", 20, "Pune"])
    writer.writerow(["Bob", 21, "Mumbai"])
    writer.writerow(["Charlie", 19, "Delhi"])


# Read CSV and convert into JSON
data = []

with open("input.csv", "r") as csv_file:

    # Read CSV data as dictionaries
    reader = csv.DictReader(csv_file)

    for row in reader:
        data.append(row)


# Write data into JSON file
with open("output.json", "w") as json_file:

    json.dump(data, json_file, indent=4)


print("CSV file successfully converted into JSON!")

# Display JSON data
print("\nJSON Data:")

with open("output.json", "r") as file:
    print(file.read())
