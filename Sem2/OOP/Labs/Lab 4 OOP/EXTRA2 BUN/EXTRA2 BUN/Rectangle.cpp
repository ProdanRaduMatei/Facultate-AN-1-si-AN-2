#include "Rectangle.h"
#include <cmath>

Rectangle::Rectangle()
{
	this->x = 0;
	this->y = 0;
	this->height = 0;
	this->width = 0;
}

Rectangle::Rectangle(unsigned int x, unsigned int y, unsigned int width, unsigned int height)
{
	this->x = x;
	this->y = y;
	this->height = height;
	this->width = width;
}

unsigned int min(unsigned int x, unsigned int y) {
	if (x < y)
		return x;
	return y;
}
unsigned int max(unsigned int x, unsigned int y) {
	if (x > y)
		return x;
	return y;
}

Rectangle::Rectangle(Point P1, Point P2)
{
	unsigned int x, y, width, height;

	x = min(P1.getX(), P2.getX());
	y = max(P1.getY(), P2.getY());

	height = max(P1.getY(), P2.getY()) - min(P1.getY(), P2.getY());
	width = max(P1.getX(), P2.getX()) - min(P1.getX(), P2.getX());

	this->x = x;
	this->y = y;
	this->height = height;
	this->width = width;
}
