#pragma once
#include <string>
#include <iostream>
#include <vector>
#include "Song.h"
using namespace std;

class Song_Collection {
    private:
        vector<Song> songs;
        std::string filepath = "songs.txt";

    public:
        Song_Collection();

        void add_Song(Song song);

        void print();
       
        void load_From_File(string filepath);

        int unique_Artists();

        void Top_10_Artists();

        void sort_Songs_By_Artist();
        void sort_Songs_By_Title();
        void sort_Songs_ByLyrics();

        vector<Song> search(string word);
};