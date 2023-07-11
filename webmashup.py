from pytube import Search,YouTube
from moviepy import editor as mp
from moviepy.editor import AudioFileClip,concatenate_audioclips
import os
# from pydub import AudioSegment

def mashup(singer,count,duration,outputFile):
    s = Search(singer)
    list = []
    while len(s.results)<count :
        s.get_next_results()

    for v in s.results:
        list.append(v.watch_url)
    list = list[0:count]
    print(len(list))


    path = '.'
    for v in list:
        try:
            yt = YouTube(v)
        except:
            print('Connection Error when initialising url')
        try :
            yt.streams.filter(progressive=True,).first().download(output_path=path)
        except:
            print('Cant download video')
        print(yt.title)
    print('Download Completed')

    files = os.listdir('.')
    print(files)

    for f in files :
        if '.3gpp' in f:
            try :
                v = mp.VideoFileClip(f)
                audioFile = os.path.splitext(os.path.basename(f))[0]
                v.audio.write_audiofile(audioFile+'.mp3')
                print(v)
            except :
                print('Cant convert video to audio')
        # print('Converted to Audio')

    for f in files :
        if '.mp3' in f:
            try :
                    audio = AudioFileClip(f)
                    clip = audio.subclip(5,duration+5)
                    clip.write_audiofile(f)
            except:
                print('Cant trim audio')

    audioClips = []
    try:
        for af in files :
                if '.mp3' in af:
                    audioClips.append(AudioFileClip(af))

        finalClip = concatenate_audioclips(audioClips)
        finalClip.write_audiofile(outputFile)
    except:
        print('cant merge audio')

    print('Done !!')


# mashup('ice spice',5,10,'mashup.mp3')