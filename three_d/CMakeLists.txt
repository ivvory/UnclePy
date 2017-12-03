cmake_minimum_required(VERSION 3.8)
project(unclepy)
set(CMAKE_CXX_STANDARD 17)

#set(GLFW_SOURCE_DIR "glfw-3.2.1")
#set(GLAD "${GLFW_SOURCE_DIR}/deps/glad/glad.h" "${GLFW_SOURCE_DIR}/deps/glad.c")
#
#add_subdirectory(${GLFW_SOURCE_DIR})
add_subdirectory(graphics)
#include_directories(${GLFW_SOURCE_DIRS}/include ${GLFW_SOURCE_DIR}/deps)

#add_executable(unclepy main.cpp ${GLAD})
add_executable(unclepy main.cpp)

#target_link_libraries(unclepy glfw)
target_link_libraries(unclepy graphics)

