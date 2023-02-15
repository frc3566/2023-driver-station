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

def get_grid_coord_from_click(mouse_pos):
	x = 0
	y = 0
	for i in range(3):
		for j in range(9):
			rect = pygame.Rect(x, y, SQUARE_SIDE_LENGTH, SQUARE_SIDE_LENGTH)
			if rect.collidepoint(mouse_pos):
				return (i, j)
			x += SQUARE_SIDE_LENGTH + GRID_GAP
		y += SQUARE_SIDE_LENGTH + GRID_GAP
		x = 0

# def update_grid_state(grid_state, game_piece):
# 	pass