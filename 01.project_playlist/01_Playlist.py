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
    title_video = input ("Enter title: ") + "\n"
    link_video = input ("Enter link video: ") + "\n"
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
    file.write(videos.title)
    file.write(videos.link)

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
    playlist_name = input("Enter playlist name: ") + "\n"
    playlist_description= input("Enter playlist description: ") + "\n"
    playlist_rating = input("Enter rating(1-5): ") + "\n"
    playlist_videos = read_videos()
    playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
    return playlist

def write_playlist_txt(playlist):
    with open("data.txt", 'w') as file:
        file.write(playlist.name)
        file.write(playlist.description)
        file.write(playlist.rating)
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

# Check digit input
def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min \
        or int(choice)> max:
        print(' (-) Wrong input,  follow description ')
        choice = input(prompt)
    choice = int(choice)
    return choice


# Menu
def show_menu():
    print("------------MENU--------------")
    print("|Option 1: Create playlist   |")
    print("|Option 2: Show playlist     |")
    print("|Option 3: Play a video      |")
    print("|Option 7: Save and Exit     |")
    print("------------------------------")


# play video
def play_video(playlist):
    print("\n Video 's " + playlist.name)
    print_videos(playlist.videos)
    total = len (playlist.videos)

    choice = select_in_range("Select a video (1," \
                             + str(total)+ "): ", 1, total)
    print("Open video: " + playlist.videos[choice-1].title \
          + " - " + playlist.videos[choice-1].link , end = '')

def main():
    
    try:
        playlist = read_playlist_from_txt()
        print("Load data success!")
    except:
        print('Wellcome first user !!!')
    
    while True:
        show_menu()
        choice = select_in_range("Select choice 1->7:  ", 1, 7)
        if choice ==1:
            playlist = read_playlist()
            input("\nPress Enter to continue.\n")	
        elif choice == 2:
            print_playlist(playlist)
            input("\nPress Enter to continue.\n")
        elif choice == 3:
            play_video(playlist)
            input("\nPress Enter to continue.\n")
        elif choice == 7:
            write_playlist_txt(playlist)
            break
        else:
            print("Wrong input, ")
            break

main()