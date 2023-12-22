#ifndef FILEREPOSITORY_H
#define FILEREPOSITORY_H

#include "Repository.h"
#include <fstream>


class FileRepository : public Repository {
public:
    FileRepository(const std::string& filepath);

    void load();
    void save();

private:
    std::string filepath = "songs.txt";
};

#endif
