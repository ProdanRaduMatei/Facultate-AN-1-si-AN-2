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

SongCollection::SongCollection() {
    songs = vector<Song>();
}

void SongCollection::addSong(Song song) {
    songs.push_back(song);
}

void SongCollection::print() {
    for (int i = 0; i < songs.size(); i++) {
        songs[i].display();
    }
}

void SongCollection::loadFromFile(string filename) {
    ifstream file(filename);
    if (!file.is_open()) {
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
            Song song(artist, title, lyrics);
            addSong(song);
            lyrics.clear();
        }
    }
}

int SongCollection::uniqueArtists() {
    vector<string> artists;
    for (int i = 0; i < songs.size(); i++) {
        bool found = false;
        for (int j = 0; j < artists.size(); j++) {
            if (songs[i].getArtist() == artists[j]) {
                found = true;
                break;
            }
        }
        if (!found) {
            artists.push_back(songs[i].getArtist());
        }
    }
    return artists.size();
}

void SongCollection::printTop10Artists() {
    map<string, int> artistCounts;
    for (int i = 0; i < songs.size(); i++) {
        string artist = songs[i].getArtist();
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

void SongCollection::sortSongsByArtist() {
    sort(songs.begin(), songs.end(), [](Song a, Song b) {
        return a.getArtist() < b.getArtist();
    });
}

void SongCollection::sortSongsByTitle() {
    sort(songs.begin(), songs.end(), [](Song a, Song b) {
        return a.getTitle() < b.getTitle();
    });
}

void SongCollection::sortSongsByLyrics() {
    sort(songs.begin(), songs.end(), [](Song a, Song b) {
        return a.getLyrics().size() < b.getLyrics().size();
    });
}

vector<Song> SongCollection::search(string word) {
    vector<Song> result;
    for (int i = 0; i < songs.size(); i++) {
        vector<string> lyrics = songs[i].getLyrics();
        for (int j = 0; j < lyrics.size(); j++) {
            if (lyrics[j].find(word) != string::npos) {
                result.push_back(songs[i]);
                break;
            }
        }
    }
    return result;
}