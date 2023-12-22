#ifndef SONGCONTROLLER_H
#define SONGCONTROLLER_H

#include "Repository.h"
#include "SongException.h"
#include "Song.h"
#include "Action.h"
#include <algorithm>
#include <stack>

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


class SongController {
private:
    Repository& repository;
    std::stack<Action*> undoStack;
    std::stack<Action*> redoStack;

public:
    SongController(Repository& repo);

    void addSong(const std::string& title, const std::string& artist, const std::vector<std::string>& lyrics = {}, const std::string& url = "");
    const Song& searchSong(const std::string& title, const std::string& artist) const;
    std::vector<Song> getFilesByArtist(bool increasingOrder = true) const;
    std::vector<Song> getFilesByTitle(bool increasingOrder = true) const;
    void sortByArtist(bool ascending);
    void sortByTitle(bool ascending);
    void removeSong(const std::string& title, const std::string& artist);
    void updateSong(const std::string& title, const std::string& artist, const std::vector<std::string>& lyrics, const std::string& url);
    void undo();
    void redo();
};

#endif
