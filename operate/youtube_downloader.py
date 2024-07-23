from pytube import YouTube

def download_youtube_video(url, path):
    yt = YouTube(url)
    yt.streams.get_highest_resolution().download(output_path=path)
    print("Download completed!")
