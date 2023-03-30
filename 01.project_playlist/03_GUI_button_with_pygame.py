import pygame

''' Tạo class 
làm mấy cái nút để chọn bài
'''
class TextButton():
	
	def __init__(self,text, position):
		self.text = text
		self.position = position
	
	def is_mouse_on_text(self):
		mouse_x , mouse_y = pygame.mouse.get_pos()
		if (mouse_x > self.position[0] and mouse_x < self.position[0]+ self.text_box[2]\
      and mouse_y > self.position[1] and mouse_y < self.position[1]+ self.text_box[3]):
			pygame.draw.line(screen, BLUE,(self.position[0], self.position[1]+ self.text_box[3]),\
		    (self.position[0]+ self.text_box[2], self.position[1]+ self.text_box[3]))
			return True
		return False
		

	def draw(self):
		font = pygame.font.SysFont('sans', 30)
		text_render = font.render(self.text, True, BLACK)
		self.text_box = text_render.get_rect()
		if self.is_mouse_on_text():
			text_render = font.render(self.text, True, BLUE) # make color
			pygame.draw.rect(screen, WHITE, (self.position[0],\
				   self.position[1], self.text_box[2],self.text_box[3]))# Draw line
		else:
			text_render = font.render(self.text, True, BLACK)
		self.text_box = text_render.get_rect()
		
		screen.blit(text_render, self.position)  # draw text


		


pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame App')
running = True
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
clock = pygame.time.Clock()
random_button = TextButton('chinhnghiep', (50,50))
while running:		
	clock.tick(60)
	screen.fill(WHITE)

	
	random_button.draw()
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				if random_button.is_mouse_on_text():
					print("Button pressed")
		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()