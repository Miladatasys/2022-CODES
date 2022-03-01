
#SIMPLE SNAKE GAME 

import pygame
import time
import random

#INIT PYGAME (INITIALIZATION)
pygame.init()

#DEFINE COLORS
#RGB MAX- MIN
#white = snakecolor
#black = background 
#red   = overmessage
#orange= foodchasing

white       = (255, 255, 255)
black       = (0, 0, 0)
red         = (255, 0, 0)
orange      = (255, 165, 0)
green_snake = (108, 187,60)

#DIMENSIONS

width, height = 600, 400 

#SETUP DISPLAY 
#SET   MODE
#SETUP TITILE
game_display = pygame.display.set_mode((width, height)) 
pygame.display.set_caption("Snake Pet Game")

#TIME RUNNING

clock = pygame.time.Clock()

#SNAKE MODS

snake_size   = 10

snake_speed  = 15

#FONT FOR MESSAGE

message_font = pygame.font.SysFont('ubuntu', 30 )

#FONT FOR SCORE

score_font   = pygame.font.SysFont('ubuntu', 25)

#DEFINE (DEF) TWO BASICS FUNCTIONS, UPDATING FUNCTIONS

def print_score(score):
    text     = score_font.render("Score: " + str(score), True, orange)
    game_display.blit(text, [5, 1])
    
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, green_snake, [pixel[0], pixel[1], snake_size, snake_size])
    

#RUN GAME FUNCTIONS (main function, dimension, game start, snake pixels in a list because is going to grow, target food, floating point), WITH VARIABLES

def run_game():
    
    game_over  = False
    game_close = False
    
    x = width  / 2
    y = height / 2
    
    x_speed = 0
    y_speed = 0
    
    snake_pixels = []
    snake_lenght = 1
    
    # THE POSITION ON THE TARGET IS RANDOM, STARTING WITH 0 AND IT'S GOING TO GO WITH MINUS SIZE
    
    target_x = round(random.randrange(0, width-snake_size)  / 10.0) * 10.0
    target_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0
    
    #MAIN GAME LOOP, game over on the screen inside of the game loop, restart the game
    
    while not game_over:
        
        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Game Over!", True, red)
            game_display.blit(game_over_message, [width / 3, height / 3])
            print_score(snake_lenght - 1)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type      == pygame.KEYDOWN:
                    if event.key   == pygame.K_1:
                        game_over  =  True
                        game_close  = False
                    if event.key   == pygame.K_2:
                        run_game()
                
                #alternative 
                
                if event.type      == pygame.QUIT:
                    game_over  =  True
                    game_over  =  False
                            
            
                
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game_over = True
            
            if event.type    == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT :
                    x_speed  =  -snake_size
                    y_speed  =  0
                if event.key == pygame.K_RIGHT:
                    x_speed  =  snake_size
                    y_speed  =  0
                if event.key == pygame.K_UP:
                    x_speed  =  0
                    y_speed  =  -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed  =  0
                    y_speed  = snake_size 

        #if we hit the bounderies, out of the screen we have to close the game as well
        
        if x >= width or x < 0 or y >= height or y < 0: 
            game_close = True
        
        #we need to advance, depending of the speed (MOVEMENT)
        
        x += x_speed
        y += y_speed
        
        #SET THE BACKGROUND, THE BASIC TARGET  (BACKGROUND) UPDATE THE SNAKE(REMOVE-INCREASE BY ACOMPLISH TARGET)
        
        game_display.fill(black)  
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])
        
        snake_pixels.append([x, y])
        
        if len(snake_pixels) > snake_lenght:
            del snake_pixels[0]
        
        for pixel in snake_pixels[: - 1]:
            if pixel       == [x, y]:
                game_close = True
        
        draw_snake(snake_size, snake_pixels)
        print_score(snake_lenght - 1)
        
        pygame.display.update()
        
        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width-snake_size)  / 10.0) * 10.0
            target_y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0
            snake_lenght += 1 
            
        clock.tick(snake_speed)
    
    #game over
    
    pygame.quit()
    quit()
    
run_game()
        