import pygame
import random
vec = pygame.math.Vector2

# 전역상수
SCREEN_X = 640 * 2  # 화면 넓이
SCREEN_Y = 410 * 2  # 화면 높이
FPS = 60
class Apple(pygame.sprite.Sprite):
    def __init__(self, root):
        self.image = pygame.image.load('apple.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.game = root
        self.groups= self.game.all_sprite
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = vec(random.randint(0,SCREEN_X), random.randint(0, SCREEN_Y))

    def update(self):
        self.rect.center = self.pos
        if self.collide():
            self.game.snake.score += 1
            self.kill()
            del self

    def collide(self):
        return pygame.sprite.spritecollide(self, self.game.snakes, False)

class Snake(pygame.sprite.Sprite):
    def __init__(self, root):
        self.image = pygame.image.load('Snake-a (1).png').convert_alpha()
        self.rect = self.image.get_rect()
        self.game = root
        self.groups= self.game.all_sprite, self.game.snakes
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.pos = vec(SCREEN_X/2, SCREEN_Y/2)
        self.score = 0

    def update(self):
        if self.game.pressed_key[pygame.K_UP]:
            self.pos.y += -9
        if self.game.pressed_key[pygame.K_DOWN]:
            self.pos.y += 9
        if self.game.pressed_key[pygame.K_LEFT]:
            self.pos.x += -9
        if self.game.pressed_key[pygame.K_RIGHT]:
            self.pos.x += 9
        self.rect.center = self.pos


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('스네이크 게임')
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))  # 화면 세팅
        self.clock = pygame.time.Clock()  # 시계 지정
        self.playing = True
        self.all_sprite = pygame.sprite.Group()
        self.snakes = pygame.sprite.Group()
        self.snake = Snake(self)
        self.all_sprite.add(self.snake)
        self.snakes.add(self.snake)
        self.pressed_key = pygame.key.get_pressed()
        self.bg = pygame.image.load('Stripes.png')
        self.bg = pygame.transform.scale(self.bg, (SCREEN_X, SCREEN_Y))

    def run(self):
        while self.playing:
            self.clock.tick(FPS)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        # 종료 코드
        self.pressed_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        if len(self.all_sprite) < 20:
            self.all_sprite.add(Apple(self))
        self.all_sprite.update()
        print(self.snake.score)

    def draw(self):

        self.screen.fill('white')
        self.screen.blit(self.bg, (0, 0))
        self.all_sprite.draw(self.screen)


game = Game()
game.run()
pygame.quit()