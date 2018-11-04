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

surfaces = (
    (0,1,2,3),
    (3,2,6,7),
    (4,5,6,7),
    (4,5,1,0),
    (1,5,6,2),
    (4,0,3,7)
    )

colors = (
	(0.2,0.85,0.4),
	(0.3,0.85,0.6),
	(0.4,0.85,0.8),
	(0.5,0.85,1)
	)

# 画出立方体
def Cube():
	glBegin(GL_QUADS)
	for surface in surfaces:
		x = 0
		for vertex in surface:
			glColor3fv(colors[x])
			glVertex3fv(vertices[vertex])
			x = x + 1
	glEnd()

showcase.main(Cube)
