#include "ImageProcessing.h"
#include "Image.h"
#include <exception>
#include <cmath>


#include <iostream>
using namespace std;

void ImageProcessing::process(const Image& src, Image& dst){}

Adjustment::Adjustment()
{
	this->contrast = 1;
	this->brightness = 0;
}

void Adjustment::setContrast(float c)
{
	this->contrast = c;
}

void Adjustment::setBrightness(int b)
{
	this->brightness = b;
}

void Adjustment::process(const Image& src, Image& dst)
{
	for (int i = 0; i < src.height(); i++)
		for (int j = 0; j < src.width(); j++)
			dst.setPixelVal(j, i, this->contrast * src.getPixelVal(j, i) + this->brightness);
}

Gamma::Gamma()
{
	this->tita = 1;
}

void Gamma::setTita(float t)
{
	this->tita = t;
}

void Gamma::process(const Image& src, Image& dst)
{
	for (int i = 0; i < src.height(); i++)
		for (int j = 0; j < src.width(); j++)
			dst.setPixelVal(j, i,pow(src.getPixelVal(j, i),this->tita));
}

int movX[9] = { -1,-1,-1,0,0,0,1,1,1 };
int movY[9] = { -1,0,1,-1,0,1,-1,0,1 };

void Convolution::setOperation(unsigned int x) {
	/*
	* 1 - Blur
	* 2 - Gaussian blur
	* 3 - Horizontal Sobel
	* 4 - Vertical Sobel
	* anything else - Identity
	*/
	this->operation = x;
}

int Convolution::rangeSobelConverter(int x)
{
	x += 4 * 255;
	return x / 8;
}

int Convolution::conSumIdentity(const Image& src, unsigned int x, unsigned int y) {
	int sum = 0, i2 = 0, j2 = 0;
	for (int i = 0; i < 9; i++) {
		if (j2 == 3) {
			j2 = 0;
			i2++;
		}
		if (x + movX[i] >= 0 && y + movY[i] >= 0 && (x + movX[i] < src.width()) && (y + movY[i] < src.height()))
			sum += src.getPixelVal(x + movX[i], y + movY[i]) * kernel[i2][j2];
		j2++;
	}
	return sum;
}

int Convolution::conSumBlur(const Image& src, unsigned int x, unsigned int y) {
	int sum = 0, i2 = 0, j2 = 0;
	for (int i = 0; i < 9; i++) {
		if (j2 == 3) {
			j2 = 0;
			i2++;
		}
		if (x + movX[i] >= 0 && y + movY[i] >= 0 && (x + movX[i] < src.width()) && (y + movY[i] < src.height()))
			sum += src.getPixelVal(x + movX[i], y + movY[i]) * kernel[i2][j2];
		j2++;
	}
	return sum/9;
}

int Convolution::conSumGaussian(const Image& src, unsigned int x, unsigned int y) {
	int sum = 0, i2 = 0, j2 = 0;
	for (int i = 0; i < 9; i++) {
		if (j2 == 3) {
			j2 = 0;
			i2++;
		}
		if (x + movX[i] >= 0 && y + movY[i] >= 0 && (x + movX[i] < src.width()) && (y + movY[i] < src.height()))
			sum += src.getPixelVal(x + movX[i], y + movY[i]) * kernel[i2][j2];
		j2++;
	}
	return sum / 16;
}

int Convolution::conSumHorizontalSobel(const Image& src, unsigned int x, unsigned int y) {
	int sum = 0, i2 = 0, j2 = 0;
	for (int i = 0; i < 9; i++) {
		if (j2 == 3) {
			j2 = 0;
			i2++;
		}
		if (x + movX[i] >= 0 && y + movY[i] >= 0 && (x + movX[i] < src.width()) && (y + movY[i] < src.height()))
			sum += src.getPixelVal(x + movX[i], y + movY[i]) * kernel[i2][j2];
		j2++;
	}
	return rangeSobelConverter(sum);
}

int Convolution::conSumVerticalSobel(const Image& src, unsigned int x, unsigned int y) {
	int sum = 0, i2 = 0, j2 = 0;
	for (int i = 0; i < 9; i++) {
		if (j2 == 3) {
			j2 = 0;
			i2++;
		}
		if (x + movX[i] >= 0 && y + movY[i] >= 0 && (x + movX[i] < src.width()) && (y + movY[i] < src.height()))
			sum += src.getPixelVal(x + movX[i], y + movY[i]) * kernel[i2][j2];
		j2++;
	}
	return rangeSobelConverter(sum);
}

void Convolution::process(const Image& src, Image& dst) {
	if (this->operation == 1) {
		kernel[0][0] = 1; kernel[0][1] = 1; kernel[0][2] = 1;
		kernel[1][0] = 1; kernel[1][1] = 1; kernel[1][2] = 1;
		kernel[2][0] = 1; kernel[2][1] = 1; kernel[2][2] = 1;

		for (int y = 0; y < dst.height(); y++) {
			for (int x = 0; x < dst.width(); x++) {
				dst.setPixelVal(x, y, this->conSumBlur(src, x, y));
			}
		}
		//blur
	}
	else if (this->operation == 2) {
		kernel[0][0] = 1; kernel[0][1] = 2; kernel[0][2] = 1;
		kernel[1][0] = 2; kernel[1][1] = 4; kernel[1][2] = 2;
		kernel[2][0] = 1; kernel[2][1] = 2; kernel[2][2] = 1;

		for (int y = 0; y < dst.height(); y++) {
			for (int x = 0; x < dst.width(); x++) {
				dst.setPixelVal(x, y, conSumGaussian(src, x, y));
			}
		}
		//gaussian
	}
	else if (this->operation == 3) {
		kernel[0][0] = 1; kernel[0][1] = 2; kernel[0][2] = 1;
		kernel[1][0] = 0; kernel[1][1] = 0; kernel[1][2] = 0;
		kernel[2][0] = -1; kernel[2][1] = -2; kernel[2][2] = -1;

		for (int y = 0; y < dst.height(); y++) {
			for (int x = 0; x < dst.width(); x++) {
				dst.setPixelVal(x, y, this->conSumHorizontalSobel(src, x, y));
			}
		}
		//horizontal
	}
	else if (this->operation == 4) {
		kernel[0][0] = -1; kernel[0][1] = 0; kernel[0][2] = 1;
		kernel[1][0] = -2; kernel[1][1] = 0; kernel[1][2] = 2;
		kernel[2][0] = -1; kernel[2][1] = 0; kernel[2][2] = 1;

		for (int y = 0; y < dst.height(); y++) {
			for (int x = 0; x < dst.width(); x++) {
				dst.setPixelVal(x, y, this->conSumVerticalSobel(src, x, y));
			}
		}
		//vertical
	}
	else
	{
		kernel[0][0] = 0; kernel[0][1] = 0; kernel[0][2] = 0;
		kernel[1][0] = 0; kernel[1][1] = 1; kernel[1][2] = 0;
		kernel[2][0] = 0; kernel[2][1] = 0; kernel[2][2] = 0;

		for (int y = 0; y < dst.height(); y++) {
			for (int x = 0; x < dst.width(); x++) {
				dst.setPixelVal(x, y, this->conSumIdentity(src, x, y));
			}
			//identity
		}
	}
	dst.setHeight(src.height());
	dst.setWidth(src.width());
}