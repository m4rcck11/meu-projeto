import subprocess




input_file = "downloads/audio.mp4"
saida = "downloads/audio.wav"


rodar = ["ffmpeg", "-i", input_file, "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", saida]


subprocess.run(rodar, check=True);


print("Convertido:", saida)