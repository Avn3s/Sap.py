from os import system, name
from time import sleep

if name == "nt":
    x = "py"
else:
    x = "python3"
system(x + " -m pip install --upgrade pip")
print("pip successfully updated!")
system(x + " -m pip install pygame")
print("\nPygame Successfully installed!")
system(x + " -m pip install --upgrade pygame")
print("Pygame successfully updated!")
sleep(5)
exit()
