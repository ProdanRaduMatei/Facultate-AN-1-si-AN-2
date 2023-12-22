#include <iostream>

class Point {
public:
    // Constructors
    Point();
    Point(int x, int y);

    // Overload stream insertion and extraction operators
    friend std::ostream& operator<<(std::ostream& os, const Point& point);
    friend std::istream& operator>>(std::istream& is, Point& point);

    // Getters and Setters
    int getX() const;
    int getY() const;
    void setX(int x);
    void setY(int y);

private:
    int x; // X-coordinate of the point
    int y; // Y-coordinate of the point
};
