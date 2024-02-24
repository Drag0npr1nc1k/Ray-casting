from drawing import *
from player import *
from settings import *
from scene import *

pygame.init()

def run():
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	player = Player(playerSpeed, rotationSpeed)
	running, clock = True, pygame.time.Clock()

	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		pygame.display.set_caption(f"FPS: {clock.get_fps():.0f} Raycasting | by: Drag0n")

		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			player.move('forward')
		if keys[pygame.K_s]:
			player.move('backward')
		if keys[pygame.K_a]:
			player.rotate('left')
		if keys[pygame.K_d]:
			player.rotate('right')

		drawScene(screen, player, fov)
		Map.drawMap(screen, player.pos, mapScale, pointOnMapSize)

		clock.tick(fpsLock)
		pygame.display.flip()

	pygame.quit()
