'''
Viết chương trình đoc danh sách video

class Video
    seft.tittle
    seft.link
def read_video  : nhờ nhập 1 video, có tittle và link chua video do
def read_videos : nhap nhieu video va chua video do
def print_video 
def print_videos
def wrire_video : ghi 1 video
def wrive_to_file:  ghi nhiều video tận dụng hàm trên

VL2:
Tạo thành cái Playlist

Class Playlist(năm,description,rating,videos)


'''
class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link

class Playlist:
    def __init__(self, name, description, rating,videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

def read_video():
    title_video = input ("Enter title: ")
    link_video = input ("Enter link video: ")
    video = Video(title_video, link_video)
    return video

def read_videos():
    videos = []
    total_video = int(input("Nhap so luong video "))
    for i in range(total_video):
        print("Enter video: ", i+1)
        vid = read_video()
        videos.append(vid)
    return videos

def print_video(video):
    print("Video title: ", video.title, end='')
    print("Video link: ", video.link, end='')
    
def print_videos (videos):
    for i in range(len(videos)):
        print_video(videos[i])

def write_video(videos, file):
    file.write(videos.title + '\n')
    file.write(videos.link + '\n')

def write_videos(videos, file):
    total_video = len(videos)
    file.write(str(total_video)+ '\n')
    for i in range(total_video):
        write_video(videos[i], file)

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

## READ PLAYLIST
'''nhap thong tin playlist do'''
def read_playlist():
    playlist_name = input("Enter playlist name: ")
    playlist_description= input("Enter playlist description: ")
    playlist_rating = input("Enter rating(1-5): ")
    playlist_videos = read_videos()
    playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
    return playlist

def write_playlist_txt(playlist):
    with open("data.txt", 'w') as file:
        file.write(playlist.name + '\n')
        file.write(playlist.description + '\n')
        file.write(playlist.rating + '\n')
        write_videos(playlist.videos, file)
    print("Successfully write playlist to txt")

def read_playlist_from_txt():
    with open ("data.txt", 'r') as file:
        playlist_name = file.readline()
        playlist_description = file.readline()
        playlist_rating = file.readline()
        playlist_videos = read_videos_file(file)
    playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
    return playlist

def print_playlist(playlist):
    print('------')
    print("Playlist name: " + playlist.name , end='')
    print("Playlist description: " + playlist.description , end='')
    print("Playlist rating: " + playlist.rating , end='')
    print_videos(playlist.videos)

def main():
    playlist = read_playlist()
    write_playlist_txt(playlist)
    playlist = read_playlist_from_txt()
    print_playlist(playlist)

main()