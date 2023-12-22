#pragma once
#include "Image.h"

using namespace namespaceImgApp;

class namespaceImgApp::ImageProcessing
{
private:
	virtual void process(const Image& src, Image& dst);
};

class Adjustment : public namespaceImgApp::ImageProcessing {
public:
	Adjustment();
	void setContrast(float c);
	void setBrightness(int b);

	void process(const Image& src, Image& dst) override;
private:
	int brightness;
	float contrast;
};

class Gamma : public namespaceImgApp::ImageProcessing {
public:
	Gamma();
	void setTita(float t);

	void process(const Image& src, Image& dst) override;
private:
	float tita;
};

class Convolution : public namespaceImgApp::ImageProcessing {
private:
	unsigned int kernel[3][3];
	unsigned int operation = 0;

public:

	void setOperation(unsigned int x);

	int rangeSobelConverter(int x);

	void process(const Image& src, Image& dst) override;

	void setKernelBlur();
	void setKernelGaussian();
	void setKernelHorizontalSobel();
	void setKernelVerticalSobel();

	int conSumIdentity(const Image& src, unsigned int x, unsigned int y);

	int conSumBlur(const Image& src, unsigned int x, unsigned int y);
	int conSumGaussian(const Image& src, unsigned int x, unsigned int y);

	int conSumHorizontalSobel(const Image& src, unsigned int x, unsigned int y);
	int conSumVerticalSobel(const Image& src, unsigned int x, unsigned int y);
};
