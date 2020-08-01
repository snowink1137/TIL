public class Song {
    public String title;
    public Artist artist;
    public Album album;

    public Song(String title, Artist artist, Album album) {
        this.title = title;
        this.artist = artist;
        this.album = album;
    }

    @Override
    public String toString() {
        return title + " - " + artist.name +"\n" + album.albumTitle + "(" + album.year + ")";
    }
}
