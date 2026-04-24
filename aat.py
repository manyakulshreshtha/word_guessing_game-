import random
import pygame 
import pygame_gui 
import string 
from sys import exit 
pygame.init()
scwidth=1024
scheight=1024
screen=pygame.display.set_mode((scwidth,scheight))
background=pygame.image.load("graphics/back.png")
floor=pygame.image.load("graphics/floor.png")
test_font=pygame.font.Font("font\Pixel Game.otf", 70)
title_font=pygame.font.Font("font\\Pixel Game.otf",55)
word_font=pygame.font.Font("font\\Pixel Game.otf",90)
title_surface=title_font.render('GUESS THE WORD AND SAVE THE WIZARD', False, 'lavender')
enter_word=title_font.render('enter guess: ',False,'lavender')
clock=pygame.time.Clock()
lives=[]
for i in range(6):
    life=pygame.image.load("graphics/live"+str(i)+".png")
    lives.append(life)
life_img=lives[5]
correct=[]
for j in range(7):
    right=pygame.image.load("graphics/right"+str(j+1)+".png")
    correct.append(right)
wiz_img=pygame.image.load("graphics/smoke.png")
word_list=['hexagon','victory','wizards','crystal',
           'journey','charmed','spellman','talisman']
word= random.choice(word_list)
display_text=['_' for _ in word ]
input_box=pygame.Rect(800,680,70,70)
assembled=0
live_count=5
win_count=0
guessed=[]
user_letter=''
active=True 
win_msg =test_font.render('You win! :) ', False, 'lavender')
lose_msg=test_font.render('you lose :(',False,'lavender')
game_over=False
while True : 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = True
            else:
                active = False
        if not game_over:
            if event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_RETURN:
                    if user_letter and len(user_letter) == 1 and user_letter in string.ascii_lowercase:
                        letter = user_letter
                        user_letter = ''
                        active = False

                        if letter in guessed:
                            continue  # ignore repeat guesses
                        guessed.append(letter)
                        if letter in word:
                            for i, char in enumerate(word):
                                if char == letter:
                                    display_text[i] = char
                                    win_count += 1
                        else:
                            live_count -= 1
                        
                        if 0 <= live_count <= 5:
                            life_img = lives[live_count]
                        if 1<= win_count <=7:
                            wiz_img=correct[win_count-1]
                    user_letter = ''
                else:
                    if len(user_letter) < 1 and event.unicode.lower() in string.ascii_lowercase:
                        user_letter = event.unicode.lower()


        if active:
            colour=pygame.Color('slateblue4')
        else:
            colour=pygame.Color('black')

    
    word_surface=title_font.render(user_letter,True,'lavender')
    display_surface=word_font.render(' '.join(display_text),False,'lavender')
    screen.blit(background,(0,0))
    screen.blit(floor,(0,0))
    screen.blit(life_img,(0,75))
    screen.blit(wiz_img,(400,120))
    screen.blit(title_surface,(160,100))
    screen.blit(enter_word,(500,700))
    screen.blit(display_surface,(300,800))
    if '_' not in display_text:
        screen.blit(win_msg, (200, 400))
        game_over=True
    if live_count<=0:
        screen.blit(lose_msg, (200, 400))
        game_over=True
    pygame.draw.rect(screen,colour,input_box)
    screen.blit(word_surface,(810,700))
    pygame.display.update()
    clock.tick(60)