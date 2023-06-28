# Read the songs from the text file
file_path = 'songs.txt'

with open(file_path, 'r', encoding="utf8") as file:
    songs = [line.strip() for line in file]

# Sort the songs in alphabetical order by artist (case-insensitive)
sorted_songs = sorted(songs, key=lambda song: song.split(' - ')[0].lower())

# Write the sorted song list back to the input file
with open(file_path, 'w', encoding="utf8") as file:
    for song in sorted_songs:
        file.write(song + '\n')

print("The songs have been sorted and saved back to the input file.")
