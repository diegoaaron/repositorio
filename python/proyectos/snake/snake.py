import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 800
dis_height = 400

dis = pygame.display.set_mode([dis_width, dis_height])
pygame.display.set_caption('Gusanito, por Diego')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Your Score: ", str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list): # dibuja el gusano
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block]) # Rect(left, top, width, height) -> Rect

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, 790))
    foody = round(random.randrange(0, 390))

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message('Perdiste, Q (Salir) o C (Nuevo juego)', red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0

                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: # salir del mapa
            game_over = True
          
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue) # define el fondo en azul

        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) # dibuja un rectangulo verde de 10 x 10 en la posicion foodx, foody
        
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        
        print(snake_Head, snake_List, len(snake_List))
        
        snake_List.append(snake_Head)

        if len(snake_List) > Length_of_snake: # ¿Porque si el tamaño de lista es mas grande que los puntos atrapados se elimina el primer elemento de la lista
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, 790))
            foody = round(random.randrange(0, 390))
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
