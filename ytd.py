import os

def playlist_download():
    playlist_url = input("Enter Playlist URL:")
    if('list=' in playlist_url):
        playlist_id = playlist_url.replace("list=",">").split(">")[1]
        os.system('youtube-dl -f bestvideo+bestaudio -o "%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s" --merge-output-format mp4 -i ' + playlist_id)
    else:
        print("invalid URL")

def single_download():
    video_url = input("Enter Video URL:")
    os.system("youtube-dl -f bestvideo+bestaudio -o %(title)s.%(ext)s --merge-output-format mp4 " + video_url) 

def channel_download():
    print("channel download is coming soon!")

def batch_download():
    list_file = input("where is list file:")
    os.system(" youtube-dl -f 397+bestaudio -o %(title)s.%(ext)s --merge-output-format mp4  --batch-file=" + list_file)
     
def mp3_download():
    video_url = input("Enter Video URL:")
    os.system("youtube-dl -f bestaudio[ext=m4a] --extract-audio -o %(title)s.%(ext)s --audio-format mp3 --audio-quality 0 " + video_url) 

methods = [playlist_download, single_download, channel_download, batch_download, mp3_download]
try:
    selectMethod = int(input("Choose Download Option: \n 1. Playlist Download \n 2. Single Video Download \n 3. Channel Download \n 4. Batch Download \n 5. MP3 Download \n >>"))
    methods[selectMethod-1]()
except:
    print("No option selected!")

 
