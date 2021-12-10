from flask import Flask, render_template, request, redirect
from controllers import select_format


app = Flask(__name__, template_folder = './templates' , static_folder = './templates' )


@app.route("/")
def download():
    return render_template("index.html",videoId=" ")


@app.get('/star_download')
def info_video():
    url=request.args.get("url")
    videoId = url.replace("https://www.youtube.com/watch?v=","")
    response = select_format.verifyFormat(
        links=videoId,
    )
    return render_template("index.html",videoId=videoId,url=url)
#recibiendo eventos de descarga
@app.get('/descargar-video')
def calidad_128():

    url = request.args.get("url")
    videoId = url.replace("https://www.youtube.com/watch?v=","")

    return select_format.select_download(link=videoId,calidad="128")

@app.get('/descargar-video_190')
def calidad_190():
    url = request.args.get("url")
    videoId = url.replace("https://www.youtube.com/watch?v=", "")
    select_format.select_download(link=videoId,calidad="190")

@app.get('/descargar-video_320')
def calidad_320():
    url = request.args.get("url")
    videoId = url.replace("https://www.youtube.com/watch?v=", "")
    return select_format.select_download(link=videoId,calidad="320")

#video
@app.get('/descargar-video_480')
def calidad_480():
    calidad="480p"
    url = request.args.get("url")
    videoId = url.replace("https://www.youtube.com/watch?v=", "")
    print(videoId)
    select_format.select_download(link=videoId, calidad=calidad)
@app.get('/descargar-video_720')
def calidad_720():
    url = request.args.get("url")
    videoId = url.replace("https://www.youtube.com/watch?v=", "")
    return select_format.select_download(link=videoId,calidad="720p")

@app.get('/descargar-video_1080')
def calidad_1080():
    url = request.args.get("url")
    videoId = url.replace("https://www.youtube.com/watch?v=", "")
    return select_format.select_download(link=videoId,calidad="1080p")





'''
@app.post('/star_download')
def start_download():
    video = request.form
    
    response = select_format.verifyFormat(
        links=video["enlace"],
    )
    return redirect('/')'''


app.run(debug=True)
