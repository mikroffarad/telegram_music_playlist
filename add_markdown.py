def wrap_lines_in_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        wrapped_lines = []
        for line in lines:
            title = line.strip()
            wrapped_line = f"[{title}]()"
            wrapped_lines.append(wrapped_line)
    with open(filename, 'w') as file:
        file.write('\n'.join(wrapped_lines))

# Example usage
wrap_lines_in_file('input.txt')
