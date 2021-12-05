import youtube_dl

#links = "https://www.youtube.com/watch?v=UwzzkBTswJg"
links='https://drive.google.com/file/d/1SdS3sm4AriVHfnEcc4gAG_VJ8FHjNoxC/view'
options = {
'format': '136',
#'ignore-errors': True,

'outtmpl': '{0}%(title)s-%(id)s.%(ext)s',
}
with youtube_dl.YoutubeDL(options) as youtube_object:
    meta = youtube_object.extract_info(links, download = True)
       
print(meta["abr"])  