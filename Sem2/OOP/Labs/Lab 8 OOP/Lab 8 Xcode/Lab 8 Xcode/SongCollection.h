#pragma once
#include <string>
#include <iostream>
#include <vector>
#include "Song.h"
using namespace std;

class SongCollection {
    private:
        vector<Song> songs;

    public:
        SongCollection();

        void addSong(Song song);

        void print();
       
        void loadFromFile(string filename);

        int uniqueArtists();

        void printTop10Artists();

        void sortSongsByArtist();
        void sortSongsByTitle();
        void sortSongsByLyrics();

        vector<Song> search(string word);
};