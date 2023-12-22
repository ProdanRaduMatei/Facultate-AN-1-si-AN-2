#pragma once
#include "Repository.h"
#include "Song.h"


class Action {
public:
    virtual void apply(Repository& repo) = 0;
};


class ActionAdd : public Action {
private:
    Repository& repo;
    Song song;
public:
    ActionAdd(Repository& repo, Song song);
    void apply(Repository& repo) override;
};

class ActionDelete : public Action {
private:
    Repository& repo;
    Song song;
public:
    ActionDelete(Repository& repo, Song song);
    void apply(Repository& repo) override;
};
