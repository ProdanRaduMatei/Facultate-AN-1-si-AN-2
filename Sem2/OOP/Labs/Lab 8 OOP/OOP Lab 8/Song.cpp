#include "Song.h"
#include <string>
#include <iostream>
#include <vector>
using namespace std;

Song::Song(string _title, string _artist, vector <string> _lyrics) {
    title = _title;
    artist = _artist;
    lyrics = _lyrics;
}

string Song::getTitle() const {
    return title;
}

string Song::getArtist() const {
    return artist;
}

vector <string> Song::getLyrics() const {
    return lyrics;
}

void Song::setTitle(string _title) {
    title = _title;
}

void Song::setArtist(string _artist) {
    artist = _artist;
}

void Song::setLyrics(vector <string> _lyrics) {
    lyrics = _lyrics;
}

void Song::display() const {
    cout << "Title: " << title << endl;
    cout << "Artist: " << artist << endl;
    cout << "Lyrics: " << endl;
    for (int i = 0; i < lyrics.size(); i++) {
        cout << lyrics[i] << endl;
    }
}
