#include "Rectangle.h"
#include "Point.h"
#include <iostream>
// Implementation of Rectangle class

// Constructors
Rectangle::Rectangle() : x_(0), y_(0), width_(0), height_(0) {}
Rectangle::Rectangle(int x, int y, int width, int height) : x_(x), y_(y), width_(width), height_(height) {}
Rectangle::Rectangle(const Point& tl, const Point& br) : x_(tl.getX()), y_(tl.getY()), width_(br.getX() - tl.getX()), height_(br.getY() - tl.getY()) {}

// Overload stream insertion and extraction operators
std::ostream& operator<<(std::ostream& os, const Rectangle& rect) {
    os << "Top-Left Point: " << rect.x_ << ", " << rect.y_ << ", Width: " << rect.width_ << ", Height: " << rect.height_;
    return os;
}

std::istream& operator>>(std::istream& is, Rectangle& rect) {
    is >> rect.x_ >> rect.y_ >> rect.width_ >> rect.height_;
    return is;
}

// Overload addition and subtraction operators for translation
Rectangle Rectangle::operator+(const Point& point) const {
    return Rectangle(x_ + point.getX(), y_ + point.getY(), width_, height_);
}

Rectangle Rectangle::operator-(const Point& point) const {
    return Rectangle(x_ - point.getX(), y_ - point.getY(), width_, height_);
}

Rectangle& Rectangle::operator+=(const Point& point) {
    x_ += point.getX();
    y_ += point.getY();
    return *this;
}

Rectangle& Rectangle::operator-=(const Point& point) {
    x_ -= point.getX();
    y_ -= point.getY();
    return *this;
}

// Overload bitwise AND and OR operators for intersection and union
Rectangle Rectangle::operator&(const Rectangle& rect) const {
    int x1 = std::max(x_, rect.x_);
    int y1 = std::max(y_, rect.y_);
    int x2 = std::min(x_ + width_, rect.x_ + rect.width_);
    int y2 = std::min(y_ + height_, rect.y_ + rect.height_);
    if (x2 < x1 || y2 < y1) {
        return Rectangle(); // Empty rectangle
    }
    return Rectangle(x1, y1, x2 - x1, y2 - y1);
}

Rectangle Rectangle::operator|(const Rectangle& rect) const {
    int x1 = std::min(x_, rect.x_);
    int y1 = std::min(y_, rect.y_);
    int x2 = std::max(x_ + width_, rect.x_ + rect.width_);
    int y2 = std::max(y_ + height_, rect.y_ + rect.height_);
    return Rectangle(x1, y1, x2 - x1, y2 - y1);
}

// Getters and Setters
int Rectangle::getX() const {
    return x_;
}

int Rectangle::getY() const {
    return y_;
}

int Rectangle::getWidth() const {
    return width_;
}

int Rectangle::getHeight() const {
    return height_;
}

void Rectangle::setX(int x) {
    x_ = x;
}

void Rectangle::setY(int y) {
    y_ = y;
}

void Rectangle::setWidth(int width) {
    width_ = width;
}

void Rectangle::setHeight(int height) {
    height_ = height;
}
