import os
import re
import youtube_dl

# Read the file containing YouTube Music links
with open('input.txt', 'r') as f:
    links = f.readlines()

# Loop through each link and download the audio
for link in links:
    # Extract the video ID from the link
    video_id = re.findall(r'(?<=v=)[\w-]+', link)[0]
    # Set the options for downloading the audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{video_id}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    # Download the audio
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link.strip()])
    # Rename the downloaded file to the content between []
    title = re.findall(r'\[(.*?)\]', link)[0]
    os.rename(f'{video_id}.mp3', f'{title}.mp3')