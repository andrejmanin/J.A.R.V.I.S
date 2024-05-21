import webbrowser
import random
import subprocess
import sys
import pyautogui
import os
import speech_recognition

from model.promt import request
from model.text_to_speech import speech

def chrome():
    webbrowser.open('https://www.google.com/')

def youtube():
    webbrowser.open('https://www.youtube.com/')

def gpt(query):
    # sr = speech_recognition.Recognizer()
    # sr.pause_threshold = 0.5
    # print("gpt-on")
    # with speech_recognition.Microphone() as mic:
    #     sr.adjust_for_ambient_noise(mic, 0.5)
    #     try:
    #         audio = sr.listen(mic)
    #         query = sr.recognize_google(audio_data=audio, language="ru-RU")
    #     except speech_recognition.exceptions.UnknownValueError:
    #         return ""
    speech(request(query))

def gpt_code():
    folder_path = 'C:/Users/Andrew/Desktop'
    file_name = f'gpt_code.txt'
    file_path = os.path.join(folder_path, file_name)

    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5
    print("gpt-on")
    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(mic, 0.5)
        try:
            audio = sr.listen(mic)
            query = sr.recognize_google(audio_data=audio, language="ru-RU")
        except speech_recognition.exceptions.UnknownValueError:
            return ""

        with open(file_path, 'w') as f:
            f.write(request(query))
        f.close()



def music():
    music_list = ['https://music.youtube.com/watch?v=QN1odfjtMoo&list=RDAMVMQN1odfjtMoo',
                  'https://music.youtube.com/watch?v=hTWKbfoikeg',
                  'https://music.youtube.com/watch?v=QUvVdTlA23w&list=RDAMVMhTWKbfoikeg',
                  'https://music.youtube.com/watch?v=VcsMFlxWGfA&list=RDAMVMVcsMFlxWGfA',
                  'https://music.youtube.com/watch?v=ktF_D0-ndCE',
                  'https://music.youtube.com/watch?v=q7xpwbdHAKM',
                  'https://music.youtube.com/watch?v=POyZQaexBOM&list=RDAMVMPOyZQaexBOM',
                  'https://music.youtube.com/watch?v=8zX35YQzvVQ&list=RDAMVMPOyZQaexBOM',
                  'https://music.youtube.com/watch?v=Gk3nlsDG7Ng&list=RDAMVMhjF0cEJVlsw',
                  'https://music.youtube.com/watch?v=HZnNt9nnEhw&list=OLAK5uy_mUTYCeC-X91GXyD5lgyPP9lPaT3SzVhbg',
                  'https://music.youtube.com/watch?v=QTIkudYT3mg&list=RDAMPLOLAK5uy_mUTYCeC-X91GXyD5lgyPP9lPaT3SzVhbg',
                  'https://music.youtube.com/watch?v=SRcnnId15BA',
                  'https://music.youtube.com/watch?v=fPO76Jlnz6c',
                  'https://music.youtube.com/watch?v=TO-_3tck2tg&list=RDAMVMfPO76Jlnz6c',
                  'https://music.youtube.com/watch?v=XrsbfrFPATs&list=OLAK5uy_nChLJ6OwuxwMF0UXADCu9pNx32f_6GuZA',
                  'https://music.youtube.com/watch?v=77z60qxdF44',
                  'https://music.youtube.com/watch?v=1z8NpmCqvZE&list=RDAMVM77z60qxdF44',
    ]
    webbrowser.open(music_list[random.randint(0, len(music_list)) - 1])

def restart_program():
    python = sys.executable
    subprocess.Popen([python] + sys.argv)

def close_web():
    pyautogui.hotkey('ctrl', 'w')

def close_app():
    pyautogui.hotkey('alt', 'f4')

def reboot():
    os.system("shutdown /r /t 1")

def create_web_workspace():
    target_directory = r'F:\web-projects'
    folder_name = 'new-folder'

    folder_path = os.path.join(target_directory, folder_name)

    os.makedirs(folder_path, exist_ok=True)

    file_name = f'index.html'
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as f:
        f.write(f'<!DOCTYPE html>\n<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>Document</title>\n\t<link rel="stylesheet" href="style.css">\n</head>\n<body>\n\n</body>\n</html>')

    file_name = f'style.css'
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w') as f:
        pass