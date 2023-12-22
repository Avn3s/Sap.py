from os import system
from time import sleep
system("py -m pip install --upgrade pip")
print("pip successfully updated!")
system("python -m pip install pygame")
print("\nPygame Successfully installed!")
system("python -m pip install --upgrade pygame")
print("Pygame successfully updated!")
sleep(5)
exit()