#include "RepositoryTest.h"

void RepositoryTest::runTests() {
    testAddSong();
    testFindSong();
    testRemoveSong();
}

void RepositoryTest::testAddSong() {
    Repository repository;
    Song song("Title", "Artist", { "Lyrics" }, 999, "URL");

    repository.addSong(song);

    // Retrieve the songs from the repository and check if the added song exists
    const std::vector<Song>& songs = repository.getSongs();
    assert(songs.size() == 1);
    assert(songs[0] == song);
}

void RepositoryTest::testFindSong() {
    Repository repository;
    Song song("Title", "Artist", { "Lyrics" }, 1000, "URL");

    repository.addSong(song);

    // Search for the added song
    const Song& foundSong = repository.find("Title", "Artist");
    assert(foundSong == song);
}

void RepositoryTest::testRemoveSong() {
    Repository repository;
    Song song("Title", "Artist", { "Lyrics" }, 2023, "URL");

    repository.addSong(song);
    repository.remove(song);

    // Retrieve the songs from the repository and check if the song has been removed
    const std::vector<Song>& songs = repository.getSongs();
    assert(songs.empty());
}