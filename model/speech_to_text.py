from conn import client
from promt import request


def text(pas: str):
    audio_file = open(pas, "rb")
    transcription = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )
    audio_file.close()
    request(transcription.text)