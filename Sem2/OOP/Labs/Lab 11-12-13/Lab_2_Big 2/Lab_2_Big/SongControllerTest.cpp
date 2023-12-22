#include "SongControllerTest.h"

void SongControllerTest::runTests() {
    testAddSong();
    testSearchSong();
    testGetFilesByArtist();
    testGetFilesByTitle();
}

void SongControllerTest::testAddSong() {
    Repository repository;
    SongController controller(repository);

    // Add a new song using the SongController
    controller.addSong("Title", "Artist", { "Lyrics" }, "URL");

    // Retrieve the songs from the repository and check if the added song exists
    const std::vector<Song>& songs = repository.getSongs();
    assert(songs.size() == 1);
    assert(songs[0].get_Title() == "Title");
    assert(songs[0].get_Artist() == "Artist");
}

void SongControllerTest::testSearchSong() {
    Repository repository;
    SongController controller(repository);

    // Add a new song using the SongController
    controller.addSong("Title", "Artist", { "Lyrics" }, "URL");

    // Search for the added song
    const Song& foundSong = controller.searchSong("Title", "Artist");
    assert(foundSong.get_Title() == "Title");
    assert(foundSong.get_Artist() == "Artist");
}

void SongControllerTest::testGetFilesByArtist() {
    Repository repository;
    SongController controller(repository);

    // Add some songs to the repository
    controller.addSong("Title1", "Artist1", { "Lyrics1" }, "URL1");
    controller.addSong("Title2", "Artist2", { "Lyrics2" }, "URL2");
    controller.addSong("Title3", "Artist1", { "Lyrics3" }, "URL3");

    // Retrieve the songs sorted by artist
    std::vector<Song> songsByArtist = controller.getFilesByArtist();

    // Add assertions to verify the order of the songs if needed
    // assert(songsByArtist[0].get_Artist() == "Artist1");
    // assert(songsByArtist[1].get_Artist() == "Artist1");
    // assert(songsByArtist[2].get_Artist() == "Artist2");
}

void SongControllerTest::testGetFilesByTitle() {
    Repository repository;
    SongController controller(repository);

    // Add some songs to the repository
    controller.addSong("Title3", "Artist1", { "Lyrics3" }, "URL3");
    controller.addSong("Title1", "Artist2", { "Lyrics1" }, "URL1");
    controller.addSong("Title2", "Artist2", { "Lyrics2" }, "URL2");

    // Retrieve the songs sorted by title
    std::vector<Song> songsByTitle = controller.getFilesByTitle();

    // Add assertions to verify the order of the songs if needed
    // assert(songsByTitle[0].get_Title() == "Title1");
    // assert(songsByTitle[1].get_Title() == "Title2");
    // assert(songsByTitle[2].get_Title() == "Title3");
}