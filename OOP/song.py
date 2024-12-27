# Python project to get used to Doc Strings, classes and methods

class Song:
    """Class to repersent a song

    Attributes:
        title (str): Title of the song
        artist (Artist): An Artist object of the song's creator
        duration (int): Length of song in seconds. Maybe zero
    """

    def __init__(self, title, artist, duration=0):
        """Song innit method

        args:
            title (str): Title of the song
            artist (Artist): An Artist object of the song's creator
            duration (Optional[int]): Length of song in seconds. Defaults to zero
        """
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """Class to repersent an Album, using it's track list

    Attributes:
        album_name (str): The name of the album
        year (int): Year of release
        arrist (Artist): Artist object responsible for the album.
            If none specified will default to "Various"
        tracks (list[songs]): List of songs
    
    Methods:
        add_song: Add a new song to the track list
    """    

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list

        Args:
            song (Song): A song to add
            position ([int], optional): If specified will be inserted 
            at this position, between songs. 
            Defaults to None which will add to the end of the list.
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)

class Artist:
    """Basic class to store artist details

    Attributes:
        name (str): Name of the artist
        albums (list[Album]): A lsit of albumbs by the artist

    Methods:
        add_album: Add a new album to the artist's album list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """Add new album to the list

        Args:
            album (Album): Add Album object to the list.
                If already present will not be added again.
        """
        self.albums.append(album)

def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("OOP/albums.txt","r") as albums:
        for line in albums:
            # data should be in format (arist, album, year, song)
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)

            new_song = Song(song_field, new_artist)
            new_album.add_song(new_song)
        
        if new_artist is not None:
            if new_album is not None:
                new_artist.add_album(new_album)
            artist_list.append(new_artist)
    
    return artist_list

def create_checkfile(artist_list):
    """create a checkfile from object data to compare with original data

    Args:
        artist_list (list): list of generated data
    """
    with open("checkfile.txt", 'w') as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print(f"{new_artist.name}\t{new_album.name}\t{new_album.year}\t{new_song.title}", 
                          file=checkfile)

if __name__ == '__main__':
    artists = load_data()
    print(len(artists))

    create_checkfile(artists)