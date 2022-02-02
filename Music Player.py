# importing the libraries
from tkinter import *
import pygame
import os


# Define class
class MusicPlayer:
    # constructor class
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("1000x200+200+200")
        # initiate pygame
        pygame.init()
        pygame.mixer.init()
        self.track = StringVar()
        self.status = StringVar()

        trackframe = LabelFrame(self.root, text="Playing Now...", font=("times new roman", 15, "bold"), bg="grey",fg="white", bd=5, relief=GROOVE)
        trackframe.place(x=0, y=0, width=600, height=100)
        songt = Label(trackframe, textvariable=self.track, width=20, font=("times new roman", 24, "bold"), bg="grey",fg="gold").grid(row=0, column=0, padx=10, pady=5)
        trackstatus = Label(trackframe, textvariable=self.track, width=20, font=("times new roman", 24, "bold"),bg="grey", fg="gold").grid(row=0, column=1, padx=10, pady=5)

        buttonframe = LabelFrame(self.root, text="Control", font=("times new roman", 15, "bold"), bg="grey", fg="white",bd=5, relief=GROOVE)
        buttonframe.place(x=0, y=100, width=600, height=100)
        playbtn = Button(buttonframe, text="PLAY", command=self.playsong, width=6, height=1,font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=0, padx=10,pady=5)
        playbtn = Button(buttonframe, text="PAUSE", command=self.pausesong, width=8, height=1,font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=1, padx=10,pady=5)
        playbtn = Button(buttonframe, text="RESUME", command=self.resumesong, width=8, height=1,font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=3, padx=10,pady=5)
        playbtn = Button(buttonframe, text="STOP", command=self.stopsong, width=6, height=1,font=("times new roman", 16, "bold"), fg="navyblue", bg="gold").grid(row=0, column=4, padx=10,pady=5)

        songsframe = LabelFrame(self.root, text="Songs", font=("times new roman", 15, "bold"), bg="grey", fg="white",bd=5, relief=GROOVE)
        songsframe.place(x=600, y=0, width=400, height=200)
        scrol_y = Scrollbar(songsframe, orient=VERTICAL)
        self.playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gold", selectmode=SINGLE,font=("times new roman", 12, "bold"), bg="silver", fg="navyblue", bd=5, relief=GROOVE)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.playlist.yview)
        self.playlist.pack(fill=BOTH)
        os.chdir("/Users/DELL/Desktop/The Official UK Top 40 Singles Chart (12.07.2019) Mp3 (320 kbps) [Hunter]")
        songt = os.listdir()
        for track in songt:
            self.playlist.insert(END, track)

    def playsong(self):
        self.track.set(self.playlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.playlist.get(ACTIVE))
        pygame.mixer.music.play()

    def stopsong(self):
        self.status.set("-Stopped")
        pygame.mixer.music.stop()

    def pausesong(self):
        self.status.set("-Paused")
        pygame.mixer.music.pause()

    def resumesong(self):
        self.status.set("-Resuming")
        pygame.mixer.music.unpause()


root = Tk()
MusicPlayer(root)
root.mainloop()
