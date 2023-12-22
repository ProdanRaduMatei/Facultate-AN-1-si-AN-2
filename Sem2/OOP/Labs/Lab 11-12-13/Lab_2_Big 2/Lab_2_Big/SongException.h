#ifndef SONGEXCEPTION_H
#define SONGEXCEPTION_H

#include <exception>
#include <string>

class SongException : public std::exception {
public:
    SongException(const std::string& description);

    const char* what() const noexcept override;

private:
    std::string description;
};

#endif
