'''
/************************************
File Name : creeps_game.py

Author : Varoon Pazhyanur 

Date Created : 01-28-2017

Last Modified : Sat 28 Jan 2017 11:54:25 PM EST


/************************************
'''

#CREEP CLASS
class Creep(Sprite):
    #a creep sprite that bounces off walls and changes its direction periodically

    #the screen is a pygame Surface object, img_filename describes where to find im, position is a 2d vector, direction is a 2d vector with an angle that is a multiple of 45 degrees and speed is in pixels/millisecond
    def __init__(self, screen, img_filename, init_position, init_direction, speed):
        #NOTE that the top left is (0,0) and y increases downwards
        
#Game params
SCREEN_WIDTH, SCREEN_HEIGHT = 400,500
BG_COLOR = 150,150,80

CREEP_FILENAMES=[
    'bluecreep.png',
    'pinkcreep.png',
    'graycreep.png']

N_CREEPS = 20
#create creeps
creeps = []
for i in range(0,N_CREEPS):
    creeps.append(Creep(screen,choice(CREEP_FILENAMES),
        (randint(0,SCREEN_WIDTH),randint(0,SCREEN<HEIGHT),
        (choice([-1,1]),choice([-1,1]),0.1))


#main game loop
while True:
    #limits frame rate to 50 FPS
    time_passed = clock.tick(50)
    
    for event in pygame.event.get()
    if event.type == pygame.QUIT:
        exit_game()
    
    #redraw background
    screen.fill(BG_COLOR)
    
    #update and redraw all creeps
    for creep in creeps:
        creep.update(time_passed)
        creep.blitme()

    pygame.display.flip()
