#include "Point.h"

Point::Point()
{
	this->x = 0;
	this->y = 0;
}

Point::Point(unsigned int x, unsigned int y)
{
	this->x = x;
	this->y = y;
}

std::ostream& operator<<(std::ostream& os, const Point& P)
{
	os << "(" << P.getX() << "," << P.getY() << ")";
	return os;
}

std::istream& operator>>(std::istream& is, Point& P)
{
	unsigned int x, y;
	is >> x >> y;
	P.setX(x);
	P.setY(y);
	return is;
}
