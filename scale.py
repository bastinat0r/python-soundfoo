import numpy as np

base = np.asarray([1., 25./24, 9./8, 6./5, 5./4, 4./3, 25./18, 3./2, 8./5, 5./3, 9./5, 15./8])

pentatonic_moll = np.asarray([
        base[0],
        base[3],
        base[5],
        base[7],
        base[10]
        ])

pentatonic_dur = np.asarray([
        base[0],
        base[2],
        base[4],
        base[7],
        base[10]
        ])

dur = np.asarray([
        base[0],
        base[2],
        base[5],
        base[7],
        base[10]
        ])

dur = np.asarray([
        base[0],
        base[2],
        base[4],
        base[5],
        base[7],
        base[9],
        base[11]
        ])
