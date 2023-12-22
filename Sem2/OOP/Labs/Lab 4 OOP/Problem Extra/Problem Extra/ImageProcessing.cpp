#include <iostream>
#include <algorithm>
#include "Image.h"
#include "ImageProcessing.h"
#include "Rectangle.h"
#include "Point.cpp"


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
                                sum += image.pixel(py, px) * kernel[(ky + k) * kernelSize + (kx + k)];
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


void drawCircle(Image& img, const Point& center, int radius, unsigned char color) {
    // Draw a circle on the image
    int centerX = center.getX();
    int centerY = center.getY();

    for (int y = 0; y < img.getHeight(); ++y) {
        for (int x = 0; x < img.getWidth(); ++x) {
            int dx = x - centerX;
            int dy = y - centerY;
            int distance = dx * dx + dy * dy;

            if (distance <= radius * radius) {
                img.setPixel(x, y, color);
            }
        }
    }
}

void drawLine(Image& img, const Point& p1, const Point& p2, unsigned char color) {
    // Draw a line on the image
    int x1 = p1.getX();
    int y1 = p1.getY();
    int x2 = p2.getX();
    int y2 = p2.getY();

    int dx = abs(x2 - x1);
    int dy = abs(y2 - y1);
    int sx = (x1 < x2) ? 1 : -1;
    int sy = (y1 < y2) ? 1 : -1;
    int err = dx - dy;

    while (x1 != x2 || y1 != y2) {
        img.setPixel(x1, y1, color);
        int e2 = 2 * err;
        if (e2 > -dy) {
            err -= dy;
            x1 += sx;
        }
        if (e2 < dx) {
            err += dx;
            y1 += sy;
        }
    }

    img.setPixel(x2, y2, color);
}

void drawRectangle(Image& img, const Rectangle& r, unsigned char color) {
    // Draw a rectangle on the image
    int x = r.getX();
    int y = r.getY();
    int width = r.getWidth();
    int height = r.getHeight();

    for (int i = x; i < x + width; ++i) {
        img.setPixel(i, y, color);
        img.setPixel(i, y + height - 1, color);
    }

    for (int j = y + 1; j < y + height - 1; ++j) {
        img.setPixel(x, j, color);
        img.setPixel(x + width - 1, j, color);
    }
}

void drawRectangle(Image& img, const Point& tl, const Point& br, unsigned char color) {
    // Draw a rectangle on the image given top-left and bottom-right points
    int x1 = tl.getX();
    int y1 = tl.getY();
    int x2 = br.getX();
    int y2 = br.getY();

    int x = std::min(x1, x2);
    int y = std::min(y1, y2);
    int width = std::abs(x2 - x1);
    int height = std::abs(y2 - y1);

    Rectangle r(x, y, width, height);
    drawRectangle(img, r, color);
}
