#ifndef REPOSITORY_H
#define REPOSITORY_H

#include "Song.h"
#include "SongException.h"
#include <vector>
#include <algorithm>

class Repository {
private:
    std::vector<Song> songs;

public:
    Repository();

    void store(const Song& song);
    const Song& find(std::string& title, std::string& artist) const;
    void addSong(const Song& song);
    const Song& find(const std::string& title, const std::string& artist) const;
    void remove(const Song& song);
    const std::vector<Song>& getSongs() const;
    int setSongs(const std::vector<Song>& newSongs);
    void update(const Song& song);
};

#endif
