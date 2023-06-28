import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up your Spotify API credentials
client_id = input('Client ID:')
client_secret = input('Client secret:')

# Authenticate with Spotify using your credentials
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Get the playlist ID from the playlist's URI or URL
playlist_link = input('Playlist link:')

# Retrieve the playlist tracks
results = sp.playlist_tracks(playlist_id)

# Iterate over the tracks and print the artist and track name
print("Songs in the playlist:")
for item in results['items']:
    track = item['track']
    artist = track['artists'][0]['name']
    track_name = track['name']
    print(f"{artist} - {track_name}")
