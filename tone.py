
import numpy as np


class Tone(object):
    """ton ohne obertoene"""

    def decay_default(t):
        return 1-t**3

    def get_array(self, sample_rate):
        """get numpy-arry for tone

        :sample_rate: sample rate to use
        :returns: numpy-arry with the sampled tone

        """
        t = np.linspace(0, 1.0, num = self.duration * sample_rate)

        data = self.wavefunc(2 * np.pi * self.freq * t) * self.amp * self.decayfunc(t)
        return data.astype(np.float)

    def __init__(self, freq, amp, duration, decayfunc=decay_default, wavefunc=np.sin):
        """
        :freq: Frequenzy
        :amp: amplitude
        :duration: duration
        :decayfunc: decay-function
        :wavefunc: waveform-function
        """

        self.freq = freq
        self.amp = amp
        self.decayfunc = decayfunc
        self.duration = duration
        self.wavefunc = wavefunc
