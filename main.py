import struct

import speech_recognition
from pydub import AudioSegment
from pydub.playback import play
import random
import time
import pyaudio
import pvporcupine

import commands


sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5


def listen():
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(mic, 0.5)
        try:
            audio = sr.listen(mic)
            query = sr.recognize_google(audio_data=audio, language="uk-UA")
        except speech_recognition.exceptions.UnknownValueError:
            return ""
        print(query)
        return query


def do_command():
    while True:
        command = listen()
        if command.lower() == 'піди відпочинь':
            return 0
        for i, k in tasks.items():
            if command.lower() == i:
                ok = ['sound/ok/uk/uk-done-1.mp3', 'sound/ok/uk/uk-done-2.mp3', 'sound/ok/uk/uk-done-3.mp3']
                time.sleep(0.5)
                k()
                play(AudioSegment.from_mp3(ok[random.randint(0, len(ok) - 1)]))
                return
        # commands.gpt(command)
        return


tasks = {
    "відкрий chrome": commands.chrome,
    "відкрий youtube": commands.youtube,
    "увімкни музику": commands.music,
    "перезавантажся": commands.restart_program,
    "закрий вкладку": commands.close_web,
    "закрий вікно": commands.close_app,
    "перезавантаж систему": commands.reboot,
    "gpt": commands.gpt,
    "web workspace": commands.create_web_workspace,
    "gpt код": commands.gpt_code,

}


def wakeup():
    list = ['sound/wakeup/uk/run-1.mp3', 'sound/wakeup/uk/run-2.mp3']
    play(AudioSegment.from_mp3(list[random.randint(0, len(list) - 1)]))


def main():

    wakeup()

    porcupine = None
    pa = None
    audio_stream = None
    try:
        porcupine = pvporcupine.create(
            access_key='XH1XgIHYTHwZ5ITQ3Em1OYXYHX4YCSd3WhCyP9v7TWxxM5dPNkyK4w==',
            keywords=["jarvis"]
        )
        pa = pyaudio.PyAudio()
        audio_stream = pa.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )
        while True:
            pcm = audio_stream.read(porcupine.frame_length)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            keyword_index = porcupine.process(pcm)
            if keyword_index >= 0:
                greet = ['sound/greet/uk/uk-listen.mp3', 'sound/greet/uk/uk-listen-2.mp3', 'sound/greet/uk/uk-yes-sir.mp3']
                play(AudioSegment.from_mp3(greet[random.randint(0, len(greet)) - 1]))
                time.sleep(0.5)
                do_command()
                time.sleep(1)

    finally:
        if porcupine is not None:
            porcupine.delete()

        if audio_stream is not None:
            audio_stream.close()

        if pa is not None:
            pa.terminate()

if __name__ == "__main__":
    main()