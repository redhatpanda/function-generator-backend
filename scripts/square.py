#write a python script that takes frequency and amplitude as input and generates a square wave using scipy.signal.square
#and plots it
import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal
import math


def square_wave(freq, amp):
    t = np.arange(0, 1, 0.001)
    s = amp * signal.square(2 * math.pi * freq * t)
    return s


def main():
    freq = float(input("Enter frequency: "))
    amp = float(input("Enter amplitude: "))
    s = square_wave(freq, amp)
    plt.plot(s)
    plt.show()


if __name__ == "__main__":
    main()


