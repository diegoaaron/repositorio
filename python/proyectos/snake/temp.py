import pygame

pygame.init()

screen_width=700
screen_height=400
screen = pygame.display.set_mode([screen_width, screen_height])

white = (255, 255, 255)
blue = (50, 153, 213)
black = (0, 0, 0)
#pygame.draw.rect(screen, white, [500, 200, 20, 20]) # Rect(left, top, width, height) -> Rect

game_over = False

score_font = pygame.font.SysFont("comicsansms", 35) # objeto que brinda una fuente
yellow = (255, 255, 102)
def Your_score(score): # funcion para mostrar el puntuja
    value = score_font.render(f"Your Score: {score}", True, yellow)
    screen.blit(value, [0, 0])


def our_snake(snake_block, snake_list): # dibuja el gusano
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block]) # Rect(left, top, width, height) -> Rect - dibuja el gusano

while not game_over:
    screen.fill(blue)
    pygame.draw.rect(screen, white, [0, 0, 20, 20]) # Rect(left, top, width, height) -> Rect

    for event in pygame.event.get():
        print(event, "---", event.type)
        if event.type == pygame.QUIT:
            game_over = True

    Your_score(event)

    our_snake(10, [[350,100],[350,110], [350,120],[350,130]])

    pygame.display.update() # actualiza el lienzo

pygame.quit()



# 