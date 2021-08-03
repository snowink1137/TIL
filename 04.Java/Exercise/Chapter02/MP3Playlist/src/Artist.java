import java.util.ArrayList;

public class Artist {
    public String name;
    ArrayList<Album> albums;

    public Artist(String name) {
        this.name = name;
        albums = new ArrayList<>();
    }

    public void addAlbum(Album album) {
        albums.add(album);
    }

    public ArrayList<Album> getAlbums() {
        return albums;
    }
}
