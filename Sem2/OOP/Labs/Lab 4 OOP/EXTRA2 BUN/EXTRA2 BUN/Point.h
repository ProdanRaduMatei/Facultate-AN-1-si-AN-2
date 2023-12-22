#pragma once
#include <iostream>

#include "namespaceImgApp.h"
using namespace namespaceImgApp;

class namespaceImgApp::Point
{
public:
	Point();
	Point(unsigned int x, unsigned int y);

	unsigned int getX() const { return x; }
	unsigned int getY() const { return y; }
	void setX(unsigned int newX) { x = newX; }
	void setY(unsigned int newY) { y = newY; }

	friend std::ostream& operator<<(std::ostream& os, const Point& P);
	friend std::istream& operator>>(std::istream& os, Point& P);

private:
	unsigned int x;
	unsigned int y;
};

