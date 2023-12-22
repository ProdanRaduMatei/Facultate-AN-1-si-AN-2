#ifndef FILEREPOSITORYTEST_H
#define FILEREPOSITORYTEST_H

#include "FileRepository.h"
#include <cassert>

class FileRepositoryTest {
public:
    void runTests();

private:
    void testLoadSongs();
    void testSaveSongs();
};

#endif
