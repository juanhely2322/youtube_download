
import youtube_dl
from models import fomats_selection
video = []
music=[]
def verifyFormat(links):
    link = ("https://www.youtube.com/watch?v={}".format(links))
    print(link)
    calidades= youtube_dl.YoutubeDL().extract_info(link, download=False)
    formatos=calidades.get("formats",[calidades])

    for f in formatos:


        #print(f["format"])
        if f["format_note"] == "tiny":
            mp3 = {
                'formato': f["format_note"],
                'peso': f["filesize"],
                "id": f["format_id"],

            }
            music.append(mp3)

        if f["ext"] == "mp4" :
            mp4={
                'formato': f["format_note"],
                'peso': f["filesize"],
                "ext":f["ext"],
                "id":f["format_id"],

            }
            video.append(mp4)






def select_download(link,calidad):

    for v in video:

        if (v["formato"] == "480p" and v["ext"] == "mp4")and calidad=="480p":
            print(v)
            return fomats_selection.descarga(id=v["id"],link=link)

        if (v["formato"] == "720p" and v["ext"] == "mp4")and calidad=="720p":
            print(v)
            return fomats_selection.descarga(id=v["id"],link=link)
        if (v["formato"] == "1080p" and v["ext"] == "mp4")and calidad=="1080p":
            print(v)
            return fomats_selection.descarga(id=v["id"],link=link)

    #########musica
    if  calidad == "128":
            return fomats_selection.descarga_audio(calidad=calidad,id=link)

    if calidad == "190":
        return fomats_selection.descarga_audio(calidad=calidad,id=link)
    if calidad == "320":
        return fomats_selection.descarga_audio(calidad=calidad,id=link)













