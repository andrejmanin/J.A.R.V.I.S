from model.conn import client
from model.text_to_speech import speech

text = 'Привіт ти асистент JARVIS. Твоє завдання допомагати користувачу з його питаннями та проблемами'


def request(promt: str):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": text},
            {"role": "user", "content": promt},
        ],
    )

    speech(completion.choices[0].message.content)
