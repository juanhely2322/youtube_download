import youtube_dl

def verifyFormat(links):
    calidades= youtube_dl.YoutubeDL().extract_info(links, download=False)
    formatos=calidades.get("formats",[calidades])
    video = []
    music=[]
    for f in formatos:


        print(f["format"])
        if f["format_note"] == "tiny":
            mp3 = {
                'formato': f["format_note"],
                'peso': f["filesize"],

            }
            music.append(mp3)

        if f["ext"] == "mp4" :
            mp4={
                'formato': f["format_note"],
                'peso': f["filesize"],
                "ext":f["ext"],

            }
            video.append(mp4)
    for m in music:
       print(m)
    for v in video:
        if v["formato"]=="360p" and v["ext"]=="mp4":
            print(v)
        if v["formato"] == "1080p" and v["ext"] == "mp4":
                print(v)









