from pynput import keyboard
from glob import glob
import pygame
import threading
import random

pygame.init()
pygame.mixer.init()
sound_tracks = glob('./sounds/*.wav')

def on_press(key):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(random.choice(sound_tracks))
    pygame.mixer.music.play()

def on_release(key):
    pass

key_listener = keyboard.Listener(on_press=on_press,
                                 on_release=on_release)
key_listener.start()

listener_thread = threading.Thread(target=key_listener)
# listener_thread.daemon = True
print('meow keyboard start..!')

while True:
    pass