#include "Tests.h"
#include "Song.h"
#include "SongCollection.h"
#include <string>
#include <iostream>
#include <vector>
using namespace std;

int testSong() {
    Song s("title", "artist", {"lyrics"}, 2023, "exemplu_link");
    cout << "testSong PASSED" << endl;
    return 0;
}

int testGetTitle() {
    Song s("title", "artist", {"lyrics"}, 2023, "exemplu_link");
    if (s.get_Title() == "title") {
        cout << "testGetTitle PASSED" << endl;
        return 0;
    }
    else {
        return 1;
    }
}

int testGetArtist() {
    Song s("title", "artist", {"lyrics"}, 2023, "exemplu_link");
    if (s.get_Artist() == "artist") {
        cout << "testGetArtist PASSED" << endl;
        return 0;
    }
    else {
        return 1;
    }
}

int testGetLyrics() {
    Song s("title", "artist", {"lyrics"}, 2023, "exemplu_link");
    if (s.get_Lyrics().size() == 1) {
        cout << "testGetLyrics PASSED" << endl;
        return 0;
    }
    else {
        return 1;
    }
}

int testDestructor() {
    Song* s = new Song("title", "artist", {"lyrics"}, 2023, "exemplu_link");
    delete s;
    cout << "testDestructor PASSED" << endl;
    return 0;
}

int testSetTitle() {
    Song s("title", "artist", {"lyrics"}, 2023, "exemplu_link");
    s.set_Title("new title");
    if (s.get_Title() == "new title") {
        cout << "testSetTitle PASSED" << endl;
        return 0;
    }
    else {
        return 1;
    }
}

int testSetArtist() {
    Song s("title", "artist", {"lyrics"}, 2023, "exemplu_link");
    s.set_Artist("new artist");
    if (s.get_Artist() == "new artist") {
        cout << "testSetArtist PASSED" << endl;
        return 0;
    }
    else {
        return 1;
    }
}

int testSetLyrics() {
    Song s("title", "artist", {"lyrics"}, 2023, "exemplu_link");
    s.set_Lyrics({"new lyrics"});
    if (s.get_Lyrics().size() == 1) {
        cout << "testSetLyrics PASSED" << endl;
        return 0;
    }
    else {
        return 1;
    }
}

int testDisplay() {
    Song s("title", "artist", {"lyrics"}, 2023, "exemplu_link");
    s.display();
    cout << "testDisplay PASSED" << endl;
    return 0;
}

int testSongCollection() {
    Song_Collection sc;
    cout << "testSongCollection PASSED" << endl;
    return 0;
}

int testAddSong() {
    Song_Collection sc;
    sc.add_Song(Song("title", "artist", {"lyrics"}, 2023, "exemplu_link"));
    cout << "testAddSong PASSED" << endl;
    return 0;
}

int testPrint() {
    Song_Collection sc;
    sc.add_Song(Song("title", "artist", {"lyrics"}, 2023, "exemplu_link"));
    sc.print();
    cout << "testPrint PASSED" << endl;
    return 0;
}

int testLoadFromFile() {
    Song_Collection sc;
    sc.load_From_File("songs.txt");
    cout << "testLoadFromFile PASSED" << endl;
    return 0;
}

int testUniqueArtists() {
    Song_Collection sc;
    sc.load_From_File("songs.txt");
    cout << sc.unique_Artists();
    cout << "testUniqueArtists PASSED" << endl;
    return 0;
}

int testTop10Artists() {
    Song_Collection sc;
    sc.load_From_File("songs.txt");
    sc.Top_10_Artists();
    cout << "testTop10Artists PASSED" << endl;
    return 0;
}

int testSortSongs() {
    Song_Collection sc;
    sc.load_From_File("songs.txt");
    cout << "Sorting by artist..." << endl;
    sc.sort_Songs_By_Artist();
    sc.print();
    cout << "Sorting by title..." << endl;
    sc.sort_Songs_By_Title();
    sc.print();
    cout << "Sorting by lyrics..." << endl;
    sc.sort_Songs_ByLyrics();
    sc.print();
    cout << "testSortSongs PASSED" << endl;
    return 0;
}

int testSearch() {
    Song_Collection sc;
    sc.load_From_File("songs.txt");
    vector<Song> results = sc.search("love");
    for (unsigned long i = 0; i < results.size(); i++) {
        results[i].display();
    }
    cout << "testSearch PASSED" << endl;
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
    passed += testTop10Artists();
    passed += testSortSongs();
    passed += testSearch();
    return passed;
}
