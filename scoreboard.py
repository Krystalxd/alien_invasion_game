import pygame.font
from pygame.sprite import Group
from ship import Ship, LowerShip

class Scoreboard():  # класс для выввода информации
	def __init__(self, ai_settings, screen, stats):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats

		self.text_color = (211, 154, 58)

		self.font = pygame.font.SysFont(None, 48)
		self.prep_score()
		self.prep_high_score()
		self.prep_level()
		self.prep_ships()
		self.prep_pause()

	def prep_score(self):  # Преобразует текущий счет в графическое изображение
	    rounded_score = int(round(self.stats.score, -1))
	    score_str = "{:,}".format(rounded_score)
	    self.score_image = self.font.render(score_str, True, self.text_color)
	    self.score_rect = self.score_image.get_rect()
	    self.score_rect.right = self.screen_rect.right - 20
	    self.score_rect.top = 20

	def prep_pause(self):
		self.pause_image = self.font.render('Game is paused', True, self.text_color)
		self.pause_rect = self.pause_image.get_rect()
		self.pause_rect.right = self.screen_rect.right - 825
		self.pause_rect.top = 540

	def show_score(self):  # вывод счета на экран
	    self.screen.blit(self.score_image, self.score_rect)
	    self.screen.blit(self.high_score_image, self.high_score_rect)
	    self.screen.blit(self.level_image, self.level_rect)
	    self.ships.draw(self.screen)

	def show_pause(self):
		self.screen.blit(self.pause_image, self.pause_rect)

	def prep_high_score(self):  # Преобразует рекордный счет в графическое изображение.
	    high_score = int(round(self.stats.high_score, -1))
	    high_score_str = "{:,}".format(high_score)
	    self.high_score_image = self.font.render(high_score_str, True, self.text_color)

	    self.high_score_rect = self.high_score_image.get_rect()
	    self.high_score_rect.centerx = self.screen_rect.centerx
	    self.high_score_rect.top = self.score_rect.top

	def prep_level(self):  # преобразует уровень в графическое изображение
	    self.level_image = self.font.render("Текущий уровень: " + str(self.stats.level), True, self.text_color)
	    self.level_rect = self.level_image.get_rect()
	    self.level_rect.right = self.screen_rect.left + 400
	    self.level_rect.top = self.score_rect.bottom - 40

	def prep_ships(self):
		self.ships = Group()
		for ship_number in range(self.stats.ships_left):
			ship = LowerShip(self.ai_settings, self.screen)
			ship.rect.x = 500 + ship_number * (ship.rect.width + 20)
			ship.rect.y = 10
			self.ships.add(ship)
