# Projeto de teste para transcrição do áudio de vídeos

Todo o processo é feito por etapas, então há necessidade de rodar individualmente os arquivos baixar, converter e transcrever. A ideia era mesclar todos no mesmo código, mas o meu objetivo final é utilizar alguma ferramenta de IA para resumir o conteúdo do vídeo, então optei por deixá-lo desta maneira para analisar o andamento


# Caso queira alterar o projeto, informações importantes:

- O projeto foi pensado para baixar e converter um vídeo de cada vez. Caso queira fazer em massa, é preciso alterar as linhas que especificam o nome do arquivo para que ele não seja sobrescrito (tanto em áudio quanto vídeo e transcrição).
- É necessário instalar o ffmpeg para que o áudio seja tratado.
- A conversão precisa ser para .wav porque é o formato mais receptivo para a llm.
- O vídeo e o áudio serão salvos na pasta downloads com o mesmo nome, portanto serão sobrescritos
- O modelo é de linguagem é o "recogna-nlp/ptt5-base-summ-xlsum"


# Pacotes necessários
- SpeechRecognition (reconhecimento de voz/transcrição)
- transformers (huggingface)
- sentencepiece (completementar huggingface)
- torch (necessário para a llm)
- protobuf (necessário para a llm)
- pyaudio (opcional, para captura de áudio ao vivo)
