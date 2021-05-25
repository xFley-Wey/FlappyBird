import pygame
pygame.init()

win_size = 700
win = pygame.display.set_mode((win_size,win_size))
background_color = (255,255,255)
font0 = pygame.font.SysFont('arial', 64)
red = (255,0,0)
def draw_text(text, font, color, frame, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x,y)
    frame.blit(textobj, textrect)  

menu_color = (0,0,0)
def menu(win):
    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        win.fill(menu_color)
        draw_text('Menu', font0, red, win, 320, 320)
        pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu(win)

    win.fill(background_color)
    #code

    pygame.display.update()