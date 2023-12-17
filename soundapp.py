from os import listdir
from pygame import mixer
from time import sleep
mixer.init()
print("\nWelcome to SoundApp!\n")
print("Here are your saved songs... To add more, move the required audio files to the 'songs' folder.\n")
v=1.0
L=listdir('songs')
for i in range(len(L)):
    print(i+1,'.','\t',L[i])
print('\n')
while True:
    n=input("\nChoose function (Enter h for help): ")
    if n.lower()=='p':
        sn=int(input("Specify the song ID from the list: "))
        if sn in range(len(L)):
            s=str(L[sn-1])
            if mixer.music.get_busy()==False:
                print("Now playing:",s)
                mixer.music.load("./songs/"+s)
                mixer.music.set_volume(v)
                mixer.music.play()
        else:
            mixer.music.queue("./songs/"+s)
            print("Queued:",s)
    elif n.lower()=='l':
        print("\nShowing song list.\n")
        for i in range(len(L)):
            print(i+1,'.','\t',L[i])
    elif n.lower()=='v':
        print("Current volume:",mixer.music.get_volume()*100,'%')
        v=(float(input("Enter Volume: ")))/100
        mixer.music.set_volume(v)
        print("New volume:",v*100,'%')
    elif n.lower()=='h':
        print("\nKindly ignore the quotes and enter the characters only\n1. Enter 'P' to play a song\n2. Enter 'L' to view the list of songs in the songs folder\n3. Enter 'PP' to pause the current song\n4. Enter 'r' to resume\n5. Enter 'S' to stop playing the current song\n6. Enter 'V' to change the Volume\n7. Enter 'Q' to exit the app")
    elif n.lower()=="pp":
        mixer.music.pause()
    elif n.lower()=="r":
        mixer.music.unpause()
    elif n.lower()=="s":
        mixer.music.stop()
        mixer.music.unload()
    elif n.lower()=='q' or n.lower()==('QUIT'):
        print("Thank you for using SoundApp.\nMade with <3 by Avnes.")
        sleep(6)
        exit()