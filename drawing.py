import pygame
import math
import numpy as np

from settings import *
from map import * 
from advancedSettings import *

map = np.array(worldMap)

class Raycasting:
	@staticmethod
	def castRay(positionPlayer:list[int], angle:float,):
		posX, posY = positionPlayer
		gridX, gridY = int(posX), int(posY)
		rayDirX, rayDirY = (math.cos(angle) if math.cos(angle) != 0 else 1e-10, math.sin(angle) if math.sin(angle) != 0 else 1e-10)
		stepX, sideDistX = (-1, (posX - gridX) * abs(1 / rayDirX)) if rayDirX < 0 else (1, (gridX + 1.0 - posX) * abs(1 / rayDirX))
		stepY, sideDistY = (-1, (posY - gridY) * abs(1 / rayDirY)) if rayDirY < 0 else (1, (gridY + 1.0 - posY) * abs(1 / rayDirY))
		hit, hitSide = False, None

		while not hit:
			if sideDistX < sideDistY:
				sideDistX, gridX, hitSide = sideDistX + abs(1 / rayDirX), gridX + stepX, "X"
			else:
				sideDistY, gridY, hitSide = sideDistY + abs(1 / rayDirY), gridY + stepY, "Y"

			if 0 <= gridX < map.shape[1] and 0 <= gridY < map.shape[0] and map[gridY, gridX] > 0:
				hit = True


		return (gridX - posX + (1 - stepX) / 2) / rayDirX if hitSide == "X" else (gridY - posY + (1 - stepY) / 2) / rayDirY

class Map:
	@staticmethod
	def drawMap(screen:pygame.surface.Surface, playerPosition:list[int], mapScale:float=0.25,pointOnMapSize:float=5):
		for y, row in enumerate(map):
			for x, cell in enumerate(row):
				if cell:
					pygame.draw.rect(screen, borderMiniMapColor, (x * resolution * mapScale, HEIGHT - (y + 1) * resolution * mapScale, resolution * mapScale, resolution * mapScale))
		pygame.draw.circle(screen, (255, 255, 0), (int(playerPosition[0] * resolution * mapScale), HEIGHT - int(playerPosition[1] * resolution * mapScale)), pointOnMapSize)

