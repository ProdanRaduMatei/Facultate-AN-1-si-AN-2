#include "Song.h"
#include <iostream>

Song::Song(std::string _title, std::string _artist, std::vector<std::string> _lyrics, int _year, const std::string& _url)
    : title(_title), artist(_artist), lyrics(_lyrics), year(_year), url(_url) {}

std::string Song::get_Title() const {
    return title;
}

std::string Song::get_Artist() const {
    return artist;
}

std::vector<std::string> Song::get_Lyrics() const {
    return lyrics;
}

int Song::get_Year() const {
    return year;
}

std::string Song::get_URL() const {
    return url;
}

void Song::set_Title(std::string _title) {
    title = _title;
}

void Song::set_Artist(std::string _artist) {
    artist = _artist;
}

void Song::set_Lyrics(std::vector<std::string> _lyrics) {
    lyrics = _lyrics;
}

void Song::set_Year(int _year) {
    year = _year;
}

void Song::set_URL(std::string _url) {
    url = _url;
}

void Song::display() const {
    std::cout << "Title: " << title << std::endl;
    std::cout << "Artist: " << artist << std::endl;
    std::cout << "Lyrics:" << std::endl;
    for (const auto& line : lyrics) {
        std::cout << line << std::endl;
    }
}

bool Song::operator==(const Song& other) const {
    return (this->artist == other.artist && this->title == other.title && this->lyrics == other.lyrics);
}
