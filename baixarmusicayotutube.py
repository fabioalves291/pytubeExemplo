from pytube import YouTube, Playlist
import os

yt = str(input('URL da sua playlist: '))
playlist = Playlist(yt);print(playlist)
print('há '+str(len(playlist))+' musicas na sua lista')
for url in playlist:
    audio = YouTube(url)
    audio = audio.streams.filter(only_audio=True)[0]
    destination = '.'
    out_file = audio.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    
