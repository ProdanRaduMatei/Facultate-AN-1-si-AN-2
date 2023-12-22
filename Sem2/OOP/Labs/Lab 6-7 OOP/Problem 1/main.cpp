//main.cpp
#include <iostream>
#include <memory>
#include <string>
#include "Shape.h"
#include "Circle.h"
#include "Square.h"

void exercise1() {
	// 1. create a polymorphic static array shapes with 6 elements that holds c1, c2, c3 and s1, s2 and s3
	Circle c1(10, 10, 1);
	Shape *c2(new Circle(0, 0, 100));
	Circle c3(-10, 0, 2);

	Shape *s1(new Square(0, 0, 2));
	Square s2(10, 20, 17);
	Square s3(9, 100, 0.3);

	Shape* shapes[6] = { &c1, c2, &c3, s1, &s2, &s3 };

	// 2. display all the elements that have an area greater than 10
	for (int i = 0; i < 6; ++i)
		if (shapes[i]->area() > 10)
			std::cout << shapes[i]->toString() << std::endl;
	
	std::cout << std::endl;

	// 3. display all the circles from the array shapes
	for (int i = 0; i < 6; ++i) {
		Circle* x = dynamic_cast<Circle*>(shapes[i]);
		if (x != nullptr)
			std::cout << x->toString() << std::endl;
	}

	delete s1;
	delete c2;
	s1 = nullptr;
	c2 = nullptr;
}

int main() {
	exercise1();
	return 0;
}
