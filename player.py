import numpy as np
import math

from settings import *
from map import *

class Player:
	def __init__(self, playerSpeed = 0.05, rotationSpeed = 0.045 , pos=[2.5, 2.5], dir=[1, 0]):
		self.worldMap = np.array(worldMap)
		self.pos = np.array(pos)    
		self.dir = np.array(dir)
		self.playerSpeed = playerSpeed
		self.rotationSpeed = rotationSpeed

	def move(self, direction):
		moveVector = None
		if direction == 'forward':
			moveVector = self.dir *  self.playerSpeed
		elif direction == 'backward':
			moveVector = -self.dir *  self.playerSpeed

		newPos = self.pos + moveVector

		if ( 0 <= newPos[0] < self.worldMap.shape[1] and 0 <= newPos[1] < self.worldMap.shape[0] and self.worldMap[int(newPos[1]), int(newPos[0])] == 0):
			self.pos = newPos

	def rotate(self, direction):
		rot = self.rotationSpeed if direction == 'left' else -self.rotationSpeed
		cosRot, sinRot = math.cos(rot), math.sin(rot)
		
		self.dir = np.array([self.dir[0] * cosRot - self.dir[1] * sinRot, self.dir[0] * sinRot + self.dir[1] * cosRot])
