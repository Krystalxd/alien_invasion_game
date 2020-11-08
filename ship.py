import pygame
from pygame.sprite import Sprite

class Ship(Sprite):  # инифиализирует корабль и задает его начальную позицию
    def __init__(self, ai_setting, screen):
    	Sprite.__init__(self)
    	super(Ship, self).__init__
    	self.screen = screen
    	self.ai_setting = ai_setting
    	self.image = pygame.image.load('C:/Users/Edgar/Desktop/alien_invasion_game/images/ship.bmp')  # загружаем изображение корабся
    	self.rect = self.image.get_rect()  # представляем изображение в виде прямоугольника
    	self.screen_rect = screen.get_rect()  # экран в виде прямоугольника
    	self.rect.centerx = self.screen_rect.centerx  # координата x центра корабля
    	self.rect.bottom = self.screen_rect.bottom  # координата y низа корабля
    	self.center = float(self.rect.centerx)  # дробное значение для ускорения движения корабля
    	self.ycenter = float(self.rect.bottom)
    	self.moving_right = False  # Флаг перемещения
    	self.moving_left = False
    	self.moving_up = False
    	self.moving_down = False
    	self.pause_flag = -1

    def blitme(self):
        self.screen.blit(self.image, self.rect) # выводит изображение image в позиции self.rect

    def update(self):  # Обновляет позицию корабля с учетом флага.
        if self.moving_right and self.rect.right < self.screen_rect.right:
        	self.center += self.ai_setting.ship_speed_factor  # ускорение корабля
        if self.moving_left and self.rect.left > 0:
        	self.center -= self.ai_setting.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
        	self.ycenter += self.ai_setting.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
        	self.ycenter -= self.ai_setting.ship_speed_factor

        self.rect.centerx = self.center 
        self.rect.bottom = self.ycenter

    def center_ship(self):
    	self.center = self.screen_rect.centerx
    	self.ycenter = self.screen_rect.bottom

class LowerShip(Sprite):
	def __init__(self, ai_setting, screen):
		Sprite.__init__(self)
		super(LowerShip, self).__init__
		self.screen = screen
		self.ai_setting = ai_setting
		self.image = pygame.image.load('C:/Users/Edgar/Desktop/alien_invasion_game/images/lower_ship.bmp')  # загружаем изображение корабся
		self.rect = self.image.get_rect()  # представляем изображение в виде прямоугольника
		self.screen_rect = screen.get_rect()  # экран в виде прямоугольника
		self.rect.centerx = self.screen_rect.centerx  # координата x центра корабля
		self.rect.bottom = self.screen_rect.bottom  # координата y низа корабля
