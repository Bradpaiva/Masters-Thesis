import numpy as np
import pylab as pl
import matplotlib.pyplot as plot
# import scipy.signal.signaltools as sigtool
# import scipy.signal as signal
# from numpy.random import sample
import random

TotalTime = 1
CarrierFreqMin = 10
CarrierFreqMax = 100
SamplingFrequency = 1000
BinaryFrequency = 100 #SamplingFrequency/c.BinaryFrequency must be int
Fdev = 50   #frequency deviation, make higher than bitrate
NoiseRatio = .1
samples = 100

barker2= [1,0]
barker3= [1,1,0]
barker4= [1,1,0,1]
barker5= [1,1,1,0,1]


Barker = barker3

t = np.linspace(0,TotalTime, SamplingFrequency*TotalTime)
fc = random.randint(CarrierFreqMin,CarrierFreqMax)

BarkerCode=np.zeros(TotalTime*SamplingFrequency)

BinaryFrequency = len(Barker)/TotalTime

x1 = np.sin(2 * np.pi * fc * t)
x2 = -1*np.sin(2 * np.pi * fc * t)

tb = SamplingFrequency/BinaryFrequency
t1=0
t2=tb
for n in range(int(BinaryFrequency)*TotalTime):
    if (Barker[n] == 1):
        BarkerCode[int(t1):int(t2)]=x1[int(t1):int(t2)]
    elif(Barker[n] == 0):
        BarkerCode[int(t1):int(t2)]=x2[int(t1):int(t2)]
    t1=t1+tb
    t2=t2+tb

plot.plot(t,BarkerCode)
plot.show()

AutoCorelation = np.convolve(BarkerCode, BarkerCode, mode='full')

t= np.linspace(0, 2,len(AutoCorelation))
plot.plot(t,AutoCorelation)
plot.show()





