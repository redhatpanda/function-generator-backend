#write a python script that takes frequency and amplitude as input and generates a sine wave
#and plots it
import numpy as np
import matplotlib.pyplot as plt
import math


def sine_wave(freq, amp):
    t = np.arange(0, 1, 0.001)
    s = amp * np.sin(2 * math.pi * freq * t)
    plt.plot(s)
    plt.savefig('sine_wave.png')


# def main():
#     freq = float(input("Enter frequency: "))
#     amp = float(input("Enter amplitude: "))
#     s = sine_wave(freq, amp)
#     plt.plot(s)
#     plt.show()


# if __name__ == "__main__":
#     main()

    