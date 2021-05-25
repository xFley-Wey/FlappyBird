import pygame

def load_image(path):
    image = pygame.image.load(path)

class bird(pygame.sprite.Sprite):
    def __init__(self, center, win_sizes ):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('/Users/user/Desktop/bird.png')
        transparent_color = self.image.get_at((0,0))
        self.image.set_colorkey(transparent_color)
        self.rect = self.image.get_rect()
        self.rect.center1, self.rect.center2 = center 
        self.speed1, self.speed2 = 0, 0
        self.win_size = win_size
        self.flying = False
    def update(self):
        if self.flying:
            self.speed2 += 1
            if self.speed2 > 13:
                self.speed2 = 13
            if self.rect.bottom < self.win_size[1]: 
                self.rect2 += self.speed2
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.flying = True
            self.speed2 = 2

class truba(pygame.sprite.Sprite):
    def __init__(self, image, win_size, vertex, height=200):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('/Users/user/Desktop/truba.png')
        image = pygame.transform.scale(image, (50, height))
        self.image = image
        transparent_color = self.image.get_at((0,0))
        self.image.set_colorkey(transparent_color)
        self.rect = self.image.get_rect()
        if vertex:
            self.rect.vertex = 0
        else:
            self.rect.bottom = win_size[1]
        self.rect1 = win_size[0]

        self.speed = speed
    def update(self):
        self.rect1 -= self.speed
        if self.rect.right < 0:
            self.disappearance()

class background(pygame.sprite.Sprite):
    self.image = load_image('/Users/user/Desktop/background.png')