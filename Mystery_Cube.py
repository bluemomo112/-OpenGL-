import showcase
from OpenGL.GL import *

#pip install PyOpenGL PyOpenGL_accelerate

# 定义点
vertices = (
	(1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, 1, 1),
    (-1, -1, 1)
	)
# 定义线
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,6),
    (7,6),
    (7,4),
    (7,3),
    (5,1),
    (5,4),
    (5,6)
    )
# 画出立方体
def Cube():
	glBegin(GL_LINES)
	for edge in edges:
		for vertex in edge:
			glVertex3fv(vertices[vertex])
	glEnd()

showcase.main(Cube)
