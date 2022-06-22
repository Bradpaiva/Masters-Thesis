import numpy as np
import matplotlib.pyplot as plt
from ssqueezepy import ssq_cwt, ssq_stft
from tqdm import tqdm
from SignalGen import *


def ScalogramSSQ(x):
    Tsx, Sx, *_ = ssq_stft(x)
    return Sx

def show_image(data):
    fig = plt.figure()
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(np.abs(data), aspect='auto', cmap='turbo')
    plt.show()

def save_image(data, filename):
    fig = plt.figure()
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(np.abs(data), aspect='auto', cmap='turbo')
    fig.savefig(filename, dpi= 100) 
    plt.close(fig)

def ScalDatasetGen():
    Signals = []
    Classes = []
    samples = 1
    numclasses = 1
    for i in tqdm(range(int(samples/numclasses))):
        CarrierFreq = RanCarrierFreq()
        AM,t, SamplingFrequency= RanAMSignal(CarrierFreq)
        ASK,t, SamplingFrequency = RanASKSignal(CarrierFreq)
        Combine = AM + ASK
        SSQ=ScalogramSSQ(Combine)
        show_image(SSQ)
        del(AM)
        del(ASK)
        del(Combine)
    # for i in tqdm(range(int(samples/numclasses))):
    #     FM,t, SamplingFrequency = RanFMSignal()
    #     Scalogram(FM, 'FM', index=i)
    #     del(FM)
    # for i in tqdm(range(int(samples/numclasses))):
    #     ASK,t, SamplingFrequency = RanASKSignal()
    #     Scalogram(ASK,'ASK',index=i)
    #     del(ASK)
    # for i in tqdm(range(int(samples/numclasses))):
    #     FSK,t, SamplingFrequency = RanFSKSignal()
    #     Scalogram(FSK,'FSK',index=i)
    #     del(FSK)
    # for i in tqdm(range(int(samples/numclasses))):
    #     PSK,t, SamplingFrequency = RanPSKSignal()
    #     Scalogram(PSK,'PSK',index=i)
    #     del(PSK)
    # for i in tqdm(range(int(samples/numclasses))):
    #     QPSK,t, SamplingFrequency = RanQPSKSignal()
    #     Scalogram(QPSK,'QPSK',index=i)
    #     del(QPSK)
    # for i in tqdm(range(int(samples/numclasses))):
    #     QAM16,t, SamplingFrequency = RanQAM16Signal()
    #     Scalogram(QAM16,'QAM16',index=i)
    #     del(QAM16)
    # return

ScalDatasetGen()



