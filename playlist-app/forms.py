"""Forms for playlist app."""

from wtforms import SelectField, TextAreaField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField('Name', validators=[InputRequired("Playlist Name")])
    description = TextAreaField('Description', validators=[InputRequired("Playlist Description")])


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField('Title', validators=[InputRequired("Song Title")])
    artist = StringField('Artist', validators=[InputRequired("Artist Name")])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
