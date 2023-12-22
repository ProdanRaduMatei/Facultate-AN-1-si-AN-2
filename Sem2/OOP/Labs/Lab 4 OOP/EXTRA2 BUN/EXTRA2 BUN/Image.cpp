#include "Image.h"
#include "Size.h"
#include <exception>
#include <fstream>
#include <sstream>
#include <iostream>

using namespace std;
using namespace namespaceImgApp;

Image::Image()
{
	this->m_width = 0;
	this->m_height = 0;
	this->m_data = nullptr;

	/*this->m_data = new unsigned int*[9999];
	for (int i = 0; i < 9999; i++)
		this->m_data[i] = new unsigned int[9999];*/
	
}

Image::Image(unsigned int w, unsigned int h)
{
	this->m_width = w;
	this->m_height = h;
	this->m_data = new unsigned int*[h];
	for (int i = 0; i < this->m_height; i++)
		this->m_data[i] = new unsigned int[w];
}

Image::Image(const Image& other)
{
	//if (this->m_height != other.m_height || this->m_width != other.m_width)
		//throw exception();

	this->m_height = other.m_height;
	this->m_width = other.m_width;

	this->m_data = new unsigned int* [this->m_height];
	for (int i = 0; i < this->m_height; i++)
		this->m_data[i] = new unsigned int[this->m_width];

	for (int i = 0; i < this->m_height ; i++)
		for (int j = 0; j < this->m_width; j++)
			this->m_data[i][j] = other.m_data[i][j];
}

Image::~Image()
{
	this->release();
}

Image& Image::operator=(const Image& other)
{
	if (this == &other)
		return *this;
	this->m_height = other.m_height;
	this->m_width = other.m_width;

	this->release();
	this->m_data = new unsigned int* [this->m_height];
	for (int i = 0; i < this->m_height; i++)
		this->m_data[i] = new unsigned int[this->m_width];

	for (int i = 0; i < this->m_height; i++)
		for (int j = 0; j < this->m_width; j++)
			this->m_data[i][j] = other.m_data[i][j];

	return *this;
}

Image Image::operator+(const Image& image)
{
	if (this->size() < image.size())
		throw exception();

	Image result(this->size().getWidth(), this->size().getHeight());

	for (int i = 0; i < this->m_height; i++)
		for (int j = 0; j < this->m_width; j++)
			result.m_data[i][j] = this->m_data[i][j] + image.m_data[i][j];

	return result;
}

Image Image::operator-(const Image& image)
{
	if (this->size() < image.size())
		throw exception();

	Image result(this->size().getWidth(), this->size().getHeight());

	for (int i = 0; i < this->m_height; i++)
		for (int j = 0; j < this->m_width; j++)
			result.m_data[i][j] = this->m_data[i][j] - image.m_data[i][j];

	return result;
}

Image Image::operator*(const Image& image)
{
	if (this->size() < image.size())
		throw exception();

	Image result(this->size().getWidth(), this->size().getHeight());

	for (int i = 0; i < this->m_height; i++)
		for (int j = 0; j < this->m_width; j++)
			result.m_data[i][j] = this->m_data[i][j] * image.m_data[i][j];

	return result;
}

bool Image::getROI(Image& roiImg, Rectangle roiRect)
{
	unsigned int x = roiRect.getX(), y = roiRect.getY(), width = roiRect.getWidth(), height = roiRect.getHeight();
	if (roiImg.m_width < x + width || roiImg.m_height < y + height)
		return false;

	Image toReturn(width, height);

	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++)
			toReturn.m_data[i][j] = roiImg.m_data[y + i][x + j];
	}

	roiImg = toReturn;

	return true;
}

bool Image::getROI(Image& roiImg, unsigned int x, unsigned int y, unsigned int width, unsigned int height)
{
	if (roiImg.m_width < x + width || roiImg.m_height < y + height)
		return false;

	Image toReturn(width, height);

	for (int i = 0; i < height; i++) {
		for (int j = 0; j < width; j++)
			toReturn.m_data[i][j] = roiImg.m_data[y + i][x + j];
	}

	roiImg = toReturn;

	return true;
}

bool Image::isEmpty() const
{
	if (this->m_height == 0 && this->m_width == 0)
		return true;
	return false;
}

Size Image::size() const
{
	return Size();
}

unsigned int Image::width() const
{
	return this->m_width;
}

unsigned int Image::height() const
{
	return this->m_height;
}

unsigned int Image::getPixelVal(int x, int y) const
{
	return this->m_data[y][x];
}

void Image::setPixelVal(int x, int y, float val) const
{
	unsigned val2;
	if (val < 0)
		val2 = 0;
	else if (val > 255)
		val2 = 255;
	else
		val2 = unsigned int(val);
	this->m_data[y][x] = val2;
}

void Image::setHeight(unsigned int newHeight)
{
	this->m_height = newHeight;
}

void Image::setWidth(unsigned int newWidth)
{
	this->m_width = newWidth;
}

unsigned int& Image::at(unsigned int x, unsigned int y)
{
	return this->m_data[x][y];
}

unsigned int& Image::at(Point pt)
{
	return this->m_data[pt.getX()][pt.getY()];
}

unsigned int* Image::row(int y)
{
	return m_data[y];
}

void Image::zeros(unsigned int width, unsigned int height)
{
	for (int i = 0; i < height; i++) {
		for (int j = 0; i < width; j++) {
			this->m_data[i][j] = 0;
		}
	}

}

void Image::ones(unsigned int width, unsigned int height)
{
	for (int i = 0; i < height; i++) {
		for (int j = 0; i < width; j++) {
			this->m_data[i][j] = 1;
		}
	}
}

void Image::release()
{
	for (int i = 0; i < this->m_height; i++)
		delete[] m_data[i];
	delete[] m_data;
}

bool Image::load(std::string imagePath)
{
	this->release();

	cout << "Loading image from: " << imagePath << endl;

	ifstream infile(imagePath);
	stringstream ss;
	string inputLine = "";

	// First line : version
	getline(infile, inputLine);
	if (inputLine.compare("P2") != 0) cerr << "Version error" << endl;
	else cout << "Version : " << inputLine << endl;

	// Second line : comment
	getline(infile, inputLine);
	cout << "Comment : " << inputLine << endl;

	// Continue with a stringstream
	ss << infile.rdbuf();
	// Third line : size
	ss >> this->m_width >> this->m_height;
	cout << this->m_width << " columns and " << m_height << " rows" << endl;

	// Fourth line : The maximum gray value
	int maxVal;
	ss >> maxVal;
	cout << "The maximum gray value: " << maxVal << endl;



	// Allocate memory
	this->m_data = new unsigned int* [this->m_height];
	for (int i = 0; i < this->m_height; i++)
		this->m_data[i] = new unsigned int[this->m_width];




	// Following lines : data
	for (int i = 0; i < this->m_height; i++)
		for (int j = 0; j < this->m_width; j++) ss >> this->m_data[i][j];
	cout << "Done loading! " << endl;

	return true;
}

bool Image::save(std::string imagePath)
{
	cout << "Saving image to: " << imagePath << endl;

	fstream fout;
	fout.open(imagePath, ofstream::out, ofstream::trunc);

	fout << "P2" << endl;
	fout << "# Result image" << endl;
	fout << this->m_width << " " << this->m_height << endl;
	fout << 255 << endl;

	for (int i = 0; i < this->m_height; i++) {
		for (int j = 0; j < this->m_width; j++) {
			fout << this->m_data[i][j] << " ";
		}
		fout << endl;
	}
	
	cout << "Saved! " << endl;
	return true;
}

std::ostream& operator<<(std::ostream& os, const Image& dt)
{
	for (int i = 0; i < dt.height(); i++) {
		for (int j = 0; j < dt.width(); j++)
			os << dt.getPixelVal(j,i) << " ";
		os << endl;
	}
	return os;
}
