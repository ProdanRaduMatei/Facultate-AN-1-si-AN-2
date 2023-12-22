#ifndef SONGCONTROLLERTEST_H
#define SONGCONTROLLERTEST_H

#include "SongController.h"
#include <cassert>

class SongControllerTest {
public:
    void runTests();

private:
    void testAddSong();
    void testSearchSong();
    void testGetFilesByArtist();
    void testGetFilesByTitle();
};

#endif
#pragma once
