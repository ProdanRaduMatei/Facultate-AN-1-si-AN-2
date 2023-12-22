#pragma once
#include <string>
#include <iostream>
#include <vector>

class Song {
private:
    std::string title;
    std::string artist;
    std::vector<std::string> lyrics;
    int year;
    std::string url;

public:
    Song(std::string _title, std::string _artist, std::vector<std::string> _lyrics, int _year, const std::string& _url);
    std::string get_Title() const;
    std::string get_Artist() const;
    std::vector<std::string> get_Lyrics() const;
    int get_Year() const;
    std::string get_URL() const;
    void set_Title(std::string _title);
    void set_Artist(std::string _artist);
    void set_Lyrics(std::vector<std::string> _lyrics);
    void set_Year(int _year);
    void set_URL(std::string _url);
    void display() const;
    bool operator==(const Song& other) const;
};
