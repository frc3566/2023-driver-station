"""
GRID
        C C C
Δ ▢ Δ   Δ ▢ Δ   Δ ▢ Δ
Δ ▢ Δ   Δ ▢ Δ   Δ ▢ Δ
H H H   H H H   H H H 

Cube: 0
Cone: 1
Hybrid: 2

"""

import pygame

from UI_CONSTANTS import * 
from COLORS import * 

def get_color_from_num(n, object):
	if n == 0 and object == 0:
		return CUBE
	elif n == 1 and object == 1:
		return CONE
	elif n == 2 and not object == -1:
		return HYBRID
	else:
		return INACTIVE

grid = [
	[1, 0, 1] * 3,
	[0, 1, 0] * 3,
	[2, 2, 2] * 3,
]

def draw_grid(surface, object):
	global grid
	x = 0
	y = 0
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			color = get_color_from_num(grid[i][j], object)
			pygame.draw.rect(surface, color, pygame.Rect(x, y, SQUARE_SIDE_LENGTH, SQUARE_SIDE_LENGTH))
			x += SQUARE_SIDE_LENGTH + GRID_GAP
		y += SQUARE_SIDE_LENGTH + GRID_GAP
		x = 0