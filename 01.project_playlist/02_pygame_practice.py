import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption('Flappy Bird')
running = True
GREEN = (100, 200, 0)
RED = (255,0,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)

clock = pygame.time.Clock()
circle_color = RED

font = pygame.font.SysFont('sans', 30)

#vẽ chữ
text = font.render('Random',True, BLACK)

#hỗ trợ vị trí  chữ
text_box = text.get_rect()

random_pos = (50,50)

while running:		
	clock.tick(60)
	screen.fill(WHITE)

	mouse_x, mouse_y = pygame.mouse.get_pos()		
	#draw retangle
	pygame.draw.rect(screen,WHITE,(random_pos[0],random_pos[1],text_box[2],text_box[3]))

	#draw text
	screen.blit(text, random_pos)

	#draw circle
	pygame.draw.circle(screen, circle_color, (200,200), 50)
	
	#kiểm tra trỏ chuột vào text đổi màu text
	if ((mouse_x > random_pos[0]) and (mouse_x < random_pos[0]+ text_box[2])\
     and (mouse_y > random_pos[1]) and (mouse_y < random_pos[1] + text_box[3])):
		text = font.render('Random',True, BLUE)
		pygame.draw.line(screen, BLUE, (random_pos[0], random_pos[1]+ text_box[3])\
		   ,(random_pos[0]+ text_box[2], random_pos[1] + text_box[3]))
	else:
		text = font.render('Random',True, BLACK)

	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if ((50 < mouse_x <100) and (50 < mouse_y< 100)):
					circle_color = (randint(0,255),randint(0,255),randint(0,255))
					print("Right click on red retangle")

		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()
