#include "FileRepositoryTest.h"

void FileRepositoryTest::runTests() {
    testLoadSongs();
    testSaveSongs();
}

void FileRepositoryTest::testLoadSongs() {
    FileRepository repository("songs.txt");
    repository.load();

    // Retrieve the songs froim the repository and check if they are loaded correctly
    const std::vector<Song>& songs = repository.getSongs();
    assert(songs.size() == 2);

    // Add additional assertions to verify the loaded songs if needed
    // assert(songs[0].get_Title() == "Song1" && songs[0].get_Artist() == "Artist1");
    // assert(songs[1].get_Title() == "Song2" && songs[1].get_Artist() == "Artist2");
}

void FileRepositoryTest::testSaveSongs() {
    FileRepository repository("songs.txt");
    repository.addSong(Song("Title1", "Artist1", { "Lyrics1" }, 2023, "URL1"));
    repository.addSong(Song("Title2", "Artist2", { "Lyrics2" }, 2023, "URL2"));
    repository.save();

    // Load the saved songs and verify if they match the added songs
    repository.load();
    const std::vector<Song>& songs = repository.getSongs();
    assert(songs.size() == 2);
    // Add additional assertions to verify the saved songs if needed
}
