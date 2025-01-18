import pygame as pg
import os
import random


class Init:
    @staticmethod
    def init(weight, height, color):
        pg.init()

        screen = pg.display.set_mode((weight, height), pg.DOUBLEBUF)
        pg.display.set_caption('К щелчку')
        screen.fill(pg.Color(color))

        return screen

    @staticmethod
    def begin_for(screen, color):
        screen.fill(pg.Color(color))

    @staticmethod
    def end_for(clock, FPS):
        pg.display.flip()
        pg.display.update()
        clock.tick(FPS)

    @staticmethod
    def load_image(name, colorkey=None):
        fullname = os.path.join('data', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            exit()
        image = pg.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image


class Player(pg.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.rect = pg.Rect(x - 10, y - 10, 20, 20)
        self.mask = pg.mask.Mask((20, 20))

    def draw(self, screen):
        pg.draw.rect(screen, pg.Color('Blue'), self.rect)

    def update(self, step=0):
        if not pg.sprite.spritecollideany(self, platforms):
            self.rect.y += 50 / FPS


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, *group):
        super().__init__(*group)
        self.rect = pg.Rect(x, y, 50, 10)
        self.mask = pg.mask.Mask((50, 10))

    def draw(self, screen):
        pg.draw.rect(screen, pg.Color('Gray'), self.rect)


WEIGHT, HEIGHT = 800, 800
COLOR = 'Black'
screen = Init.init(WEIGHT, HEIGHT, COLOR)

clock = pg.time.Clock()
FPS = 60
is_running = True

platforms = pg.sprite.Group()
player = None

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            if event.button == pg.BUTTON_LEFT:
                Platform(event.pos[0], event.pos[1], platforms)
            elif event.button == pg.BUTTON_RIGHT:
                player = Player(event.pos[0], event.pos[1])
    Init.begin_for(screen, COLOR)

    if player:
        player.draw(screen)
        player.update()
        steps = pg.key.get_pressed()
        if steps[pg.K_a] or steps[pg.K_LEFT]:
            player.rect.x -= 10
        elif steps[pg.K_d] or steps[pg.K_RIGHT]:
            player.rect.x += 10
    for item in platforms:
        item.draw(screen)
    platforms.update()

    Init.end_for(clock, FPS)
pg.quit()
