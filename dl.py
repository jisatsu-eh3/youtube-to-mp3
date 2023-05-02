import yt_dlp

def download_audio(yt_url):

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])

def main():

    urlList = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ"]
    for i in range(len(urlList)):
        yt_url = urlList[i]
        download_audio(yt_url)

main()

