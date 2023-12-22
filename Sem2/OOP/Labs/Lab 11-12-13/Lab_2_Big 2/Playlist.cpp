#include "Playlist.h"
#include <algorithm>
#include <random>

std::random_device rd;
std::mt19937 g(rd());

Playlist::Playlist()
{
}

void Playlist::addSong(const Song& song)
{
    this->songs.push_back(song);
}

void Playlist::clearPlaylist()
{
    this->songs.clear();
}

void Playlist::removeSong(const Song& song)
{
    this->songs.erase(std::remove(this->songs.begin(), this->songs.end(), song), this->songs.end());
}

void Playlist::generateRandomPlaylist(int n)
{
    std::vector<Song> songs = this->songs;
    this->clearPlaylist();
    std::shuffle(songs.begin(), songs.end(), g);
    for (int i = 0; i < n; i++)
        this->addSong(songs[i]);
}
