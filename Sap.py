#Importing requirements
from os import listdir,remove,system,name
from subprocess import call
from pygame import mixer
from time import sleep
from pygame import USEREVENT,event
import threading

mixer.init()
if name=="nt":
    system("cls")
else:
    system("clear")

pop='''
    ._______.     ___      .______        .______   ____    ____ 
    /       |    /   \     |   _  \       |   _  \  \   \  /   / 
   |   (----`   /  ^  \    |  |_)  |      |  |_)  |  \   \/   /  
    \   \      /  /_\  \   |   ___/       |   ___/    \_    _/   
.----)   |    /  _____  \  |  |     __    |  |          |  |     
|_______/    /__/     \__\ | _|    (__)   | _|          |__|     

'''
print(pop)
print("\n\n\n\n\n\nLoading....")
mixer.music.load("./utils/loadingscreen.mp3")
mixer.music.play()
sleep(6)
mixer.music.fadeout(3000)
mixer.music.unload()

if name=="nt":
    system("cls")
else:
    system("clear")
print(pop)

print("\nWelcome to Sappy!\n\n~~>Built by Avnes\n~~>Dogshit by default\n~~>Use at your own risk\n")
print("Here are your saved songs... To add more, move the required audio files to the 'songs' folder.\n")

v=1.0
for i in range(len(listdir('songs'))):
        if listdir('songs')[i]!='ZZZ.txt':
            print(i+1,'.','\t',listdir('songs')[i])
print('\n')

MUSIC_END=USEREVENT+1
mixer.music.set_endevent(MUSIC_END)

q=[]


def songplay(q):
    while True:
        if (mixer.music.get_busy()==False) or (event == MUSIC_END):
            if len(q)!=0:
                mixer.music.unload()
                x=q.pop(0)
                mixer.music.load(x)
                mixer.music.play()
        sleep(2)


song=threading.Thread(target=songplay, args=(q,))

def player(q):
    while True:
        n=input("\n >>-----> ")
        
        if n.lower()=='p':
            sn=(input("Specify the song ID from the list: "))
            if sn.isdigit() and sn.isdigit() in range(len(listdir('songs'))):
                sn=int(sn)
                s=str(listdir('songs')[sn-1])
                q.append("./songs/"+s)
                print("Added",s,"to the queue.")
            else:
                print('Invalid function... try again.')
            
        elif n.lower()=='l':
            print("\nShowing song list.\n")
            for i in range(len(listdir('songs'))):
                if listdir('songs')[i]!='ZZZ.txt':
                    print(i+1,'.','\t',listdir('songs')[i])
            
        elif n.lower()=='v':
            print("Current volume:",mixer.music.get_volume()*100,'%')
            v=(float(input("Enter Volume: ")))/100
            if mixer.music.get_busy()==True:
                mixer.music.set_volume(v)
            print("New volume:",v*100,'%')

        elif n.lower()=='h':
            print("\nKindly ignore the quotes and enter the characters only\n-> Enter 'P' to play a song\n-> Enter 'L' to view the list of songs in the songs folder\n-> Enter 'PP' to pause the current song\n-> Enter 'R' to resume\n-> Enter 'N' to go to the next song in queue\n-> Enter 'CQ' to stop playback and clear the queue\n-> Enter 'CS' to clear the screen (buggy)\n-> Enter 'V' to change the Volume\n-> Enter 'D' to delete a song\n-> Press Alt+F4 to exit")
            
        elif n.lower()=="pp":
            mixer.music.pause()
            
        elif n.lower()=="r":
            mixer.music.unpause()
            
        elif n.lower()=="n":
            mixer.music.stop()
            mixer.music.unload()
            print("Moving on to the next song...")
            
        elif n.lower()=="cq":
            mixer.music.stop()
            mixer.music.unload()
            q.clear()

        elif n.lower()=="d":
            d=input("Song number to be deleted (enter 'esc' to skip): ")
            if d!='esc':
                if int(d)-1 in range(len(listdir('songs'))):
                    remove('songs/'+str(listdir('songs')[int(d)-1]))
        
        elif n.lower()=="cs":
            if name=="nt":
                system("cls")
            else:
                system("clear")
        
        elif n.lower()=="rr":
            mixer.music.stop()
            mixer.music.unload()
            q.clear()
            print("Never Gonna Give You Up")
            mixer.music.load("./utils/narr.mp3")
            mixer.music.play()
        
        else:
            print("Unknown command. Enter 'h' for help.")


play=threading.Thread(target=player, args=(q,))


play.start()
song.start()

