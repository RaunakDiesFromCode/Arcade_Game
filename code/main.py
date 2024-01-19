import pygame, sys
from settings import *
import settings
from level import Level

class Game:
	def __init__(self):

		# general setup
		pygame.init()
		self.screen = pygame.display.set_mode((WIDTH,HEIGTH))
		pygame.display.set_caption('Zelda')
		self.clock = pygame.time.Clock()

		self.level = Level()

		# sound 
		main_sound = pygame.mixer.Sound('/Users/raunakmanna/Documents/Programming/Python/Arcade_Game/audio/main.ogg')
		main_sound.set_volume(0.5)
		main_sound.play(loops = -1)
		if settings.RESTART == True:
			main_sound.stop()
	
	def run(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_m:
						self.level.toggle_menu()

			self.screen.fill(WATER_COLOR)
			self.level.run()
			pygame.display.update()
			self.clock.tick(FPS)
			print(settings.HEALTH)
			if settings.HEALTH <= 0:
				print('Death')
				# print(settings.HEALTH)
				# screen = pygame.display.set_mode((400, 300))
				font = pygame.font.SysFont("Arial", 36)
				txtsurf = font.render("Hello, World", True, 'white')
				self.screen.blit(txtsurf,(200 , 150 ))
				# txtsurf = font.render("Hello, World", True, 'white')
				# sys.exit()

			if settings.RESTART == True:
				
				self.__init__()
				settings.MENU = False
				settings.RESTART = False
				settings.DIED = False


if __name__ == '__main__':
	game = Game()
	game.run()