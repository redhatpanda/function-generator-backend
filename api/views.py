from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
import numpy as np
import matplotlib.pyplot as plt
from math import *
import matplotlib
import scipy.signal as signal
from scipy.signal import square
from scipy.integrate import quad 
import smtpserver
matplotlib.use('Agg')
# Create your views here.
@api_view(['POST'])
def handleGenFunction(request):
    gendata = request.data
    email = gendata.get('email')
    frequency = int(gendata.get('frequency'))
    amplitude = int(gendata.get('amplitude'))
    gentype = gendata.get('gentype')

    print(str(email)+" "+str(frequency)+" "+str(amplitude)+" "+str(gentype))

    if gentype == 'Sine-Wave':
        t = np.arange(0, 1, 0.001)
        s = amplitude * np.sin(2 * pi * frequency * t)
        plt.plot(s)
        plt.savefig('sine_wave.png')
        plt.close()
        smtpserver.sendSineEmail(email)

    elif gentype == 'Square-Wave':
        t = np.arange(0, 1, 0.001)
        s = amplitude * np.sin(2 * pi * frequency * t)
        plt.plot(s)
        plt.savefig('square_wave.png')
        plt.close()
        smtpserver.sendSqaureEmail(email)

    elif gentype == 'Triangle-Wave':
        t = np.arange(0, 1, 0.001)
        s = amplitude * signal.sawtooth(2 * pi * frequency * t, width=0.5)
        plt.plot(s)
        plt.savefig('triangle_wave.png')
        plt.close()
        smtpserver.sendTriangleEmail(email)

    elif gentype == 'Sawtooth-Wave':
        t = np.arange(0, 1, 0.001)
        s = amplitude * signal.sawtooth(2 * pi * frequency * t)
        plt.plot(s)
        plt.savefig('sawtooth_wave.png')
        plt.close()
        smtpserver.sendSawtoothEmail(email)

    return Response("Success")

@api_view(['POST'])
def handleGenFourier(request):
    fourierdata = request.data
    n_val = int(fourierdata.get('n-value'))
    email = fourierdata.get('email')
    print(str(email)+" "+str(n_val))
    x = np.arange(-np.pi,np.pi,0.001)
    y = square(x)
    fc = lambda x:square(x)*cos(i*x)
    fs = lambda x:square(x)*sin(i*x)
    n = n_val
    An = []
    Bn = []
    sum = 0
    for i in range(n):
        an = quad(fc,-np.pi,np.pi)[0]*(1.0/np.pi)
        bn = quad(fs,-np.pi,np.pi)[0]*(1.0/np.pi)
        An.append(an)
        Bn.append(bn)

    for i in range(n):
        if i == 0.0:
            sum = sum + An[i]/2
        else:
            sum = sum + (An[i]*np.cos(i*x)+Bn[i]*np.sin(i*x))

    plt.plot(x,sum,'g')
    plt.plot(x,y,'r--')
    plt.title('fourier series for square wave')
    plt.savefig('fourier_series.png')
    plt.close()
    smtpserver.sendFourierEmail(email)

    return Response("Success")