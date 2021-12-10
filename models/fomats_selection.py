from flask import jsonify
import youtube_dl

def descarga(id,link):
    links = ("https://www.youtube.com/watch?v={}".format(link))
    ydl_opts = {
        'format': id,
        'outtmpl': './static/%(title)sf%(format_note)s.%(ext)s',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(links)

    return jsonify({
        'url': 'http://localhost:5000/static/' + links + '.mp3'})

def descarga_audio(calidad,id):
    link = str("https://www.youtube.com/watch?v={}".format(id))
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': "mp3",
            'preferredquality': calidad,
        }],
        'outtmpl': './static/' +id+ '.%(ext)s',
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:  ydl.download(link)
    return jsonify({
        'url': 'http://localhost:5000/static/' + id + '.mp3'
    })





