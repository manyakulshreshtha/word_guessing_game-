import pygame 
from sys import exit 
pygame.init()
scwidth=800
scheight=600
screen=pygame.display.set_mode((scwidth,scheight))
test_surface=pygame.Surface((100,200))
test_surface2=pygame.Surface((10,10))
#img_surface=pygame.image.load('graphics/abc.png')
test_surface.fill('Red')
test_surface2.fill('Yellow')
test_font=pygame.font.Font("font\Pixel Game.otf", 50)
clock=pygame.time.Clock()
text_surface=test_font.render('hangman',False,'Green')
test_surface2_xpos=600
while True :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit 
    screen.blit(test_surface,(200,100))
    screen.blit(text_surface,(300,400))
    test_surface2_xpos-=4
    if test_surface2_xpos<-100: test_surface2_xpos=800
    screen.blit(test_surface2,(test_surface2_xpos,0))
    #screen.blit(img_surface,(0,0))
    pygame.display.update()
    clock.tick(60)
