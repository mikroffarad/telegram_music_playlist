def convert_to_markdown(file_path):
    updated_lines = []
    with open(file_path, 'r', encoding="utf8") as file:
        for line in file:
            line = line.strip()
            if line:
                # Find the position of the YouTube link
                youtube_index = line.find('(https://youtu.be/')
                if youtube_index != -1:
                    # Extract the artist and title
                    artist_title = line[:youtube_index].strip()
                    youtube_link = line[youtube_index+1:-1].strip()
                    # Create the Markdown hyperlink
                    markdown_line = f"[{artist_title}]({youtube_link})"
                    updated_lines.append(markdown_line)
                else:
                    updated_lines.append(line)  # Preserve non-matching lines

    with open(file_path, 'w', encoding="utf8") as file:
        file.write('\n'.join(updated_lines))


# Example usage
input_file = 'songs.txt'  # Replace with the path to your input file
convert_to_markdown(input_file)
