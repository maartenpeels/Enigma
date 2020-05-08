import sys
from math import floor

import pygame

from enigma import Enigma
from plugboard import Plugboard
from reflector import Reflector
from rotor import Rotor

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keyboard = [
    "QWERTYUIOP",
    "ASDFGHJKL",
    "ZXCVBNM"
]

key_size = 16

black = (0, 0, 0)

key_color = (128, 128, 128)
key_color_pressed = (255, 255, 100)

pressed_key = None

e1 = Enigma(rotors=[
    Rotor(position=24, type="II"),
    Rotor(position=13, type="I"),
    Rotor(position=22, type="III")
],
    plugboard=Plugboard([
        ('A', 'M'),
        ('F', 'I'),
        ('N', 'V'),
        ('P', 'S'),
        ('T', 'U'),
        ('W', 'Z'),
    ]),
    reflector=Reflector("A")
)

pygame.init()
window = pygame.display.set_mode((800, 600))
font = pygame.font.Font('freesansbold.ttf', 16)

pygame.display.flip()


def draw_keyboard(pos):
    row_num = 0
    y = pos[1]
    for row in keyboard:
        x = pos[0] + (row_num * key_size)
        for char in row:
            draw_letter(char, (x, y))
            x += floor(key_size * 2.2)
        y += floor(key_size * 2.4)
        row_num += 1


def draw_letter(char, pos):
    pygame.draw.circle(window, key_color_pressed if char == pressed_key else key_color, pos, key_size)
    text_surface = font.render(char, True, black)
    window.blit(text_surface, (pos[0] - (key_size / 2), pos[1] - (key_size / 2)))


while True:
    window.fill(black)
    draw_keyboard((100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if chr(event.key).upper() in letters:
                pressed_key = chr(event.key).upper()
        if event.type == pygame.KEYUP:
            pressed_key = None
    pygame.display.flip()
