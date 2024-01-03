#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
from sys import exit

pin = 12
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
p = GPIO.PWM(pin, 10)

# Definición de las frecuencias de las notas
notes = {'C': 523.25, 'D': 587.33, 'E': 659.25, 'F': 349.23, 'G': 392.00, 'A': 440.00, 'B': 493.88, 'C5': 523.25, 'G5': 784.00, '#': 0.5}
# Velocidades de las notas
speed = {'w': 0.8, 'h': 0.6, 'q': 0.45, 'e': 0.3, 's': 0.15}

# Secuencia de "We Wish You a Merry Christmas"
merry_christmas = [
    ['G-q', 'E-q', 'E-q', 'F-q', 'D-q', 'D-q', 'C-h', '#-h',
     'G-q', 'E-q', 'E-q', 'F-q', 'D-q', 'D-q', 'C-h', '#-h',
     'C-q', 'C-q', 'C-q', 'G-q', 'A-q', 'A-q', 'G5-e', 'F-q', 'E-q', 'C-q', 'A-h', '#-h',
     'G-q', 'E-q', 'E-q', 'F-q', 'D-q', 'D-q', 'C-h', '#-h']
    # Repite o añade más secuencias según sea necesario
]

p.start(50)

header = '[Note]\t[Frequency]\t[Duration]'+'\n------\t-----------\t----------'
printcount = 0

def goodbye(msg=''):
    print(msg + '\n\nListo. Suerte chicken little')
    exit()

def play_song(song):
    global header, printcount, notes, speed
    try:
        print(header)
        for part in song:
            for note_info in part:
                note, duration = note_info.split('-')
                note_freq = notes[note]
                note_duration = speed[duration]
                print(f'  {note}\t   {note_freq}\t   {note_duration}')
                p.ChangeFrequency(note_freq)
                sleep(note_duration)
                p.ChangeFrequency(10)
    except KeyboardInterrupt:
        goodbye('\nInterrupted...')

while True:
    play_song(merry_christmas)
