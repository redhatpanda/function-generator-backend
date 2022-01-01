#write a python script that takes frequency and amplitude as input and generates a triangle wave
#and plots it
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy.signal as signal


def triangle_wave(freq, amp):
    t = np.arange(0, 1, 0.001)
    s = amp * signal.sawtooth(2 * math.pi * freq * t, width=0.5)
    return s


def main():
    freq = float(input("Enter frequency: "))
    amp = float(input("Enter amplitude: "))
    s = triangle_wave(freq, amp)
    plt.plot(s)
    plt.show()


if __name__ == "__main__":
    main()

