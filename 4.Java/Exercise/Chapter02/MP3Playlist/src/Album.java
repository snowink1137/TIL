import java.util.ArrayList;

public class Album {
    public String albumTitle;
    public int year;
    public Artist artist;
    ArrayList<Song> tracks;

    public Album(String albumTitle, int year, Artist artist) {
        this.albumTitle = albumTitle;
        this.year = year;
        this.artist = artist;
        this.tracks = new ArrayList<>();
    }

    public void addTrack(Song song) {
        tracks.add(song);
    }

    public Song getTrack(int i) {
        return tracks.get(i-1);
    }
}
