import re


def extract_emails(text):
    # Use regular expression to find email addresses
    emails = re.findall(
        r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    return emails


# Read text from file
with open('text.txt', 'r') as file:
    input_text = file.read()

# Extract emails from input text
emails = extract_emails(input_text)

# Initialize a set to store unique emails
unique_emails = set()

# Check if output file already exists and read its content
try:
    with open('output.txt', 'r') as output_file:
        existing_emails = output_file.readlines()
        unique_emails.update([email.strip() for email in existing_emails])
except FileNotFoundError:
    pass

# Append unique emails to the set
unique_emails.update(emails)

# Write unique emails to the output file
with open('output.txt', 'w') as output_file:
    for email in unique_emails:
        output_file.write(email + '\n')

print("Emails extracted and saved to output.txt.")
