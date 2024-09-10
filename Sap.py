# Importing requirements
from os import listdir, remove, system, name
from pygame import mixer
from time import sleep
import threading
from random import choice
import json

mixer.init()
if name == "nt":
    system("cls")
else:
    system("clear")

word = """
    ._______.     ___      .______        .______   ____    ____ 
    /       |    /   \\     |   _  \\       |   _  \\  \\   \\  /   / 
   |   (----`   /  ^  \\    |  |_)  |      |  |_)  |  \\   \\/   /  
    \\   \\      /  /_\\  \\   |   ___/       |   ___/    \\_    _/   
.----)   |    /  _____  \\  |  |     __    |  |          |  |     
|_______/    /__/     \\__\\ | _|    (__)   | _|          |__|     

"""

x = choice(listdir("utils/loading"))

print(word)
print("\n\n\n\n\n\nLoading....")
v = 0.1
mixer.music.set_volume(v)
mixer.music.load("./utils/loading/" + x)
mixer.music.play()
sleep(4)
mixer.music.fadeout(3000)
mixer.music.unload()

if name == "nt":
    system("cls")
else:
    system("clear")
print(word)

print(
    "\nWelcome to Sappy!\n\n~~>Built by Avnes\n~~>Dogshit by default\n~~>Use at your own risk\n"
)
print(
    "Here are your saved songs... To add more, move the required audio files to the 'songs' folder.\n"
)

for i in range(len(listdir("songs"))):
    if listdir("songs")[i] != "◌󠇯.txt":
        print(i + 1, ".", listdir("songs")[i][:-4:])
print("\n")


isPaused = False
is_running = True
q = []
p = []


def playload():
    with open("playlists.json", "r") as file:
        playlists = json.load(file)
        return playlists


def songplay():
    global isPaused, v, q, is_running, p
    while True:
        if mixer.music.get_busy() == False and isPaused == False:
            if len(q) != 0:
                mixer.music.unload()
                x = q.pop(0)
                p.append(x)
                mixer.music.load(x)
                mixer.music.set_volume(v)
                mixer.music.play()
        if is_running == False:
            quit()
        sleep(2)


song = threading.Thread(target=songplay, args=())


def player():
    global isPaused, v, q, is_running, p
    while True:
        n = input("\n >>> ")

        if n.lower().startswith("p "):
            try:
                sn = n.split()[1]
                if sn.isdigit() and sn.isdigit() in range(len(listdir("songs"))):
                    sn = int(sn)
                    s = str(listdir("songs")[sn - 1])
                    q.append("./songs/" + s)
                    mixer.music.stop()
                    mixer.music.unload()
                    print(f"Now Playing {s}")
            except:  # noqa: E722
                print("Invalid function arguments... try again.")

        elif n.lower() == "l":
            print("\nShowing song list.\n")
            for i in range(len(listdir("songs"))):
                if listdir("songs")[i] != "◌󠇯.txt":
                    print(i + 1, ".", listdir("songs")[i][:-4:])

        elif n.lower().startswith("v"):
            try:
                print("Current volume:", mixer.music.get_volume() * 100, "%")
                v = float(n.split()[1]) / 100
                if mixer.music.get_busy() == True:
                    mixer.music.set_volume(v)
                print("New volume:", v * 100, "%")
            except:
                ...

        elif n.lower() == "h":
            print(
                "\nKindly ignore the quotes and enter the characters only\n-> Enter 'P' to play a song\n-> Enter 'L' to view the list of songs in the songs folder\n-> Enter 'PP' to pause the current song\n-> Enter 'R' to resume\n-> Enter 'N' to go to the next song in queue\n-> Enter 'PV' to go to the previous song\n-> Enter 'CQ' to stop playback and clear the queue\n-> Enter 'CS' to clear the screen (buggy and not recommended for use)\n-> Enter 'V' to change the Volume\n-> Enter 'D' to delete a song\n-> Enter 'E' to exit"
            )

        elif n.lower() == "pp":
            mixer.music.pause()
            isPaused = True

        elif n.lower() == "r":
            mixer.music.unpause()
            isPaused = False

        elif n.lower() == "n":
            mixer.music.stop()
            mixer.music.unload()
            print("Moving on to the next song...")

        elif n.lower() == "pv":
            q.insert(0, p.pop())
            q.insert(0, p.pop())
            mixer.music.stop()
            mixer.music.unload()
            print("Going to the previous song...")

        elif n.lower().startswith("q"):
            if n.lower() == "q":
                for i in range(len(q)):
                    print(str(i + 1) + ".", q[i][8:-4:])
            else:
                try:
                    sn = n.split()[1]
                    if sn.isdigit() and sn.isdigit() in range(len(listdir("songs"))):
                        sn = int(sn)
                        s = str(listdir("songs")[sn - 1])
                        q.append("./songs/" + s)
                        print(f"Added {s} to the queue.")
                except:
                    print("Invalid function arguments... try again.")

        elif n.lower() == "cq":
            mixer.music.stop()
            mixer.music.unload()
            q.clear()

        elif n.lower().startswith("pl"):
            if n.lower() == "pl":
                x = 1
                for i in playload():
                    print(f"{x}. {i}")
                    x += 1
            elif n.lower().startswith("pl q"):
                select = n.split()[2]
                for i in playload()[select]:
                    q.append("./songs/" + i)

            elif n.lower().startswith("pl new"):
                try:
                    plname = n.split()[2]
                    songnumbers = eval(n.split()[3])
                    songs = [listdir("songs")[i - 1] for i in songnumbers]
                    playlists = playload()
                    playlists[plname] = songs
                    with open("playlists.json", "w") as file:
                        json.dump(playlists, file, indent=4)
                except IndexError:
                    print("Invalid syntax: use 'pl new <name> <song_number list>' ")

            elif n.lower().startswith("pl del"):
                try:
                    plname = n.split()[2]
                    playlists = playload()
                    playlists.pop(plname)
                    with open("playlists.json", "w") as file:
                        json.dump(playlists, file, indent=4)
                except IndexError:
                    print("Invalid syntax: use 'pl del <playlist_name>' ")

        elif n.lower().startswith("d"):
            try:
                d = n.split()[1]
                if int(d) - 1 in range(len(listdir("songs"))):
                    remove("songs/" + str(listdir("songs")[int(d) - 1]))
            except IndexError:
                print("Invalid function arguments... try again.")

        elif n.lower() == "cs":
            if name == "nt":
                system("cls")
            else:
                system("clear")
            print("\n\nInterface Cleared.")

        elif n.lower() == "rr":
            mixer.music.stop()
            mixer.music.unload()
            q.clear()
            print("Never Gonna Give You Up")
            mixer.music.load("./utils/narr.mp3")
            mixer.music.play()

        elif n.lower() == "e":
            q.clear()
            mixer.music.stop()
            mixer.music.unload()
            is_running = False
            quit()

        else:
            print("Unknown command. Enter 'h' for help.")


play = threading.Thread(target=player, args=())


play.start()
song.start()

while True:
    sleep(0.5)
    if is_running == False:
        print("\nThank You For Using Sap.py.\nMade with <3 by Avnes")
        quit()
