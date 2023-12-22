#pragma once
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <stdexcept>
#include "SongCollection.h"
using namespace std;


Song_Collection::Song_Collection() {
    songs = vector<Song>();
}


// adding a song
void Song_Collection::add_Song(Song song) {
    songs.push_back(song);
}


// printing a song
void Song_Collection::print() {
    for (unsigned long i = 0; i < songs.size(); i++) {
        songs[i].display();
    }
}



// loading from a file
void Song_Collection::load_From_File(string filepath) {
    ifstream file(filepath);
    if (!file.fail()) {
        throw std::invalid_argument("Couldn't load file! \n");
    }
    string line;
    string artist;
    string title;
    vector<string> lyrics;
    while (getline(file, line)) {
        if (line.find("ARTIST=") != string::npos) {
            artist = line.substr(7);
        } else if (line.find("TITLE=") != string::npos) {
            title = line.substr(6);
        } else if (line.find("LYRICS=") != string::npos) {
            lyrics.push_back(line.substr(7));
        } else if (line == "") {
            Song song(artist, title, lyrics, 0, "URL");
            add_Song(song);
            lyrics.clear();
        }
    }
}


// getting the unique artist
int Song_Collection::unique_Artists() {
    vector<string> artists;
    for (unsigned long i = 0; i < songs.size(); i++) {
        bool found = false;
        for (unsigned long j = 0; j < artists.size(); j++) {
            if (songs[i].get_Artist() == artists[j]) {
                found = true;
                break;
            }
        }
        if (!found) {
            artists.push_back(songs[i].get_Artist());
        }
    }
    return artists.size();
}


// getting TOP 10
void Song_Collection::Top_10_Artists() {
    map<string, int> artistCounts;
    for (unsigned long i = 0; i < songs.size(); i++) {
        string artist = songs[i].get_Artist();
        if (artistCounts.find(artist) == artistCounts.end()) {
            artistCounts[artist] = 1;
        } else {
            artistCounts[artist]++;
        }
    }
    vector<pair<string, int>> sortedArtists(artistCounts.begin(), artistCounts.end());
    sort(sortedArtists.begin(), sortedArtists.end(), [](pair<string, int> a, pair<string, int> b) {
        return a.second > b.second;
    });
    int count = 0;
    for (auto it = sortedArtists.begin(); it != sortedArtists.end() && count < 10; it++, count++) {
        cout << it->first << ": " << it->second << " songs" << endl;
    };
}


// sorting by artists
void Song_Collection::sort_Songs_By_Artist() {
    sort(songs.begin(), songs.end(), [](Song a, Song b) {
        return a.get_Artist() < b.get_Artist();
    });
}


// sorting by title
void Song_Collection::sort_Songs_By_Title() {
    sort(songs.begin(), songs.end(), [](Song a, Song b) {
        return a.get_Title() < b.get_Title();
    });
}


// sorting by lyrics
void Song_Collection::sort_Songs_ByLyrics() {
    sort(songs.begin(), songs.end(), [](Song a, Song b) {
        return a.get_Lyrics().size() < b.get_Lyrics().size();
    });
}

vector<Song> Song_Collection::search(string word) {
    vector<Song> result;
    for (unsigned long i = 0; i < songs.size(); i++) {
        vector<string> lyrics = songs[i].get_Lyrics();
        for (unsigned long j = 0; j < lyrics.size(); j++) {
            if (lyrics[j].find(word) != string::npos) {
                result.push_back(songs[i]);
                break;
            }
        }
    }
    return result;
}
