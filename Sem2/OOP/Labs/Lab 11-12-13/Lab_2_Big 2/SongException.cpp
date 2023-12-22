#include "SongException.h"

SongException::SongException(const std::string& description) : description(description) {}

const char* SongException::what() const noexcept {
    return description.c_str();
}
