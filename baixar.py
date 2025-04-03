from pytubefix import YouTube 







url = 'https://youtu.be/vt7_S2PcAgg?list=RDNSr3g2PiRGIt4'


yt = YouTube(url)
stream = yt.streams.filter(only_audio=True).first()
stream.download(output_path="downloads", filename="audio.mp4")


print("baixou")