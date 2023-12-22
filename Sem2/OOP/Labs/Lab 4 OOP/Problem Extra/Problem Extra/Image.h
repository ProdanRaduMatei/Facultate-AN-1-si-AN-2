#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstring>

class Point {
public:
    int x;
    int y;
    Point(int x, int y): x(x), y(y) {}
};

class Image {
private:
    int* pixels;
    int width;
    int height;
    
public:
    // Constructors and Destructor
    Image();
    Image(int width, int height);
    Image(const Image& other);
    ~Image();
    
    // Copy assignment operator
    Image& operator=(const Image& other);
    
    // Getters
    int getWidth() const;
    int getHeight() const;
    std::string getSize();
    
    // Load and Save
    bool loadFromFile(const std::string& filename);
    bool saveToFile(const std::string& filename) const;
    
    // Operators
    friend std::ostream& operator<<(std::ostream& os, const Image& image);
    Image operator+(const Image& other) const;
    Image operator-(const Image& other) const;
    
    Image operator*(const Image& other) const;
    
    Image operator+(int scalar) const;
    
    Image operator-(int scalar) const;
    
    Image operator*(int scalar) const;
    
    bool isEmpty() const;
    
    // Method to get a reference to a pixel in the image
    int& operator()(int x, int y);
    
    int& operator()(const Point& p);
    
    // Method to get a pointer to a row in the image
    int* getRow(int y);
    
    // Method to release the memory allocated for the image
    void release();
    
    // Method to get a new image containing a region of interest
    Image getROI(int x, int y, int w, int h) const;
    
    // Static methods
    static Image zeros(int w, int h);
    
    static Image ones(int w, int h);
    
    int pixel(int x, int y) const;
    
    void setPixel(int x, int y, int value);
};
