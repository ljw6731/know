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
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.len = random.randint(5, 15)

    def move(self):
        self.y += self.speed

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

    def update(self):
        for i in range(10):
            self.rains.append(Rain(random.randint(10, Screen_x-10), 10, self))
        for rain in self.rains:
            rain.move()
            if rain.off_screen():
                self.rains.remove(rain)
                del rain

    def draw(self):
        self.screen.fill((200, 255, 200))
        for rain in self.rains:
            rain.draw()

game = Game()
game.run()
pygame.QUIT()