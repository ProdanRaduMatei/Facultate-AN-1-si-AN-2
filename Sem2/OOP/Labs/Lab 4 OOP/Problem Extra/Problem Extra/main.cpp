#include <iostream>
#include "Image.cpp" // assuming the class is defined in "Image.h"
#include "ImageProcessing.cpp"

// Test case for the ImageConvolution class
void ImageConvolutionTest_ProcessTest() {
    // Create a dummy image with known pixel values
    Image image(4, 4); // 4x4 image
    image.setPixel(0, 0, 1);
    image.setPixel(0, 1, 2);
    image.setPixel(0, 2, 3);
    image.setPixel(0, 3, 4);
    image.setPixel(1, 0, 5);
    image.setPixel(1, 1, 6);
    image.setPixel(1, 2, 7);
    image.setPixel(1, 3, 8);
    image.setPixel(2, 0, 9);
    image.setPixel(2, 1, 10);
    image.setPixel(2, 2, 11);
    image.setPixel(2, 3, 12);
    image.setPixel(3, 0, 13);
    image.setPixel(3, 1, 14);
    image.setPixel(3, 2, 15);
    image.setPixel(3, 3, 16);

    // Create an ImageConvolution object
    ImageConvolution conv(image);

    // Define a kernel for convolution
    int kernel[9] = {1, 2, 1,
                     0, 0, 0,
                     -1, -2, -1};

    // Perform convolution on the image
    conv.process(kernel, 3);

    // Check the expected pixel values after convolution
    assert(image.getPixel(0, 0) == 13);
    assert(image.getPixel(0, 1) == 20);
    assert(image.getPixel(0, 2) == 17);
    assert(image.getPixel(0, 3) == 8);
    assert(image.getPixel(1, 0) == 18);
    assert(image.getPixel(1, 1) == 24);
    assert(image.getPixel(1, 2) == 18);
    assert(image.getPixel(1, 3) == 8);
    assert(image.getPixel(2, 0) == 12);
    assert(image.getPixel(2, 1) == 12);
    assert(image.getPixel(2, 2) == 0);
    assert(image.getPixel(2, 3) == -12);
    assert(image.getPixel(3, 0) == -4);
    assert(image.getPixel(3, 1) == -4);
    assert(image.getPixel(3, 2) == -6);
    assert(image.getPixel(3, 3) == -8);
}

// Test functions for ImageProcessing subclasses
void testBrightnessContrast() {
    std::vector<float> src = {100.0f, 150.0f, 200.0f};
    std::vector<float> dst;

    BrightnessContrast bc(1.5f, 30.0f);
    bc.process(src, dst);

    std::cout << "Brightness and Contrast Adjustment Test:" << std::endl;
    std::cout << "Source Image: ";
    for (float value : src) {
        std::cout << value << " ";
    }
    std::cout << std::endl;
    std::cout << "Processed Image: ";
    for (float value : dst) {
        std::cout << value << " ";
    }
    std::cout << std::endl;
}

void testGammaCorrection() {
    std::vector<float> src = {0.5f, 1.0f, 1.5f};
    std::vector<float> dst;

    GammaCorrection gc(0.8f);
    gc.process(src, dst);

    std::cout << "Gamma Correction Test:" << std::endl;
    std::cout << "Source Image: ";
    for (float value : src) {
        std::cout << value << " ";
    }
    std::cout << std::endl;
    std::cout << "Processed Image: ";
    for (float value : dst) {
        std::cout << value << " ";
    }
    std::cout << std::endl;
}

int main() {
    // Create an image with dimensions 3x3 and fill it with zeros
    Image img(3, 3);

    // Test the loadFromFile method
    /*if (!img.loadFromFile("test.pgm")) {
        std::cerr << "Failed to load image from file.\n";
        return 1;
    }*/

    // Test the getSize method
    std::cout << "Image size: " << img.getSize() << "\n";

    // Test the operator<< method
    std::cout << img;

    // Test the copy constructor and operator=
    Image img2(img);
    Image img3 = img2;

    // Test the operator+ method
    Image img4 = img + img2;
    std::cout << img4;

    // Test the operator- method
    Image img5 = img - img2;
    std::cout << img5;

    // Test the operator* method
    Image img6 = img * img2;
    std::cout << img6;

    // Test the operator+ (scalar) method
    Image img7 = img + 100;
    std::cout << img7;

    // Test the operator- (scalar) method
    Image img8 = img - 50;
    std::cout << img8;

    // Test the operator* (scalar) method
    Image img9 = img * 2;
    std::cout << img9;

    // Test the isEmpty method
    std::cout << "img isEmpty? " << img.isEmpty() << "\n";
    Image img10;
    std::cout << "img10 isEmpty? " << img10.isEmpty() << "\n";

    // Test the operator() method
    img(0, 0) = 255;
    std::cout << img;

    // Test the saveToFile method
    if (!img.saveToFile("out.pgm")) {
        std::cerr << "Failed to save image to file.\n";
        return 1;
    }

    return 0;
}
