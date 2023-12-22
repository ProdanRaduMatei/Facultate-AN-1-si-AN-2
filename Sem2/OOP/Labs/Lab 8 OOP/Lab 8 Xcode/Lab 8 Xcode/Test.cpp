#include "Tests.h"
#include "Song.h"
#include "SongCollection.h"
#include <string>
#include <iostream>
#include <vector>
using namespace std;

int testSong() {
    Song s("title", "artist", {"lyrics"});
    return 0;
}

int testGetTitle() {
    Song s("title", "artist", {"lyrics"});
    if (s.getTitle() == "title") {
        return 0;
    }
    else {
        return 1;
    }
}

int testGetArtist() {
    Song s("title", "artist", {"lyrics"});
    if (s.getArtist() == "artist") {
        return 0;
    }
    else {
        return 1;
    }
}

int testGetLyrics() {
    Song s("title", "artist", {"lyrics"});
    if (s.getLyrics().size() == 1) {
        return 0;
    }
    else {
        return 1;
    }
}

int testDestructor() {
    Song *s = new Song("title", "artist", {"lyrics"});
    delete s;
    return 0;
}

int testSetTitle() {
    Song s("title", "artist", {"lyrics"});
    s.setTitle("new title");
    if (s.getTitle() == "new title") {
        return 0;
    }
    else {
        return 1;
    }
}

int testSetArtist() {
    Song s("title", "artist", {"lyrics"});
    s.setArtist("new artist");
    if (s.getArtist() == "new artist") {
        return 0;
    }
    else {
        return 1;
    }
}

int testSetLyrics() {
    Song s("title", "artist", {"lyrics"});
    s.setLyrics({"new lyrics"});
    if (s.getLyrics().size() == 1) {
        return 0;
    }
    else {
        return 1;
    }
}

int testDisplay() {
    Song s("title", "artist", {"lyrics"});
    s.display();
    return 0;
}

int testSongCollection() {
    SongCollection sc;
    return 0;
}

int testAddSong() {
    SongCollection sc;
    sc.addSong(Song("title", "artist", {"lyrics"}));
    return 0;
}

int testPrint() {
    SongCollection sc;
    sc.addSong(Song("title", "artist", {"lyrics"}));
    sc.print();
    return 0;
}

int testLoadFromFile() {
    SongCollection sc;
    sc.loadFromFile("songs.txt");
    return 0;
}

int testUniqueArtists() {
    SongCollection sc;
    sc.loadFromFile("songs.txt");
    cout << sc.uniqueArtists();
    return 0;
}

int testPrintTop10Artists() {
    SongCollection sc;
    sc.loadFromFile("songs.txt");
    sc.printTop10Artists();
    return 0;
}

int testSortSongs() {
    SongCollection sc;
    sc.loadFromFile("songs.txt");
    cout << "Sorting by artist..." << endl;
    sc.sortSongsByArtist();
    sc.print();
    cout << "Sorting by title..." << endl;
    sc.sortSongsByTitle();
    sc.print();
    cout << "Sorting by lyrics..." << endl;
    sc.sortSongsByLyrics();
    sc.print();
    return 0;
}

int testSearch() {
    SongCollection sc;
    sc.loadFromFile("songs.txt");
    vector<Song> results = sc.search("love");
    for (int i = 0; i < results.size(); i++) {
        results[i].display();
    }
    return 0;
}


int testAll() {
    int passed = 0;
    passed += testSong();
    passed += testGetTitle();
    passed += testGetArtist();
    passed += testGetLyrics();
    passed += testDestructor();
    passed += testSetTitle();
    passed += testSetArtist();
    passed += testSetLyrics();
    passed += testDisplay();
    passed += testSongCollection();
    passed += testAddSong();
    passed += testPrint();
    passed += testLoadFromFile();
    passed += testUniqueArtists();
    passed += testPrintTop10Artists();
    passed += testSortSongs();
    passed += testSearch();
    return passed;
}
