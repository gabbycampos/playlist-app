## Playlist-app

To get this application running, make sure you do the following in the Terminal:

1. `python3 -m venv venv`
2. `source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `createdb playlist-app`
5. `flask run`

< This application allows a user to create songs and playlists and add a song to a playlist. The data model will allow for many songs to be part of many different playlists and allow for many different playlists to include many different songs.

#### Technologies used in the project:
- Flask
- WTForms
- PostgreSQL
