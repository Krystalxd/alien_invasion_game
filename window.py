import pygame
import sys  # нужно для завершения игры по команде игрока
from settings import Settings  # используем наш модуль с настройками
from ship import Ship, LowerShip
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
from client import update_score

def run_game():
    # Инициализирует игру и создает объект экрана.
    pygame.init()  # инициализирует настройки, необходимые Pygame для нормальной работы.
    background_image = pygame.image.load('C:/Users/Edgar/Desktop/alien_invasion_game/images/background.bmp')
    ai_settings = Settings()  # создаем экземпляр класса
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height), pygame.FULLSCREEN)  # задаем разрешение экрана
    pygame.display.set_caption("Alien Invasion")
    pygame.display.set_icon(pygame.image.load('C:/Users/Edgar/Desktop/alien_invasion_game/images/Jedi_Order.bmp'))
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    ship = Ship(ai_settings, screen)  # Cоздание корабля
    lower_ship = LowerShip(ai_settings, screen)
    alien = Alien(ai_settings, screen)
    play_button = Button(ai_settings, screen, "Play")
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # Запуск основного цикла игры.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)  # Отслеживание событий клавиатуры и мыши.
        if ship.pause_flag == -1:
        	if stats.game_active:
        	    ship.update()
        	    gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
        	    gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
        	gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, background_image)  # обновление экрана
        else:
        	gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, background_image)  # обновление экрана
run_game()
