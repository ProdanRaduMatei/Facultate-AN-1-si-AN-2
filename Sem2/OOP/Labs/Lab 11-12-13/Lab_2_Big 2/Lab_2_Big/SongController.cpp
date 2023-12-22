#include "SongController.h"
#include "SongException.h"
#include "Song.h"
#include "Action.h"
#include <algorithm>
#include <stack>
#include <exception>

SongController::SongController(Repository& repo) : repository(repo) {}


void SongController::addSong(const std::string& title, const std::string& artist, const std::vector<std::string>& lyrics, const std::string& url) {
    try {
        Song Song(title, artist, lyrics, 0, url);
        repository.addSong(Song);
    }
    catch (const SongException& exception) {
        throw exception;
    }
}

const Song& SongController::searchSong(const std::string& title, const std::string& artist) const {
    try {
        return repository.find(title, artist);
    }
    catch (const SongException& exception) {
        throw exception;
    }
}

std::vector<Song> SongController::getFilesByArtist(bool increasingOrder) const {
    std::vector<Song> songs = repository.getSongs();

    // Sort the songs vector by artist name using a lambda function
    std::sort(songs.begin(), songs.end(), [&](const Song& song1, const Song& song2) {
        if (increasingOrder) {
            return song1.get_Artist() < song2.get_Artist();
        }
        else {
            return song1.get_Artist() > song2.get_Artist();
        }
        });

    return songs;
}

std::vector<Song> SongController::getFilesByTitle(bool increasingOrder) const {
    std::vector<Song> songs = repository.getSongs();

    // Sort the songs vector by title using a lambda function
    std::sort(songs.begin(), songs.end(), [&](const Song& song1, const Song& song2) {
        if (increasingOrder) {
            return song1.get_Title() < song2.get_Title();
        }
        else {
            return song1.get_Title() > song2.get_Title();
        }
        });

    return songs;
}

void SongController::sortByArtist(bool ascending) {
    std::vector<Song> songs = repository.getSongs();

    // Sort the songs vector by artist name using a lambda function
    std::sort(songs.begin(), songs.end(), [&](const Song& song1, const Song& song2) {
        if (ascending) {
            return song1.get_Artist() < song2.get_Artist();
        }
        else {
            return song1.get_Artist() > song2.get_Artist();
        }
        });

    repository.setSongs(songs);
}

void SongController::sortByTitle(bool ascending) {
    std::vector<Song> songs = repository.getSongs();

    // Sort the songs vector by title using a lambda function
    std::sort(songs.begin(), songs.end(), [&](const Song& song1, const Song& song2) {
        if (ascending) {
            return song1.get_Title() < song2.get_Title();
        }
        else {
            return song1.get_Title() > song2.get_Title();
        }
        });

    repository.setSongs(songs);
}

// void SongController::addSong(const std::string& title, const std::string& artist, const std::vector<std::string>& lyrics, const std::string& url) {
//     try {
//         Song Song(title, artist, lyrics, 0, url);
//         repository.addSong(Song);
//     }
//     catch (const SongException& exception) {
//         throw exception;
//     }
// }

// const Song& SongController::searchSong(const std::string& title, const std::string& artist) const {
//     try {
//         return repository.find(title, artist);
//     }
//     catch (const SongException& exception) {
//         throw exception;
//     }
// }

// std::vector<Song> SongController::getFilesByArtist(bool increasingOrder) const {
//     std::vector<Song> songs = repository.getSongs();

//     // Sort the songs vector by artist name using a lambda function
//     std::sort(songs.begin(), songs.end(), [&](const Song& song1, const Song& song2) {
//         if (increasingOrder) {
//             return song1.get_Artist() < song2.get_Artist();
//         }
//         else {
//             return song1.get_Artist() > song2.get_Artist();
//         }
//         });

//     return songs;
// }

// std::vector<Song> SongController::getFilesByTitle(bool increasingOrder) const {
//     std::vector<Song> songs = repository.getSongs();

//     // Sort the songs vector by title using a lambda function
//     std::sort(songs.begin(), songs.end(), [&](const Song& song1, const Song& song2) {
//         if (increasingOrder) {
//             return song1.get_Title() < song2.get_Title();
//         }
//         else {
//             return song1.get_Title() > song2.get_Title();
//         }
//         });

//     return songs;
// }

// void SongController::sortByArtist(bool ascending) {
//     //how can i fix this vector?
//     std::vector<Song> songs = repository.getSongs();
//     if (ascending) {
//         std::sort(songs.begin(), songs.end(), [](const Song& song1, const Song& song2) {
//             return song1.get_Artist() < song2.get_Artist();
//             });
//     }
//     else {
//         std::sort(songs.begin(), songs.end(), [](const Song& song1, const Song& song2) {
//             return song1.get_Artist() > song2.get_Artist();
//             });
//     }
// }

/*Add two stacks as attributes in the SongController class: an undo stack and a redo stack.
When the user performs an action that can be undone (add or remove), push the current state of the application onto the undo stack.
If the user initiates an undo operation:
a. Pop the top state from the undo stack and push it onto the redo stack.
b. Apply the popped state to the application to restore the previous state.
If the user initiates a redo operation:
a. Pop the top state from the redo stack and push it onto the undo stack.
b. Apply the popped state to the application to restore the next state
The objects in these stacks will be pointers to Action objects. 
*/



void SongController::undo() {
    if (undoStack.empty()) {
        throw std::exception();
    }
    if (!undoStack.empty()) {
        Action* action = undoStack.top();
        undoStack.pop();
        action->apply(repository);
        redoStack.push(action);
    }
}

void SongController::redo() {
    if (redoStack.empty()) {
        throw std::exception();
    }
    if (!redoStack.empty()) {
        Action* action = redoStack.top();
        redoStack.pop();
        action->apply(repository);
        undoStack.push(action);
    }
}

// void SongController::addSong(const std::string& title, const std::string& artist, const std::vector<std::string>& lyrics, const std::string& url) {
//     try {
//         Song Song(title, artist, lyrics, 0, url);
//         repository.addSong(Song);
//         std::unique_ptr<Action> action = std::make_unique<AddAction>(repository, Song);
//         undoStack.push(std::move(action));
//         redoStack = std::stack<std::unique_ptr<Action>>();
//     }
//     catch (const SongException& exception) {
//         throw exception;
//     }
// }

// void SongController::removeSong(const std::string& title, const std::string& artist) {
//     try {
//         Song song = repository.find(title, artist);
//         repository.remove(song);
//         std::unique_ptr<Action> action = std::make_unique<RemoveAction>(repository, song);
//         undoStack.push(std::move(action));
//         redoStack = std::stack<std::unique_ptr<Action>>();
//     }
//     catch (const SongException& exception) {
//         throw exception;
//     }
// }

// void SongController::updateSong(const std::string& title, const std::string& artist, const std::vector<std::string>& lyrics, const std::string& url) {
//     try {
//         Song song(title, artist, lyrics, 0, url);
//         Song oldSong = repository.find(title, artist);
//         repository.update(song);
//         std::unique_ptr<Action> action = std::make_unique<UpdateAction>(repository, oldSong, song);
//         undoStack.push(std::move(action));
//         redoStack = std::stack<std::unique_ptr<Action>>();
//     }
//     catch (const SongException& exception) {
//         throw exception;
//     }
// }

// void SongController::saveSong(const std::string& title, const std::string& artist) {
//     try {
//         Song song = repository.find(title, artist);
//         repository.saveSong(song);
//     }
//     catch (const SongException& exception) {
//         throw exception;
//     }
// }

// void SongController::nextSong() {
//     try {
//         Song song = repository.nextSong();
//         repository.saveSong(song);
//     }
//     catch (const SongException& exception) {
//         throw exception;
//     }
// }

// void SongController::savePlaylist(const std::string& filename) {
//     try {
//         repository.savePlaylist(filename);
//     }
//     catch (const SongException& exception) {
//         throw exception;
//     }
// }

// void SongController::openPlaylist(const std::string& filename) {
//     try {
//         repository.openPlaylist(filename);
//     }
//     catch (const SongException& exception) {
//         throw exception;
//     }
// }

// std::vector<Song> SongController::getPlaylist() const {
//     return repository.getPlaylist();
// }

// void SongController::setPlaylist(const std::vector<Song>& songs) {
//     repository.setPlaylist(songs);
// }

// void SongController::setPlaylistIndex(int index) {
//     repository.setPlaylistIndex(index);
// }

// int SongController::getPlaylistIndex() const {
//     return repository.getPlaylistIndex();
// }

// void SongController::setPlaylistMode(bool mode) {
//     repository.setPlaylistMode(mode);
// }

