#ifndef REPOSITORYTEST_H
#define REPOSITORYTEST_H

#include "Repository.h"
#include <cassert>

class RepositoryTest {
public:
    void runTests();

private:
    void testAddSong();
    void testFindSong();
    void testRemoveSong();
};

#endif
