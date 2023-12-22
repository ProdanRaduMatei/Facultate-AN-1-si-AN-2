#ifndef SONGACTION_H
#define SONGACTION_H

#include <QString>

enum class ActionType {
    Add,
    Remove,
    SortByTitle,
    SortByArtist
};

struct SongAction {
    ActionType type;
    QString title;
    QString artist; // Add the artist member
};

#endif // SONGACTION_H
