# CMakeList.txt : CMake project for Bonus 4, include source and define
# project specific logic here.
#

# Add source to this project's executable.
add_executable (CMakeTarget "Bonus 4.cpp" naiveBayes.h naiveBayes.cpp knn.h knn.cpp matrix.h matrix.cpp)

if (CMAKE_VERSION VERSION_GREATER 3.12)
  set_property(TARGET CMakeTarget PROPERTY CXX_STANDARD 20)
endif()

