import pytube

url = input("Inserte la url del video:")
youtube = pytube.YouTube(url)
video = youtube.streams.first()
video.download()
url = input("Inserte Url")
