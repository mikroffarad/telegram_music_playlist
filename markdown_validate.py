import re
from pytube import YouTube

# Regular expression to match YouTube Music links
regex = r"(?:https?:\/\/)?(?:www\.)?music\.youtube\.com\/watch\?v=([a-zA-Z0-9_-]{11})"

# Read input file line by line
with open("input.txt", "r") as f:
    for line in f:
        # Extract YouTube Music link from line
        match = re.search(regex, line)
        if match:
            # Get video title and content
            yt = YouTube(match.group())
            title = yt.title
            content = re.search(r"\[(.*?)\]", line).group(1)
            # Output title and content before link
            print(f"{content}")
            print(f"{title}")
            print("================")