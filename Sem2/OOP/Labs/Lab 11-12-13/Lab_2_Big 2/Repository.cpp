#include "Repository.h"
#include "SongException.h"

Repository::Repository() {}

//Create a function void store(const Song& s) that will store the song passed as a parameter. If a song with that tile and artist already exists, throw a SongException exception with the text “A song <song_title> by <song_artist> already exists”. 
void Repository::store(const Song& song) {
    auto it = std::find(songs.begin(), songs.end(), song);

    if (it != songs.end()) {
        std::string errorMessage = "The song " + song.get_Title() + " by " + song.get_Artist() + " already exists.";
        throw SongException(errorMessage);
    }

    songs.push_back(song);
}

//Create a function const Song& find(std::string title, std::string artist) that searches for the song with the title title by the artist artist. If no such song exists, throw a SongException exception with the text “The song <song_title> by <song_artist> does not exist”. Don’t explicitly iterate through the container, instead use a function from <algorithm> and a lambda.
const Song& Repository::find(std::string& title, std::string& artist) const {
    auto it = std::find_if(songs.begin(), songs.end(), [&](const Song& song) {
        return (song.get_Title() == title && song.get_Artist() == artist);
    });

    if (it == songs.end()) {
        std::string errorMessage = "The song " + title + " by " + artist + " does not exist.";
        throw SongException(errorMessage);
    }

    return *it;
}

void Repository::addSong(const Song& song) {
    songs.push_back(song);
}

const Song& Repository::find(const std::string& title, const std::string& artist) const {
    auto it = std::find_if(songs.begin(), songs.end(), [&](const Song& song) {
        return (song.get_Title() == title && song.get_Artist() == artist);
    });

    if (it == songs.end()) {
        std::string errorMessage = "The song " + title + " by " + artist + " does not exist.";
        throw SongException(errorMessage);
    }

    return *it;
}

//Create a function void remove(const Song& s) that removes the song passed as a parameter. If no such song exists, throw a SongException exception with the text “The song <song_title> by <song_artist> does not exist”.
//Use a function from <vector> to remove the Song, don’t explicitly implement the removal.
void Repository::remove(const Song& song) {
    auto it = std::find(songs.begin(), songs.end(), song);

    if (it != songs.end()) {
        songs.erase(it);
    }
    else {
        std::string errorMessage = "The song " + song.get_Title() + " by " + song.get_Artist() + " does not exist.";
        throw SongException(errorMessage);
    }
}

const std::vector<Song>& Repository::getSongs() const {
    return songs;
}

int Repository::setSongs(const std::vector<Song>& newSongs) {
    songs = newSongs;
    return 0;
}

void Repository::update(const Song& song) {
    auto it = std::find(songs.begin(), songs.end(), song);

    if (it != songs.end()) {
        *it = song;
    }
    else {
        std::string errorMessage = "The song " + song.get_Title() + " by " + song.get_Artist() + " does not exist.";
        throw SongException(errorMessage);
    }
}