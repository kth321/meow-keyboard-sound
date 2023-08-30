import keyboard
import pygame
import threading
import random
from glob import glob

# available_keys = [chr(97 + i) for i in range(26)]
available_keys = [97 + i for i in range(26)]

sound_tracks = glob('./sounds/cat*.wav')

print(available_keys)
print(sound_tracks)

pygame.init()
pygame.mixer.init()
beep_sound = pygame.mixer.Sound('./sounds/cat1.wav')

def key_listener():
    while True:
        for key in available_keys:
            if keyboard.is_pressed(key):
                beep_sound.stop()
                beep_sound.play()

listener_thread = threading.Thread(target=key_listener)
listener_thread.daemon=True
listener_thread.start()

print('thread started')
print('keep going')

while True:
    pass
