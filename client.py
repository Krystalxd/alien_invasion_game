import requests
import json
from tkinter import *


def update_score(score):
    def show_message():
        global nick
        print(message_entry.get())
        nick = message_entry.get()
        root.destroy()


    root = Tk()
    root.title("Results")
    root.geometry("300x250")
    root.lift()

    message_entry = Entry(textvariable="")
    message_entry.place(relx=.5, rely=.1, anchor="c")

    message_button = Button(text="Confirm", command=show_message)
    message_button.place(relx=.5, rely=.5, anchor="c")

    root.mainloop()

    get = requests.get('http://127.0.0.1:8888')

    data = get.json()
    data[nick] = score
    send = json.dumps(data)
    requests.post('http://127.0.0.1:8888', json=send)
