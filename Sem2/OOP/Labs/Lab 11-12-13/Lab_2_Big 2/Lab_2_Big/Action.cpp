#include <iostream>
#include <string>
#include <vector>

#include "Song.h"
#include "SongException.h"
#include "Repository.h"
#include "Action.h"

using namespace std;

ActionAdd::ActionAdd(Repository& repo, Song song) : repo{ repo }, song{ song } {}
void ActionAdd::apply(Repository& repo) {
    repo.addSong(song);
}

ActionDelete::ActionDelete(Repository& repo, Song song) : repo{ repo }, song{ song } {}
void ActionDelete::apply(Repository& repo) {
    repo.remove(song);
}


