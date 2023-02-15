import networktables as nt
from networktables import NetworkTables
import pygame

from ui_utils import *
from logic import * 
from UI_CONSTANTS import * 

def main():
	pygame.init()
	NetworkTables.initialize()
	table = NetworkTables.getTable('SmartDashboard') # Maybe change the table?

	pygame.display.set_caption('Place Cones/Cubes Interface')
	WIDTH = SQUARE_SIDE_LENGTH * 9
	HEIGHT = SQUARE_SIDE_LENGTH * 3
	window_surface = pygame.display.set_mode((WIDTH + GRID_GAP * 8, HEIGHT + GRID_GAP * 2))

	background = pygame.Surface((WIDTH, HEIGHT))
	background.fill(pygame.Color('#000000'))

	is_running = True

	while is_running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_running = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				grid_coords = get_grid_coord_from_click(event.pos)
				table.putNumber("Target_Grid_Coord", [float(x) for x in grid_coords])
			else:
				# TODO: color code placeable grid nodes
				draw_grid(window_surface)
				pygame.display.update()

main()