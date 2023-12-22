#pragma once
#include "Shape.h"
#include <string>

struct Point {
	float x;
	float y;
};
class Square : public Shape
{
public:
	Square(float x, float y, float side);
	~Square();
	Square(const Square& other);
	Square& operator=(const Square& other);
	float area() override;
	std::string toString();
private:
	float m_side;
	Point* m_vertices;
};


