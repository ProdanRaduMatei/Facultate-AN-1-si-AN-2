#pragma once
#include "Point.h"

#include "namespaceImgApp.h"
using namespace namespaceImgApp;

class namespaceImgApp::Rectangle
{
public:
	Rectangle();
	Rectangle(unsigned int x, unsigned int y, unsigned int width, unsigned int height);
	Rectangle(Point P1, Point P2);

	unsigned int getX() { return x; }
	unsigned int getY() { return y; }
	unsigned int getWidth() { return width; }
	unsigned int getHeight() { return height; }

private:
	unsigned int x;
	unsigned int y;
	unsigned int width;
	unsigned int height;
};

