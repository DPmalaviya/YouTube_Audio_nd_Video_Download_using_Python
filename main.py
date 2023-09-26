import pytube
from sys import argv
import os

link = argv[1]
YT = pytube.YouTube(link)
decision = argv[2]
title_youtube = YT.title.title()
print(title_youtube)

Video_filepath = 'DataBase\\Audio'
Audio_filepath = 'DataBase\\Audio'

if decision == str(1):
    print('Audio encoding started...')
    # audio = YT.streams.get_audio_only()
    audio = YT.streams.filter(only_audio=True, abr="160kbps").first()
    audio.download(Audio_filepath)

elif decision == str(2):
    print('Audio encoding started...')
    # audio = YT.streams.get_audio_only()
    audio = YT.streams.filter(only_audio=True, abr="160kbps").first()
    audio.download(Audio_filepath)
    
    print("Video encoding started...")
    video = YT.streams.filter(res="1080p").first()
    video.download(Video_filepath)

    import moviepy.editor as mpe

    for video_filename in os.listdir(Video_filepath):
        for audio_filename in os.listdir(Audio_filepath):
            if video_filename[:8] == audio_filename[:8]:
                if title_youtube[:5] == video_filename[:5]:
                    full_path_video = Video_filepath + '\\' + video_filename
                    full_path_audio = Audio_filepath + '\\' + audio_filename
                    video_clip = mpe.VideoFileClip(full_path_video)
                    audio_clip = mpe.AudioFileClip(full_path_audio)
                    final_clip = video_clip.set_audio(audio_clip)

                    final_clip.write_videofile(f"DataBase\\Video\\{video_filename}")
                    os.remove(full_path_video)
                    os.remove(full_path_audio)
                else:
                    print("File not be Found.")    

else:
    print('Please Enter 1 or 2\nTo Identify Audio Or Video Respectivly')
    print('You should Type(for Audio):\npython main.py "https://www.youtube.com/watch?v=suk3mW0tDPA&pp=ygUJa2ZnMiBzb25n" 1')