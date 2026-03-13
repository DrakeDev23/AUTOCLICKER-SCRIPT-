import ctypes
import keyboard
import time

user32 = ctypes.windll.user32

mining = False
holding = False

print("F6 = toggle mining")
print("ESC = exit")

while True:

    if keyboard.is_pressed("esc"):
        if holding:
            user32.mouse_event(4,0,0,0,0)  
        print("Exiting...")
        break

    if keyboard.is_pressed("F6"):
        mining = not mining
        print("Mining:", mining)
        time.sleep(0.4)

    if mining and not holding:
        user32.mouse_event(2,0,0,0,0)  
        holding = True

    if not mining and holding:
        user32.mouse_event(4,0,0,0,0)  
        holding = False

    time.sleep(0.01)