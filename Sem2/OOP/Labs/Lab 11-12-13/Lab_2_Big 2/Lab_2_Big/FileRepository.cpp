#include "FileRepository.h"

FileRepository::FileRepository(const std::string& filepath) : Repository(), filepath(filepath) {}

void FileRepository::load() {
    std::ifstream inputFile(filepath);
    if (!inputFile.is_open()) {
        throw std::runtime_error("Cannot open the input file.");
    }

    std::vector<Song> loadedSongs; // Local vector to store the loaded songs

    // Read songs from the file and add them to the local vector
    std::string title, artist, line, url;
    std::vector<std::string> lyrics;
    int year = 2023;
    while (std::getline(inputFile, title) && std::getline(inputFile, artist)) {
        lyrics.clear();
        while (std::getline(inputFile, line) && !line.empty()) {
            lyrics.push_back(line);
        }
        Song song(title, artist, lyrics, year, url);
        loadedSongs.push_back(song);
    }

    inputFile.close();

    // Assign the local vector to the member variable songs using the accessor function
    const_cast<std::vector<Song>&>(getSongs()) = loadedSongs;
}


void FileRepository::save() {
    std::ofstream outputFile(filepath);
    if (!outputFile.is_open()) {
        throw std::runtime_error("Cannot save the songs to the file.");
    }

    const std::vector<Song>& songs = getSongs(); // Access the songs vector using the getSongs() accessor function
    for (const Song& song : songs) {
        outputFile << song.get_Title() << "\n";
        outputFile << song.get_Artist() << "\n";
        const std::vector<std::string>& lyrics = song.get_Lyrics();
        for (const std::string& line : lyrics) {
            outputFile << line << "\n";
        }
        outputFile << "\n";
    }

    outputFile.close();
}
