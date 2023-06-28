def remove_spaces_from_file(filename):
    with open(filename, 'r') as file:
        # Read the contents of the file
        contents = file.readlines()

    # Remove spaces from the beginning of each line
    stripped_lines = []
    for line in contents:
        stripped_line = line.lstrip()
        stripped_lines.append(stripped_line)

    # Write the stripped lines back to the file
    with open(filename, 'w') as file:
        file.writelines(stripped_lines)

# Example usage
remove_spaces_from_file('input.txt')
