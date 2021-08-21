import pygame
import random

Screen_x = 480 * 2
Screen_y = 300 * 2



class Rain():
    def __init__(self, x, y, game):
        self.x = x
        self.y = y
        self.speed = random.randint(5, 18)
        self.bold = random.randint(1, 4)
        self.game = game
        self.color = pygame.Color('skyblue')
        self.len = random.randint(5, 15)

    def move(self):
        self.y += self.speed
        self.x += 0

    def off_screen(self):
        return self.y > Screen_y+20

    def draw(self):
        pygame.draw.line(self.game.screen, self.color, (self.x, self.y), (self.x, self.y+self.len), self.bold)


class Sa(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.image = pygame.image.load('139492090-탱크-독일-제2차-세계-대전-타이거-1-중전차-군사-군대-기계-전쟁-무기-전투-기호-실루엣-측면-보기-아이콘-벡터-일러스트-레이-션-절연.jpg')
        #self.image.fill('Red')
        self.image = pygame.transform.scale(self.image, (200,200))
        self.image_t = self.image
        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.rect.centerx = Screen_x/2
        self.rect.centery = Screen_y *8 /10
        self.angle = 0
        self.mask = self.image.get_masks()
        self.pos = pygame.math.Vector2(0,0)


    def update(self):
        # self.angle +=1
        self.image = pygame.transform.rotozoom(self.image_t, self.angle, 1)
        self.image.set_colorkey()
        self.rect = self.image.get_rect()
        self.pos.x += 8
        if self.pos.x > Screen_x:
            self.pos.x = 0
        self.pos.y = Screen_y * 8 / 10
        self.rect.center = self.pos



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임제목')
        self.screen = pygame.display.set_mode((Screen_x, Screen_y))
        self.clock = pygame.time.Clock()
        self.playing = True
        self.all_sprites = pygame.sprite.Group()
        self.sa = Sa(self)
        self.rains = []

    def run(self):
        while self.playing:
            self.clock.tick(90)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        self.rains.append(Rain(random.randint(0, Screen_x) , 100, self))


    def update(self):
        self.all_sprites.update()
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain



    def draw(self):
        self.screen.fill((255, 255, 255))
        self.all_sprites.draw(self.screen)
        for rain in self.rains:
            rain.draw()


game = Game()
game.run()
pygame.QUIT()