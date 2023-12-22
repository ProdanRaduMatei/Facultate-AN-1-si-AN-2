#include "drawingModule.h"
#include <cmath>
#include <iostream>
#include "Rectangle.h"

#include "namespaceImgApp.h"
using namespace namespaceImgApp;

float distance(Point P1, Point P2) {
	return sqrtf((P2.getX() - P1.getX()) * (P2.getX() - P1.getX()) + (P2.getY() - P1.getY()) * (P2.getY() - P1.getY()));
}

void drawCircle(Image& img, Point center, int radius, unsigned int color)
{
	for (int i = 0; i < img.height(); i ++) {
		for (int j = 0; j < img.width(); j++) {
			Point P(j,i);
			float d = distance(center, P);//compute distance
			if(radius-1 <= d && d <= radius+1)//if d is from the interval [radius-1,radius+1]
				img.setPixelVal(j, i, color);
		}
	}
}

void drawLine(Image& img, Point p1, Point p2, unsigned int color)///INCOMPLETE
{
	for (int i = 0; i < img.height(); i++) {
		for (int j = 0; j < img.width(); j++) {
			int equation = j * p1.getY() + p1.getX() * p2.getY() + i * p2.getX() - p2.getX()*p1.getY() - j*p2.getY() - i*p1.getX();
			if((-70 <= equation && equation <= 70) && ( (p1.getX() <= j && j <= p2.getX() && p1.getY() <= i && i <= p2.getY()) || (p2.getX() <= j && j <= p1.getX() && p2.getY() <= i && i <= p1.getY())))
				img.setPixelVal(j, i, color);
		}
	}
}

void drawRectangle(Image& img, Rectangle r, unsigned int color)
{
	unsigned int limitY = r.getY() + r.getHeight();
	unsigned int limitX = r.getX() + r.getWidth();

	unsigned int x = r.getX(), y = r.getY();

	while (x < limitX) {//top vertex
		img.setPixelVal(x,y,color);
		x++;
	}
	while (y < limitY) {//right vertex
		img.setPixelVal(x, y, color);
		y++;
	}
	while (x > r.getX()) {//bottom vertex
		img.setPixelVal(x, y, color);
		x--;
	}
	while (y > r.getY()) {//left vertex
		img.setPixelVal(x, y, color);
		y--;
	}
}

void drawRectangle(Image& img, Point p1, Point p2, unsigned int color)
{
	Rectangle r(p1, p2);
	drawRectangle(img, r, color);
}


