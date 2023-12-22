#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstring>
#include "Point.h"

class Image {
private:
    int* pixels;
    int width;
    int height;
    
public:
    // Constructors and Destructor
    Image(): pixels(nullptr), width(0), height(0) {}
    Image(int width, int height): pixels(new int[width*height]), width(width), height(height) {}
    Image(const Image& other): pixels(new int[other.width*other.height]), width(other.width), height(other.height) {
        std::memcpy(pixels, other.pixels, sizeof(int)*width*height);
    }
    ~Image() {
        delete[] pixels;
    }
    
    // Copy assignment operator
    Image& operator=(const Image& other) {
        if (this == &other)
            return *this;
        delete[] pixels;
        pixels = new int[other.width*other.height];
        width = other.width;
        height = other.height;
        std::memcpy(pixels, other.pixels, sizeof(int)*width*height);
        return *this;
    }
    
    // Getters
    int getWidth() const {
        return width;
    }
    int getHeight() const {
        return height;
    }
    std::string getSize() const {
        return std::to_string(width) + "x" + std::to_string(height);
    }
    
    bool loadFromFile(const std::string& filename) {
        std::ifstream file(filename, std::ios::binary);
        if (!file.is_open()) {
            return false;
        }
        std::string magicNumber;
        std::getline(file, magicNumber);
        if (magicNumber != "P2") { // Change magic number to "P2" for PGM format
            return false;
        }
        int maxVal;
        file >> width >> height >> maxVal;
        file.get(); // consume the newline character
        delete[] pixels;
        pixels = new int[width * height];
        for (int i = 0; i < width * height; ++i) {
            int value;
            file >> value;
            pixels[i] = value;
        }
        file.close();
        return true;
    }

    bool saveToFile(const std::string& filename) const {
        std::ofstream file(filename);
        if (!file.is_open()) {
            return false;
        }
        file << "P2\n" << width << " " << height << "\n255\n";
        for (int i = 0; i < width * height; ++i) {
            file << pixels[i] << " ";
        }
        file.close();
        return true;
    }

    
    // Operators
    friend std::ostream& operator<<(std::ostream& os, const Image& image) {
        for (int y = 0; y < image.height; y++) {
            for (int x = 0; x < image.width; x++)
                os << std::setw(3) << image.pixels[y*image.width + x] << " ";
            os << "\n";
        }
        return os;
    }
    Image operator+(const Image& other) const {
        if (width != other.width || height != other.height)
            throw std::invalid_argument("Image dimensions do not match");
        Image result(width, height);
        for (int i = 0; i < width*height; i++)
            result.pixels[i] = pixels[i] + other.pixels[i];
        return result;
    }
    Image operator-(const Image& other) const {
        if (width != other.width || height != other.height)
            throw std::invalid_argument("Image dimensions do not match");
        Image result(width, height);
        for (int i = 0; i < width*height; i++)
            result.pixels[i] = pixels[i] - other.pixels[i];
        return result;
    }
    
    Image operator*(const Image& other) const {
        if (width != other.width || height != other.height)
            throw std::invalid_argument("Image dimensions do not match");
        Image result(width, height);
        for (int i = 0; i < width*height; i++)
            result.pixels[i] = pixels[i] * other.pixels[i];
        return result;
    }
    
    Image operator+(int scalar) const {
        Image result(width, height);
        for (int i = 0; i < width*height; i++)
            result.pixels[i] = pixels[i] + scalar;
        return result;
    }
    
    Image operator-(int scalar) const {
        Image result(width, height);
        for (int i = 0; i < width*height; i++)
            result.pixels[i] = pixels[i] - scalar;
        return result;
    }
    
    Image operator*(int scalar) const {
        Image result(width, height);
        for (int i = 0; i < width*height; i++)
            result.pixels[i] = pixels[i] * scalar;
        return result;
    }
    
    bool isEmpty() const {
        return (width == 0 || height == 0);
    }
    
    // Method to get a reference to a pixel in the image
    int& operator()(int x, int y) {
        if (x < 0 || x >= width || y < 0 || y >= height)
            throw std::out_of_range("Index out of bounds");
        return pixels[y * width + x];
    }
    
    int& operator()(const Point& p) {
        return (*this)(p.x, p.y);
    }
    
    // Method to get a pointer to a row in the image
    int* getRow(int y) {
        if (y < 0 || y >= height)
            throw std::out_of_range("Index out of bounds");
        return pixels + y * width;
    }
    
    // Method to release the memory allocated for the image
    void release() {
        delete[] pixels;
        width = 0;
        height = 0;
        pixels = nullptr;
    }
    
    // Method to get a new image containing a region of interest
    Image getROI(int x, int y, int w, int h) const {
        if (x < 0 || y < 0 || w <= 0 || h <= 0 || x + w > width || y + h > height)
            throw std::out_of_range("Invalid ROI");
        
        Image roi(w, h);
        for (int j = 0; j < h; j++) {
            std::copy(pixels + (y + j) * width + x, pixels + (y + j) * width + x + w, roi.pixels + j*w);
        }
        return roi;
    }
    
    // Static methods
    static Image zeros(int w, int h) {
        Image img(w, h);
        std::memset(img.pixels, 0, w*h*sizeof(int));
        return img;
    }
    
    static Image ones(int w, int h) {
        Image img(w, h);
        std::memset(img.pixels, 1, w*h*sizeof(int));
        return img;
    }
    
    int pixel(int x, int y) const {
        return pixels[y * width + x];
    }

    // Set the pixel value at the specified coordinates
    void setPixel(int x, int y, int value) {
        pixels[y * width + x] = value;
    }
};

class ImageProcessing {
    public:
      virtual void process(const Image& src, Image& dst) = 0;
};

class BrightnessContrastAdjustment : public ImageProcessing {
    public:
        BrightnessContrastAdjustment(float alpha = 1.0f, float beta = 0.0f) : alpha(alpha), beta(beta) {}

      void process(const Image& src, Image& dst) override {
        // Iterate through each pixel in the image
          for (int i = 0; i < src.getWidth(); ++i) {
              for (int j = 0; j < src.getHeight(); ++j) {
                  // Apply brightness and contrast adjustment to each pixel
                  float value = alpha * src.pixel(i, j) + beta;

                  // Clip the result to the range [0, 255]
                  value = std::max(0.0f, std::min(255.0f, value));

                  // Set the processed pixel value in the destination image
                  dst.setPixel(i, j, value);
              }
          }
      }

    private:
      float alpha;  // Gain
      float beta;   // Bias
};

class GammaCorrection : public ImageProcessing {
    public:
        GammaCorrection(float gamma = 1.0f) : gamma(gamma) {}

    void process(const Image& src, Image& dst) override {
        // Iterate through each pixel in the image
        for (int i = 0; i < src.getWidth(); ++i) {
            for (int j = 0; j < src.getHeight(); ++j) {
                // Apply gamma correction to each pixel
                float value = std::pow(src.pixel(i, j), gamma);

                // Clip the result to the range [0, 255]
                value = std::max(0.0f, std::min(255.0f, value));

                // Set the processed pixel value in the destination image
                dst.setPixel(i, j, value);
            }
        }
    }

    private:
        float gamma;  // Gamma encoding factor
};

class ImageConvolution {
    public:
        // Constructor
        ImageConvolution(Image& image) : image(image), width(image.getWidth()), height(image.getHeight()) {}

        // Process method to perform image convolution
        void process(const int* kernel, int kernelSize) const {
            if (kernelSize % 2 == 0)
                throw std::invalid_argument("Kernel size must be odd");

            int k = kernelSize / 2;
            for (int y = 0; y < height; y++) {
                for (int x = 0; x < width; x++) {
                    int sum = 0;
                    for (int ky = -k; ky <= k; ky++) {
                        for (int kx = -k; kx <= k; kx++) {
                            int px = x + kx;
                            int py = y + ky;
                            if (px >= 0 && px < width && py >= 0 && py < height)
                                sum += image.getPixel(py, px) * kernel[(ky + k) * kernelSize + (kx + k)];
                        }
                    }
                    image.setPixel(y, x, sum);
                }
            }
        }

    private:
        Image& image;
        int width;
        int height;
};
