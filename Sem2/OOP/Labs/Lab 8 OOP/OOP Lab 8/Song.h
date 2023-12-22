#pragma once
#include <string>
#include <iostream>
#include <vector>
using namespace std;

class Song {
private:
    string title;
    string artist;
    vector <string> lyrics;

public:
    Song(string _title, string _artist, vector <string> _lyrics);
    string getTitle() const;
    string getArtist() const;
    vector <string> getLyrics() const;
    void setTitle(string _title);
    void setArtist(string _artist);
    void setLyrics(vector <string> _lyrics);
    void display() const;
};
