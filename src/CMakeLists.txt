cmake_minimum_required(VERSION 3.13)

project(now LANGUAGES CXX)

add_executable(now now.cpp)

target_link_libraries(now PRIVATE ${CONAN_TARGETS})

target_compile_features(now PRIVATE cxx_std_17)
