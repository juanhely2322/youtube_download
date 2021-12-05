from flask import Flask, render_template, request, redirect
from controllers import select_format

app = Flask(__name__, template_folder = './templates' , static_folder = './templates' )


@app.route("/")
def download():
    return render_template("index.html")


@app.post('/star_download')
def start_download():
    video = request.form
    response = select_format.verifyFormat(
        links=video["enlace"],
    )
    return redirect('/')


app.run(debug=True)
