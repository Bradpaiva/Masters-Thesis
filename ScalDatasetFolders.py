import numpy as np
import matplotlib.pyplot as plt
from ssqueezepy import ssq_cwt, ssq_stft
from tqdm import tqdm
from SignalGen import *




def Scalogram(x, classes, index=0):
    #%%# CWT + SSQ CWT ####################################
    TWx, Wx, *_ = ssq_cwt(x)
    filename= 'Scalogram/WxCWT/'+classes+'/WxCWT'+str(index)+'.png'
    save_image(Wx, filename)
    filename= 'Scalogram/TWxCWT/'+classes+'/TWxCWT'+str(index)+'.png'
    save_image(TWx, filename)
    #%%# STFT + SSQ STFT ##################################
    Tsx, Sx, *_ = ssq_stft(x)
    filename= 'Scalogram/TsxSTFT/'+classes+'/TsxSTFT'+str(index)+'.png'
    save_image(np.flipud(Tsx), filename)
    filename= 'Scalogram/SxSTFT/'+classes+'/SxSTFT'+str(index)+'.png'
    save_image(np.flipud(Sx), filename)


def save_image(data, filename):
    fig = plt.figure()
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(np.abs(data), aspect='auto', cmap='turbo')
    fig.savefig(filename, dpi= 100) 
    # plt.show()
    plt.close(fig)


def ScalDatasetGen():
    Signals = []
    Classes = []
    samples = 7000
    numclasses = 7
    for i in tqdm(range(int(samples/numclasses))):
        CarrierFreq = RanCarrierFreq()
        AM,t, SamplingFrequency= RanAMSignal(CarrierFreq)
        Scalogram(AM,'AM',index=i)
        del(AM)
    for i in tqdm(range(int(samples/numclasses))):
        CarrierFreq = RanCarrierFreq()
        FM,t, SamplingFrequency = RanFMSignal(CarrierFreq)
        Scalogram(FM, 'FM', index=i)
        del(FM)
    for i in tqdm(range(int(samples/numclasses))):
        CarrierFreq = RanCarrierFreq()
        ASK,t, SamplingFrequency = RanASKSignal(CarrierFreq)
        Scalogram(ASK,'ASK',index=i)
        del(ASK)
    for i in tqdm(range(int(samples/numclasses))):
        CarrierFreq = RanCarrierFreq()
        FSK,t, SamplingFrequency = RanFSKSignal(CarrierFreq)
        Scalogram(FSK,'FSK',index=i)
        del(FSK)
    for i in tqdm(range(int(samples/numclasses))):
        CarrierFreq = RanCarrierFreq()
        PSK,t, SamplingFrequency = RanPSKSignal(CarrierFreq)
        Scalogram(PSK,'PSK',index=i)
        del(PSK)
    for i in tqdm(range(int(samples/numclasses))):
        CarrierFreq = RanCarrierFreq()
        QPSK,t, SamplingFrequency = RanQPSKSignal(CarrierFreq)
        Scalogram(QPSK,'QPSK',index=i)
        del(QPSK)
    for i in tqdm(range(int(samples/numclasses))):
        CarrierFreq = RanCarrierFreq()
        QAM16,t, SamplingFrequency = RanQAM16Signal(CarrierFreq)
        Scalogram(QAM16,'QAM16',index=i)
        del(QAM16)
    return

ScalDatasetGen()

