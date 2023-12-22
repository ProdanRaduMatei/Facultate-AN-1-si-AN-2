#include "Point.h"
#include <iostream>
// Implementation of Point class

// Constructors
Point::Point() : x(0), y(0) {}
Point::Point(int x, int y) : x(x), y(y) {}

// Overload stream insertion and extraction operators
std::ostream& operator<<(std::ostream& os, const Point& point) {
    os << "(" << point.x << ", " << point.y << ")";
    return os;
}

std::istream& operator>>(std::istream& is, Point& point) {
    is >> point.x >> point.y;
    return is;
}

// Getters and Setters
int Point::getX() const {
    return x;
}

int Point::getY() const {
    return y;
}

void Point::setX(int x) {
    x = x;
}

void Point::setY(int y) {
    y = y;
}
