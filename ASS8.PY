
# Experiment 8: File Handling

# Create an input file with sample data
with open("input.txt", "w") as file:
    file.write("Python Programming\n")
    file.write("Advanced Python\n")
    file.write("File Handling\n")
    file.write("Regular Expressions\n")
    file.write("Data Analysis\n")


# Open the input file in read mode
with open("input.txt", "r") as file:

    # Read all lines into a list
    lines = file.readlines()

    # Count total number of lines
    total_lines = len(lines)

    # Extract the first two lines
    first_two_lines = lines[:2]


# Display total lines
print("Total number of lines:", total_lines)


# Write first two lines into output file
with open("output.txt", "w") as file:

    file.writelines(first_two_lines)

print("First two lines written to output.txt")


# Display the extracted lines
print("Content of output.txt:")

with open("output.txt", "r") as file:
    print(file.read())
