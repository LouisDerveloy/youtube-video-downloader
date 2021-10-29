from pytube import YouTube
import sys
import os

def get_Video(): return YouTube(sys.argv[1])

def save(video):
    video.streams.get_by_itag(22).download(output_path=sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads'), filename=video.title + ".mp4")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        video = get_Video()
        print(f"""
Title: {video.title}

Description:

{video.description}

____________________________________________________________________________________________________
Author: {video.author}
Age restriction: {video.age_restricted}
URL: {video.watch_url}
        """)
        saveOrNot = str(input("Do you want to save this video ? Y or N\n"))
        save(video) if saveOrNot == "Y" or saveOrNot == "y" else print("The video has not be saved.")