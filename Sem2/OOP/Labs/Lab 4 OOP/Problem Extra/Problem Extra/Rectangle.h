#include "Point.h"
#include <iostream>

class Rectangle {
public:
    // Constructors
    Rectangle();
    Rectangle(int x, int y, int width, int height);
    Rectangle(const Point& tl, const Point& br);

    // Overload stream insertion and extraction operators
    friend std::ostream& operator<<(std::ostream& os, const Rectangle& rect);
    friend std::istream& operator>>(std::istream& is, Rectangle& rect);

    // Overload addition and subtraction operators for translation
    Rectangle operator+(const Point& point) const;
    Rectangle operator-(const Point& point) const;
    Rectangle& operator+=(const Point& point);
    Rectangle& operator-=(const Point& point);

    // Overload bitwise AND and OR operators for intersection and union
    Rectangle operator&(const Rectangle& rect) const;
    Rectangle operator|(const Rectangle& rect) const;

    // Getters and Setters
    int getX() const;
    int getY() const;
    int getWidth() const;
    int getHeight() const;
    void setX(int x);
    void setY(int y);
    void setWidth(int width);
    void setHeight(int height);

private:
    int x_; // X-coordinate of the top-left point
    int y_; // Y-coordinate of the top-left point
    int width_; // Width of the rectangle
    int height_; // Height of the rectangle
};
