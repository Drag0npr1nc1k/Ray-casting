from settings import *
from drawing import *

def drawScene(screen, player, fov):
	screen.fill(skyColor)
	pygame.draw.rect(screen, groundColor, (0, HEIGHT // 2, WIDTH, HEIGHT // 2))

	for x in range(0, WIDTH, resolution):
		rayAngle = (fov / 2) - (x / WIDTH) * fov
		dist = Raycasting.castRay(player.pos, math.atan2(player.dir[1], player.dir[0]) + rayAngle)
		height = HEIGHT / (dist * math.cos(rayAngle))
		wallColorDarkened = (int(wallColor[0] * min(1.0, 1.0 - (1.0 / distanceView * dist))), (wallColor[1] * min(1.0, 1.0 - (1.0 / distanceView * dist))), (wallColor[2] * min(1.0, 1.0 - (1.0 / distanceView * dist))))

		pygame.draw.rect(screen, wallColorDarkened, (x, HEIGHT/2 - height/2, resolution, height))
