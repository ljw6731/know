import pygame
import random
from pygame.locals import *

Screen_x = 480 * 2
Screen_y = 300 * 2
CHARACTER_SPEED = 5

class Player:
    def __init__(self, root):
        self.x = 100
        self.y = Screen_y-200
        self.dx = 0
        self.dy = 0
        self.game = root
        self.image = self.game.player_image
        self.hit = 0

    def move(self, key):
        if key == pygame.K_UP:
            self.dy = -CHARACTER_SPEED
            self.dx = 0
        if key == pygame.K_DOWN:
            self.dy = CHARACTER_SPEED
            self.dx = 0
        if key == pygame.K_LEFT:
            self.dx = -CHARACTER_SPEED
            self.dy = 0
        if key == pygame.K_RIGHT:
            self.dx = CHARACTER_SPEED
            self.dy = 0

        if 0 < self.x < Screen_x:
            self.x += self.dx
        else:
            self.dx *= -1
            self.x += self.dx

        if 0 < self.y < Screen_y:
            self.y += self.dy
        else:
            self.dy *= -1
            self.y += self.dy

    def draw(self):
        game.screen.blit(self.image, (self.x, self.y))

    # def hit_by(self, rain):
    #     return pygame.Rect(self.x, self.y, 108, 138).collidepoint((rain.x, rain.y))

class Cloud:
    def __init__(self, x, root):
        self.x = x
        self.y = random.randint(0,100)
        self.image = root.image_cloud
        self.game = root
        self.speed = random.randint(3, 10)

    def move(self):
        self.x  += self.speed
        if self.x > Screen_x:
            self.x = 0

    def draw(self):
        self.game.screen.blit(self.image, (self.x, self.y))

    def rain(self):
        self.game.rains.append(Rain(self.x+random.randint(0, 130), self.y+60, self.game))

    def click(self):
        pos = pygame.mouse.get_pos()
        rect = self.image.get_rect()
        rect.x = self.x
        rect.y = self.y
        return rect.collidepoint(pos)

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

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('게임제목')
        self.screen = pygame.display.set_mode((Screen_x, Screen_y))
        self.clock = pygame.time.Clock()
        self.playing = True
        self.rains = []
        self.clouds = []
        self.load_data()
        self.player = Player(self)

    def load_data(self):
        self.image = pygame.image.load('99A3E1445FD60DEA3B.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (Screen_x, Screen_y))

        self.image_cloud = pygame.image.load('cloud (1).svg')
        self.player_image = pygame.image.load('dino.png').convert_alpha()
        self.player_image = pygame.transform.scale(self.player_image, (260,200))

        self.player_dinos = []
        for x in range(1, 11):
            self.player_dinos.append(pygame.image.load) = pygame.image.load(f'Idle ({x}).png').convert_alpha()


    def run(self):
        self.opening()
        while self.playing:
            self.clock.tick(55)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()
        self.ending()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                for cloud in self.clouds:
                   if cloud.click():
                       self.clouds.remove(cloud)
                       del cloud
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_q:
                    self.playing = False
                self.player.move(event.key)

    def update(self):
        # 구름생성
        while len(self.clouds)<10:
            self.clouds.append(Cloud(random.randint(0, Screen_x), self))
        # 구름에서 비 내리기
        for cloud in self.clouds:
            cloud.rain()
        # 비 움직이게 하고벗어나면 삭제
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain
        # 구름 움직이기
        for cloud in self.clouds:
            cloud.move()
        # 캐릭터 움직이기
        self.player.move(None)

    def draw(self):
        self.screen.fill((200, 255, 200))
        self.screen.blit(self.image, (0, 0))
        for rain in self.rains:
            rain.draw()
        for cloud in self.clouds:
            cloud.draw()
        self.player.draw()

    def opening(self):
        self.screen.fill(pygame.Color('black'))
        stop = True
        self.draw_text(f'스페이스 바를 누르면 게임이 시작 됩니다.', 30, pygame.Color('hotpink'), 100, Screen_y * 1 / 20)
        self.draw_text(f'구름을 클릭하면 구름이 사라집니다.', 30, pygame.Color('hotpink'), 100,  Screen_y * 2 / 20)
        self.draw_text(f'방향키로 공룡을 조작합니다.', 30, pygame.Color('hotpink'), 100, Screen_y * 3 / 20)
        self.draw_text(f'q를 누르면 게임이 종료됩니다.', 30, pygame.Color('hotpink'), 100, Screen_y * 4 / 20)
        pygame.display.flip()
        while stop:
            self.clock.tick(60)
            pygame.event.get()
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[K_SPACE]:
                stop = False

    def ending(self):
        self.screen.fill(pygame.Color('black'))
        stop = True
        self.draw_text(f' .', 30, pygame.Color('hotpink'), 100, Screen_y * 1 / 20)
        self.draw_text(f'구름을 클릭하면 구름이 사라집니다.', 30, pygame.Color('hotpink'), 100, Screen_y * 2 / 20)
        self.draw_text(f'방향키로 공룡을 조작합니다.', 30, pygame.Color('hotpink'), 100, Screen_y * 3 / 20)
        pygame.display.flip()
        while stop:
            self.clock.tick(60)
            pygame.event.get()
            self.pressed_key = pygame.key.get_pressed()
            if self.pressed_key[K_SPACE]:
                stop = False

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('malgungothic', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.screen.blit(text_surface, text_rect)



game = Game()
game.run()
pygame.QUIT()