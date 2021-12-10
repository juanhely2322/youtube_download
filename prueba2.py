import youtube_dl

links = "https://www.youtube.com/watch?v=UwzzkBTswJg"
options = {
'format': 'bestaudio/best',
#'ignore-errors': True,
'postprocessors': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '192',
}],
'outtmpl': './output/%(title)s.%(format_note)s.%(ext)s',
}
with youtube_dl.YoutubeDL(options) as youtube_object:
    meta = youtube_object.extract_info(links, download = False)

print(youtube_object['outtmpl'])
print(meta["ext"])