import pygame

pygame.init()

screen_width=700
screen_height=400
screen=pygame.display.set_mode([screen_width, screen_height])

white = (255, 255, 255)
blue = (50, 153, 213)

#pygame.draw.rect(screen, white, [500, 200, 20, 20]) # Rect(left, top, width, height) -> Rect

game_over = False

while not game_over:
    screen.fill(blue)
    pygame.draw.rect(screen, white, [0, 0, 20, 20]) # Rect(left, top, width, height) -> Rect

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            game_over = True
    
    pygame.display.update() # actualiza la porción 

pygame.quit()

# 