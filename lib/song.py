class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Update counts and lists
        Song.count += 1
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.update_counts(artist, genre)

    @classmethod  
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def update_counts(cls, artist, genre):
        # Update genre count
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1
        
        # Update artist count
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1