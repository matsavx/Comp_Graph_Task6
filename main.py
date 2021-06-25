import math

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def Cube(vertices, edges):
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def Cylinder(radius, height):
    angle_stepsize = 0.1

    glBegin(GL_LINES)
    angle = 0.0
    while angle < 2 * math.pi:
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, height)
        glVertex3f(x, y, 0.0)
        angle = angle + angle_stepsize

    glVertex3f(radius, 0.0, height)
    glVertex3f(radius, 0.0, 0.0)

    glEnd()

    glBegin(GL_LINES)
    angle = 0.0
    while angle < 2 * math.pi:
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex3f(x, y, height)
        angle = angle + angle_stepsize

    glVertex3f(radius, 0.0, height)

    glEnd()


def Pyramid():
    glBegin(GL_LINES)

    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)

    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glEnd()

    glBegin(GL_LINES)

    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)

    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)

    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glEnd()


def Cone(height, radius):
    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0, 0, height)
    angle = 0
    while angle<360:
        glVertex3f(math.sin(angle) * radius, math.cos(angle) * radius, 0)
        angle = angle + 1

    glEnd()


def Tetraedr(a):
    v = (
        (0, 0, a * math.sqrt(6) / 4),
        (a / math.sqrt(3), 0, -a * math.sqrt(6) / 12),
        (-a / math.sqrt(12), a / 2, -a * math.sqrt(6) / 12),
        (-a / math.sqrt(12), -a / 2, -a * math.sqrt(6) / 12)
    )

    glBegin(GL_LINE_LOOP)
    glVertex3f(v[0][0], v[0][1], v[0][2])
    glVertex3f(v[1][0], v[1][1], v[1][2])
    glVertex3f(v[2][0], v[2][1], v[2][2])

    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex3f(v[0][0], v[0][1], v[0][2])
    glVertex3f(v[3][0], v[3][1], v[3][2])
    glVertex3f(v[1][0], v[1][1], v[1][2])
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex3f(v[0][0], v[0][1], v[0][2])
    glVertex3f(v[2][0], v[2][1], v[2][2])
    glVertex3f(v[3][0], v[3][1], v[3][2])
    glEnd()

    glBegin(GL_LINE_LOOP)
    glVertex3f(v[1][0], v[1][1], v[1][2])
    glVertex3f(v[3][0], v[3][1], v[3][2])
    glVertex3f(v[2][0], v[2][1], v[2][2])
    glEnd()


def Octaedr():
    glBegin(GL_LINES)

    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(1.0, 0.0, 1.0)

    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(1.0, 0.0, 1.0)
    glVertex3f(1.0, 0.0, -1.0)

    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, -1.0)

    glVertex3f(0.0, 2.0, 0.0)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, 1.0)

    glEnd()

    glBegin(GL_LINES)

    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(-1.0, 0.0, -1.0)

    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(1.0, 0.0, 1.0)

    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, -1.0)

    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(1.0, 0.0, 1.0)

    glEnd()

    glBegin(GL_LINES)

    glVertex3f(0.0, -2.0, 0.0)
    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(1.0, 0.0, 1.0)

    glVertex3f(0.0, -2.0, 0.0)
    glVertex3f(1.0, 0.0, 1.0)
    glVertex3f(1.0, 0.0, -1.0)

    glVertex3f(0.0, -2.0, 0.0)
    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, -1.0)

    glVertex3f(0.0, -2.0, 0.0)
    glVertex3f(-1.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, 1.0)

    glEnd()

    glBegin(GL_LINES)

    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(-1.0, 0.0, -1.0)

    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(1.0, 0.0, 1.0)

    glVertex3f(1.0, 0.0, -1.0)
    glVertex3f(-1.0, 0.0, -1.0)

    glVertex3f(-1.0, 0.0, 1.0)
    glVertex3f(1.0, 0.0, 1.0)

    glEnd()


def main():
    vertices = (
        (1.0, -1.0, -1.0),
        (1.0, 1.0, -1.0),
        (-1.0, 1.0, -1.0),
        (-1.0, -1.0, -1.0),
        (1.0, - 1.0, 1.0),
        (1.0, 1.0, 1.0),
        (-1.0, -1.0, 1.0),
        (-1.0, 1.0, 1.0)
    )
    edges = (
        (0, 1),
        (0, 3),
        (0, 4),
        (2, 1),
        (2, 3),
        (2, 7),
        (6, 3),
        (6, 4),
        (6, 7),
        (5, 1),
        (5, 4),
        (5, 7)
    )

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslatef(0.0, -1.0, -10)
    glRotatef(20, 10, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Cube(vertices, edges)
        # Cylinder(1, 2)
        # Pyramid()
        # Cone(2, 1)
        # Tetraedr(2)
        Octaedr()
        pygame.display.flip()
        pygame.time.wait(10)


main()
