#importamos a lib youtube_dl
import youtube_dl as yt
#criação do metodo get_mp3
def get_mp3():
    #extraindo as informaçoes do video e guardando na variavel video_info
    video_info=yt.YoutubeDL().extract_info(url=input("insira a url do video"),download=True )

    options={'format':'bestaudio/best','keepvideo':True,'outtmpl':f"{video_info['title']}.mp3"}

    with yt.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

get_mp3()