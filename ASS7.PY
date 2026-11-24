
# Experiment 7: Email Extraction using Regex

import re

# Function to find email addresses
def find_emails(text):

    # Regular expression pattern for email addresses
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # Find all matching email addresses
    emails = re.findall(pattern, text)

    return emails


# Sample text
text = """
Contact us at abc@gmail.com
or xyz123@yahoo.com
You can also email student@college.edu
"""

# Call the function
result = find_emails(text)

# Display the extracted emails
print("Email addresses found:")

for email in result:
    print(email)
