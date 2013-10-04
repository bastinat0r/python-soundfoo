import numpy as np

from tone import Tone

from matplotlib import pyplot

class MultiTone(object):
    """A selection of multiple tones"""

    def add_tone(self, tone):
        if isinstance(tone, Tone):
            self._tones.append(tone)
        if isinstance(tone, MultiTone):
            self._tones += tone.get_tones()

    def get_tones(self):
        return self._tones

    def get_matrix(self, sample_rate):
        m = [i.get_array(sample_rate) for i in self._tones]
        max_len = max([len(i) for i in m])
        m = [np.concatenate([i, np.zeros(max_len - len(i))]) for i in m]
        m = np.asmatrix(np.asarray(m))
        return m

    def plot(self, freq, sample_rate):
        print int(1.0/freq * sample_rate)
        x = np.asarray(self.get_array(sample_rate))
        x = np.squeeze(x)
        x = x[0:int(1.0/freq * sample_rate)]
        pyplot.plot(x)
        pyplot.show()

    def get_array(self, sample_rate):
        """get np.arry with tone samples

        :sample_rate: @todo
        :returns: @todo

        """
        m = self.get_matrix(sample_rate)
        s = np.sum(m, 0)
        return np.clip(s, -1.0, +1.0)

    def __init__(self, tones = []):
        """generate tones

        :tones: list of tones to use

        """
        self._tones = []
        for i in tones:
            if isinstance(i, Tone):
                self._tones.append(i)
            if isinstance(i, MultiTone):
                self._tones = self._tones + i.get_tones()
