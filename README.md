# YouTube to MP3 Downloader

This Python script allows you to download YouTube videos as MP3 audio files. It uses the `yt_dlp` library to download videos from YouTube and `ffmpeg` to convert the videos to MP3 format.

## Requirements

This script requires Python 3 and the following libraries:

    yt_dlp: used to download videos from YouTube
    ffmpeg: used to convert videos to MP3 format

You can install yt_dlp using the following command:

```
pip install yt_dlp
```

## Usage

To use this script, add the YouTube video URLs that you want to download to the `urlList` variable in the script:

```
urlList = [
"https://www.youtube.com/watch?v=dQw4w9WgXcQ",
"https://www.youtube.com/watch?v=4fezP875xOQ"
]
```

Then run the script using the following command:

```
python youtube_to_mp3.py
```

The script will download the videos and convert them to MP3 audio files. The MP3 files will be saved in the same directory as the script.

## Copyright Issues

It is important to note that downloading copyrighted content from YouTube may be illegal in some countries. It is your responsibility to ensure that you have the right to download and use the content before using this script. 
