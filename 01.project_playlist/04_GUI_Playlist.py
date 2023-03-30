import pygame
import webbrowser

''' Ghep class từ Playlist
MỤC TIEU: Đọc file data Playlist lên GUI
'''


class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link
        self.seen = False
    
    def open(self):
        webbrowser.open(self.link)
        self.seen = True

class Playlist:
    def __init__(self, name, description, rating,videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

class TextButton():
	
	def __init__(self,text, position):
		self.text = text
		self.position = position
	
	def is_mouse_on_text(self):
		"""Check mouse in/out text

		Returns:
			True: Mouse in ROI text
		"""
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

#Function load data
def read_video_file(file):
    title = file.readline()
    link = file.readline()
    video = Video(title,link)
    return video

def read_videos_file(file):
    videos = []
    total = file.readline()
    for i in range(int(total)):
        video = read_video_file(file)
        videos.append(video)
    return videos

def read_playlist_from_txt(file):
	playlist_name = file.readline()
	playlist_description = file.readline()
	playlist_rating = file.readline()
	playlist_videos = read_videos_file(file)
	playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
	return playlist

def read_playlists_from_txt():
	playlists = []
	with open ("data_playlists.txt", 'r') as file:
		total = file.readline()
		for i in range (int(total)):
			playlist = read_playlist_from_txt(file)
			playlists.append(playlist)
	return playlists

		
# Load data: Data from mutiple playlists
playlists = read_playlists_from_txt()

playlists_btn_list = []
videos_btn_list = []
margin = 50 # do lech

# Tạo nút button cho playlist
for i in range (len(playlists)):
	playlists_btn = TextButton(playlists[i].name.rstrip(),(50, 50+ margin*i))
	playlists_btn_list.append(playlists_btn)


# GUI
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Pygame App')
running = True
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
clock = pygame.time.Clock()

while running:		
	clock.tick(60)
	screen.fill(WHITE)

	# draw playlists
	for i in range (len(playlists_btn_list)):
		playlists_btn_list[i].draw()

	# draw videos
	for video_button in videos_btn_list:
		video_button.draw()

	# event button
	for event in pygame.event.get():
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				for i in range(len(playlists_btn_list)):
					if playlists_btn_list[i].is_mouse_on_text():
						print("Button pressed")
						playlist_choice = i
						videos_btn_list = []
						for j in range (len(playlists[i].videos)):
							video_btn = TextButton(str(j+1) + '. '+ playlists[i].videos[j].title.rstrip(),(250, 50+ margin*j))
							videos_btn_list.append(video_btn)

				#play videos	
				if playlist_choice != None:
					for i in range(len(videos_btn_list)):
						if videos_btn_list[i].is_mouse_on_text():
							playlists[playlist_choice].videos[i].open()

		if event.type == pygame.QUIT:
			running = False
				
	pygame.display.flip()

pygame.quit()