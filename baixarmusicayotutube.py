from pytube import YouTube, Playlist
import os

#yt = str(input('URL da sua playlist: '))
yt = str('https://www.youtube.com/watch?v=peVg7MSC7lw&list=PLmhZXh0MdA7x-aWkj3pRtub9fZ1xdlqJ8')
playlist = Playlist(yt);print(playlist)
for url in playlist:
    audio = YouTube(url)
    audio = audio.streams.filter(only_audio=True)[0]
    destination = '.'
    out_file = audio.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    
    os.rename(out_file, new_file)

    
