set(GLFW_SOURCE_DIR "../glfw-3.2.1")
set(GLAD "${GLFW_SOURCE_DIR}/deps/glad/glad.h" "${GLFW_SOURCE_DIR}/deps/glad.c")

add_subdirectory(${GLFW_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR}/glfw)


add_library(graphics STATIC manager.cpp ${GLAD})
target_include_directories (graphics PUBLIC ${CMAKE_CURRENT_SOURCE_DIR} ${GLFW_SOURCE_DIR}/deps)

target_link_libraries(graphics glfw)
