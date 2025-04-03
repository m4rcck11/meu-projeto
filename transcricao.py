import speech_recognition as sr
from transformers import pipeline




r = sr.Recognizer()




with sr.AudioFile('downloads/audio.wav') as source:
    print("Ajustando para o ambiente de áudio...")
    r.adjust_for_ambient_noise(source)  
    print("Realizando reconhecimento de áudio. Aguarde.")
    audio_text = r.record(source)  

try:
    text = r.recognize_google(audio_text, language='pt-BR') 
    print("Transcrição realizada.")
    print(text)
    
    with open('transcricao.txt', 'w', encoding='utf-8') as arq:
        arq.write(text)
    print("Texto salvo em 'transcricao.txt'.")

    print("Gerando resumo...")
    summarizer = pipeline("summarization", model="recogna-nlp/ptt5-base-summ-xlsum")
    resumo = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']

    print("Resumo gerado!")
    print(resumo)

    with open('resumo.txt', 'w', encoding='utf-8') as arq:
        arq.write(resumo)

    print("Resumo salvo em 'resumo.txt'.")





except sr.UnknownValueError:
    print("Erro desconhecido.")
except sr.RequestError as e:
    print(f"Erro ao solicitar a transcrição: {e}")
