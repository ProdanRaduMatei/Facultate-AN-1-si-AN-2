#pragma once
#include <string>
class Shape {
public:
	Shape(float x, float y);
	Shape(int x, int y, int r);
	virtual ~Shape() = default;
	virtual float area();
	virtual std::string toString();
protected:
	float m_x, m_y;
};

