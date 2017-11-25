cmake_minimum_required(VERSION 3.8)
project(unclepy)

set(CMAKE_CXX_STANDARD 17)
find_package(OpenGL REQUIRED)
#link_libraries(glfw)

set(GLFW_SOURCE_DIR "glfw-3.2.1")
set(GLAD "${GLFW_SOURCE_DIR}/deps/glad/glad.h" "${GLFW_SOURCE_DIR}/deps/glad.c")

add_subdirectory(${GLFW_SOURCE_DIR})

include_directories(${GLFW_SOURCE_DIRS}/include ${GLFW_SOURCE_DIR}/deps)
add_executable(unclepy main.cpp ${GLAD})

target_link_libraries(unclepy glfw)

