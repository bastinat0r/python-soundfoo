#! /usr/bin/python2.7
from scipy.io.wavfile import write
import scikits.audiolab
import numpy as np
import random

from tone import Tone
from multi_tone import MultiTone
import scale
rate = 44100

def play(t):
    scikits.audiolab.play(t.get_array(rate), fs=rate)

for f in np.nditer(220 * scale.pentatonic_moll):
    print f
    play(Tone(f, 0.2, 0.2))


while True:
    f1 = random.choice(scale.pentatonic_moll * 220)
    print f1
    t = MultiTone([Tone(f1 * i, 0.05/i, 0.5/i) for i in range(1, 3)])

    t1 = MultiTone([Tone(f1 * i * random.choice(scale.pentatonic_moll), 0.04/i, 0.5/i) for i in range(1, 3)])

    t.add_tone(t1)
    t1 = MultiTone([Tone(f1 * i * random.choice(scale.pentatonic_moll), 0.04/i, 0.5/i) for i in range(1, 3)])
    t.add_tone(t1)
    play(t)
    #t.plot(220 , rate)

