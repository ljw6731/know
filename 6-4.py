import pygame
import random
vec = pygame.Vector2
Screen_x = 480 * 2
Screen_y = 300 * 2


class Ui(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.groups = self.game.ui
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((Screen_x, Screen_y))
        self.rect = self.image.get_rect()
        self.image.set_colorkey('Black')
        self.ui_health = self.game.sa.health

    def update(self):
        self.image.fill('Black')
        pygame.draw.rect(self.image, 'Gray', (25,30, Screen_x-50, Screen_y-50), 10, 10)
        self.ui_health = self.game.sa.health
        pygame.draw.line(self.image, 'Red', (100, Screen_y-65),  (100+self.ui_health*3, Screen_y-65), 15)
        self.draw_text(f'{self.ui_health}', 30, pygame.Color('Red'), 100, Screen_y -65)

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.SysFont('malgungothic', size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.x = x
        text_rect.y = y
        self.image.blit(text_surface, text_rect)


class Rain(pygame.sprite.Sprite):
    def __init__(self, x, y, root):
        self.speed = random.randint(5, 28)
        self.bold = random.randint(1, 4)
        self.game = root
        self.len = random.randint(5, 15)
        self.color = pygame.Color('skyblue')
        self.red = random.randint(0, 10)
        self.groups = self.game.rains, self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.image = pygame.Surface((self.bold, self.len))
        self.image.fill(self.color)
        if self.red == 0:
            self.image.fill('Red')
        self.pos = vec(x, y)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if pygame.sprite.collide_mask(self, self.game.sa):
            if self.red == 0:
                self.game.sa.health -= 10
                self.game.hit_sound.play()
            self.kill()
            del self
            return
        self.pos.y += self.speed
        self.rect.topleft = self.pos
        if self.off_screen():
            self.kill()
            del self
            return

    def off_screen(self):
        return self.rect.y > Screen_y + 20


class Sa(pygame.sprite.Sprite):
    def __init__(self, root):
        self.game = root
        self.image = pygame.image.load('나는 탱크를 잘못 만든다는 진실에 도달할수 없다.png').convert_alpha()
        self.image_l = pygame.transform.scale(self.image, (200,200))
        self.image_r = pygame.transform.flip(self.image, True, False)
        self.image = self.image_l
        self.rect = self.image.get_rect()
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.angle = 0
        self.mask = pygame.mask.from_surface(self.image)
        self.pos = pygame.math.Vector2(Screen_x/2,Screen_y *8 /10)
        self.health = 100


    def update(self):
        if self.health < 5:
            self.health = 100
        self.rect = self.image.get_rect()
        if self.game.pressed_key[pygame.K_RIGHT]:
            self.pos.x += 5
            self.image = self.image_r
        if self.game.pressed_key[pygame.K_LEFT]:
            self.pos.x -= 5
            self.image = self.image_l


        if self.pos.x > Screen_x:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = Screen_x
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
        self.rains = pygame.sprite.Group()
        self.ui = pygame.sprite.GroupSingle()
        self.ui.add(Ui(self))
        self.bg = pygame.image.load('BG.png').convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (Screen_x, Screen_y))
        self.camera = vec(0, 0)
        self.bgcamera = vec(0, 0)
        self.hit_sound = pygame.mixer.Sound('Collect.wav')
        pygame.mixer.music.load('Garden (1).mp3')

    def run(self):
        pygame.mixer.music.play(-1)
        while self.playing:
            self.clock.tick(90)
            self.event()
            self.update()
            self.draw()
            pygame.display.update()

    def event(self):
        self.pressed_key = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
        self.rains.add(Rain(random.randint(0, Screen_x) , 100, self))


    def update(self):
        self.all_sprites.update()
        self.ui.update()
        if Screen_x / 8 * 2 > self.sa.pos.x:
            self.camera.x = -10
        elif Screen_x * 6 / 8 < self.sa.pos.x:
            self.camera.x = 10
        else:
            self.camera.x = 0
        for sprite in self.all_sprites:
            sprite.pos.x -= self.camera.x
        self.bgcamera += self.camera



    def draw(self):
        self.screen.fill((255, 255, 255))
        for n in range(5):
            self.screen.blit(self.bg, (Screen_x * (n - 2) - self.bgcamera.x, 0))
        self.all_sprites.draw(self.screen)
        self.ui.draw(self.screen)




game = Game()
game.run()
pygame.QUIT()