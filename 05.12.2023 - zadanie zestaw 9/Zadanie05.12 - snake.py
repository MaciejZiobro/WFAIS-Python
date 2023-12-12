# W grze strujmey strzałkami
# Śmierć następuje przy kolizji ze samym sobą lub po zjedzeniu 3 trujących owoców - niebieksi licznik
# Każdy pożywny owoc (czerwony) wydłuża węża oraz zwiększa wynik o 1
# Wraz z wzrostem wyniku prędkość węża zwiększa się oraz odległość miedyz owocem trującym i pożywnym się zmniejsza cop utrudnia gre


import sys, pygame, random, math, time

black = (0, 0, 0)
gray = (128, 128, 128)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

FPS = 60  
clock = pygame.time.Clock()

pygame.init()
size = (width, height) = (800, 600)   
screen = pygame.display.set_mode(size)   
pygame.display.set_caption('Snake')

current_dir = False # False - poziomo, True pionowo
speed0 = 5 # Odpowiendio + lub - definiują zwrot
speed = speed0
speed_const = 10
snake_size = 1
snake_bodySize = 15
snake_pos = [50, 50]
snake_body = [[100,50], [85,50], [70,50], [55,50], [40,50]]
death_counter = 0
fruit_flag = False
frame_nr = 0
pfruit_flag = False

font = pygame.font.Font(None, 60)
fontp = pygame.font.Font(None, 40)
font_end = pygame.font.Font(None, 150)
score = 0



done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit(0)
        # Sterowanie klawiatura
        elif event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP:
                current_dir = True
                speed = -abs(speed0 + (score/speed_const))
            elif event.key == pygame.K_DOWN:
                current_dir = True
                speed = abs(speed0+(score/speed_const))
            elif event.key == pygame.K_LEFT:
                current_dir = False
                speed = -abs(speed0+(score/speed_const))
            elif event.key == pygame.K_RIGHT:
                current_dir = False
                speed = abs(speed0+(score/speed_const))
    

    
    
    snake_pos[0] += speed*int(not current_dir)
    snake_pos[1] += speed*int(current_dir)
    snake_body.insert(0, [snake_pos[0], snake_pos[1]])
    
    frame_nr += 1
    collide_const = 3
    screen.fill(black)
    
    # Narysowanie snake
    for part in snake_body:
        sq = pygame.Rect(part[0], part[1], snake_bodySize, snake_bodySize)
        pygame.draw.rect(screen, green, sq)
    
    # Spawn owocu
    if not fruit_flag:
        x = random.uniform(40, width-40)
        y = random.uniform(40, height-40)
        fruit = pygame.Rect(x, y, snake_bodySize, snake_bodySize)
        xp = min(max(random.uniform(x-150+2.5*score, x+150-2.5*score), 25), width -25)
        yp = min(max(random.uniform(y-125+2*score, y+125-2*score), 20), height-20)
        pfruit = pygame.Rect(xp, yp, snake_bodySize, snake_bodySize)
        fruit_flag = True
        pygame.draw.rect(screen, red, fruit)
        pygame.draw.rect(screen, blue, pfruit)
        
    else:
        pygame.draw.rect(screen, red, fruit)
        pygame.draw.rect(screen, blue, pfruit)
        
    head = pygame.Rect(snake_body[0][0], snake_body[0][1], snake_bodySize, snake_bodySize)
    if head.colliderect(fruit):
        score += 1
        fruit_flag = False
    else:
        snake_body.pop()
        
    if head.colliderect(pfruit):
        score -= 1
        fruit_flag = False
        snake_body.pop()
        death_counter += 1
    else: pass

    # granice zapętlone
    if snake_pos[0] > width:
        snake_pos[0] = 0
    if snake_pos[0] < 0:
        snake_pos[0] = width - 5
    if snake_pos[1] > height:
        snake_pos[1] = 0
    if snake_pos[1] < 0:
        snake_pos[1] = height - 5
    
        
    # Score printing
    text_score = str(score)
    score_surf = font.render(text_score, True, white)
    text_rect = score_surf.get_rect(center=(width -40, 40))
    screen.blit(score_surf, text_rect)
    
    text_death = str(death_counter)
    sdeath_surf = fontp.render(text_death, True, blue)
    text_rect2 = sdeath_surf.get_rect(center=(width -40, 80))
    screen.blit(sdeath_surf, text_rect2)
    
    pygame.display.flip()
    clock.tick(FPS)
    
    # warunki końca gry
    if death_counter >= 3:
        done = True
    for i in snake_body:
        for y in snake_body:
            if i!=y and frame_nr>30:
                rect1 = pygame.Rect(i[0], i[1], snake_bodySize, snake_bodySize)
                rect2 = pygame.Rect(y[0], y[1], snake_bodySize, snake_bodySize)
                
                if y[0] - collide_const <= i[0] and i[0] <= y[0] + collide_const and y[1] - collide_const <= i[1] and i[1] <= y[1] + collide_const:
                    done = True


end_score = "Game Over"
end_surf = font_end.render(end_score, True, red)
text_rect3 = end_surf.get_rect(center=(width/2, height/2))
screen.blit(end_surf, text_rect3)
pygame.display.flip()
time.sleep(5)    
             
pygame.quit()


