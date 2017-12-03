#ifndef UNCLEPY_MANAGER_H
#define UNCLEPY_MANAGER_H

#include <iostream>
#include <glad/glad.h>
#include <GLFW/glfw3.h>


class GLManager {
public:
    GLManager();
    virtual ~GLManager();

    void render_loop();
private:
    GLFWwindow* window;
};


#endif //UNCLEPY_MANAGER_H
