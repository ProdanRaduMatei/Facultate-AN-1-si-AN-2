#pragma once
//#include "Image.h"

#include "namespaceImgApp.h"
using namespace namespaceImgApp;

class namespaceImgApp::Size// : public Image
{
public:
	Size();
	Size(unsigned int w, unsigned int h);

	unsigned int getWidth() const{ return m_width; }
	unsigned int getHeight() const{ return m_height; }

	friend bool operator==(const Size& S1, const Size& S2);
	friend bool operator!=(const Size& S1, const Size& S2);
	friend bool operator>(const Size& S1, const Size& S2);
	friend bool operator<(const Size& S1, const Size& S2);

private:
	unsigned int m_width;
	unsigned int m_height;
};
