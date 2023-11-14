import tkinter as tk
from pytube import YouTube

def downloader():
    try:
        url = YouTube(str(link.get()))
        video = url.streams.first()
        video.download()
        tk.Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)
    except Exception as e:
        tk.Label(root, text='ERROR: ' + str(e), font='arial 15').place(x=180, y=210)

root = tk.Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("YouTube Video Downloader")

tk.Label(root, text='Youtube Video Downloader', font='arial 20 bold').pack()

# Enter link
link = tk.StringVar()
tk.Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=160, y=60)
link_enter = tk.Entry(root, width=70, textvariable=link).place(x=32, y=90)

# Button to download video
tk.Button(root, text='DOWNLOAD', font='arial 15 bold', bg='blue', padx=2, command=downloader).place(x=180, y=150)

root.mainloop()
