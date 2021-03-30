import pygame

pygame.init()

screen_width=700
screen_height=400
screen = pygame.display.set_mode([screen_width, screen_height])

white = (255, 255, 255)
blue = (50, 153, 213)

#pygame.draw.rect(screen, white, [500, 200, 20, 20]) # Rect(left, top, width, height) -> Rect

game_over = False

score_font = pygame.font.SysFont("comicsansms", 35) # objeto que brinda una fuente
yellow = (255, 255, 102)
def Your_score(score): # funcion para mostrar el puntuja
    value = score_font.render(f"Your Score: {score}", True, yellow)
    screen.blit(value, [0, 0])


while not game_over:
    screen.fill(blue)
    pygame.draw.rect(screen, white, [0, 0, 20, 20]) # Rect(left, top, width, height) -> Rect

    for event in pygame.event.get():
        print(event, "---", event.type)
        if event.type == pygame.QUIT:
            game_over = True

    Your_score(event)

    pygame.display.update() # actualiza la porción 

pygame.quit()



# 