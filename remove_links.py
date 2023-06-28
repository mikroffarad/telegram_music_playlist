import re

# Open the file in read mode
with open('input.txt', 'r') as file:
    # Read the contents of the file
    contents = file.read()

# Remove all links in the format (link) from the contents using regular expressions
contents = re.sub(r'\(\S+\)', '', contents)

# Open the file in write mode and write the modified contents
with open('output.txt', 'w') as file:
    file.write(contents)
