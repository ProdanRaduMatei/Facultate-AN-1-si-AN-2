#ifndef PLAYLIST_H
#define PLAYLIST_H

#include "Song.h"
#include <vector>


class Playlist
{
    private:
        std::vector<Song> songs;
public:
    Playlist();
    void addSong(const Song& song);
    void clearPlaylist();
    void removeSong(const Song& song);
    void generateRandomPlaylist(int n);
};

#endif // PLAYLIST_H
