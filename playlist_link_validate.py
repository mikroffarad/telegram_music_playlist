import re
import requests
import asyncio
import html

# ANSI escape codes for text color
COLOR1 = '\033[38;2;14;243;255m'
COLOR2 = '\033[38;2;255;46;151m'
RESET = '\033[0m'

def get_youtube_title(video_id):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        response = requests.get(url)
        title = re.search('<title>(.*?)</title>', response.text)
        if title:
            video_title = html.unescape(title.group(1))
            # Remove "- YouTube" snippet from the title
            video_title = re.sub(r"\s-\sYouTube$", "", video_title)
            return video_title
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while retrieving the title: {e}")
    return None

async def parse_line(line, results):
    line = line.strip()
    if line:
        match = re.search(r'\[(.*?)\]\s*\((https?://(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)[^\s]+)\)', line)
        if match:
            song_name = match.group(1)
            youtube_link = match.group(2)
            video_id = re.search("(?:youtube\.com/watch\?v=|youtu\.be/)([^\s&]+)", youtube_link).group(1)
            video_title = get_youtube_title(video_id)
            result = {
                'song_name': song_name,
                'youtube_link': youtube_link,
                'video_title': video_title if video_title else 'Failed to retrieve video title.'
            }
            results.append(result)
            print(f"{COLOR1}{song_name}{RESET}")
            print(f"{COLOR2}{video_title}{RESET}")
            print(f"{COLOR2}{youtube_link}{RESET}")
            print('==============')
        await asyncio.sleep(0.1)  # Add a small delay for better output formatting

async def check_text_file(file_path):
    with open(file_path, 'r', encoding="utf8") as file:
        lines = file.readlines()
        idx = 0
        results = []
        while idx < len(lines):
            line = lines[idx].strip()
            if line:
                task = parse_line(line, results)
                await task
                await asyncio.sleep(0)  # Allow other tasks to run
                try:
                    await asyncio.get_event_loop().run_in_executor(None, input, "Press Enter to continue...")
                except KeyboardInterrupt:
                    break  # Stop parsing if input is interrupted by Ctrl + C
                idx += 1
            else:
                idx += 1
    return results

# Example usage
file_path = "songs.txt"  # Replace with the path to your text file

async def main():
    results = await check_text_file(file_path)
    for result in results:
        song_name = result['song_name']
        youtube_link = result['youtube_link']
        video_title = result['video_title']
        print(f"{COLOR1}Song: {song_name}{RESET}")
        print(f"{COLOR1}Video title: {video_title}{RESET}")
        print(f"{COLOR2}YouTube link: {youtube_link}{RESET}")
        print('==============')

asyncio.run(main())