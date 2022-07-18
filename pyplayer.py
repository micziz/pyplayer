import os, sys
from pyfzf.pyfzf import FzfPrompt
from playsound import playsound

arr = os.listdir('.')
while True:
    fzf = FzfPrompt()
    music = fzf.prompt(arr)
    "".join(music)
    sMusic = str(music)
    if sMusic.endswith(".mp3']"):
        nSMusic = sMusic.removesuffix("']") 
        nNSMusic = nSMusic.removeprefix("['")
        try:
            playsound(nNSMusic)
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit()
        chooseContinue = input("Repeat? ")
        if chooseContinue == "yes":
            try:
                playsound(nNSMusic)
            except KeyboardInterrupt:
                print("Exiting...")
                sys.exit()
        else:
            continue