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


class Bomb(pg.sprite.Sprite):
    def __init__(self, group):
        # НЕОБХОДИМО вызвать конструктор родительского класса Sprite.
        # Это очень важно !!!
        super().__init__(group)
        self.image = Init.load_image("bomb2.png")
        self.mask = pg.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WEIGHT - self.image.get_width())
        self.rect.y = random.randrange(HEIGHT - self.image.get_height())
        between = group.copy()
        between.remove(self)
        while pg.sprite.spritecollideany(self, between):
            self.rect.x = random.randrange(WEIGHT - self.image.get_width())
            self.rect.y = random.randrange(HEIGHT - self.image.get_height())

    def update(self, *args):
        if args and args[0].type == pg.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            image = Init.load_image("boom.png")
            self.rect.x -= (image.get_width() - self.image.get_width()) / 2
            self.rect.y -= (image.get_height() - self.image.get_height()) / 2
            self.image = image


WEIGHT, HEIGHT = 800, 800
COLOR = 'Black'
screen = Init.init(WEIGHT, HEIGHT, COLOR)

clock = pg.time.Clock()
FPS = 145
is_running = True

all_sprites = pg.sprite.Group()
for _ in range(20):
    Bomb(all_sprites)

while is_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            all_sprites.update(event)
    Init.begin_for(screen, COLOR)

    all_sprites.draw(screen)
    all_sprites.update()

    Init.end_for(clock, FPS)
pg.quit()
