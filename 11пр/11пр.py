import json
import requests
from tkinter import *


def click():
    file_o = open('output11.txt', 'r+')
    info = requests.get(f"https://api.github.com/users/{vvod.get()}").json()

    try:
        company = info["company"]
    except:
        company = None
    try:
        id=info["id"]
    except:
        id=None
    try:
        email=info["email"]
    except:
        email=None
    try:
        name=info["name"]
    except:
        name=None
    try:
        url=info["url"]
    except:
        url=None
    try:
        created_at=info["created_at"]
    except:
        created_at=None
    print(f"'company': {company}\n 'created_at': {created_at}\n 'email':{email}\n 'id':{id}\n 'name':{name}\n 'url':{url}")
    file_o.write(f"'company': {company}\n 'created_at': {created_at}\n 'email':{email}\n 'id':{id}\n 'name':{name}\n 'url':{url}")

window=Tk()
window.title('Ивакин Артём УБ-23')
window.geometry('1000x500')

lbl = Label(window, text="№4; имя: nixpkgs", font=("Arial Bold", 20))
lbl.grid(column=0,row=0)
button=Button(window,text='тык', command = click)
button.grid(column=0,row=1)

vvod=Entry(window,width=16)
vvod.grid(column=0,row=2)


window.mainloop()