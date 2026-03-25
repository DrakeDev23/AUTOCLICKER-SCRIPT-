import ctypes
import keyboard
import time

class AutoMiner:
    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.mining = False
        self.holding = False

    def press_mouse(self):
        self.user32.mouse_event(2, 0, 0, 0, 0)

    def release_mouse(self):
        self.user32.mouse_event(4, 0, 0, 0, 0)

    def toggle_mining(self):
        self.mining = not self.mining
        print("Mining:", self.mining)

    def stop(self):
        if self.holding:
            self.release_mouse()
        print("Exiting...")

    def run(self):
        print("F6 = toggle mining")
        print("ESC = exit")

        while True:
            if keyboard.is_pressed("esc"):
                self.stop()
                break

            if keyboard.is_pressed("F6"):
                self.toggle_mining()
                time.sleep(0.4)  

            if self.mining and not self.holding:
                self.press_mouse()
                self.holding = True

            if not self.mining and self.holding:
                self.release_mouse()
                self.holding = False

            time.sleep(0.01)


if __name__ == "__main__":
    miner = AutoMiner()
    miner.run()