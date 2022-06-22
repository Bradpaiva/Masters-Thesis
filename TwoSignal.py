import numpy as np
import matplotlib.pyplot as plt
from ssqueezepy import ssq_cwt, ssq_stft
from tqdm import tqdm
from SignalGen import *

Samples = 1500

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

# def MergeSignals(Signal1,Signal2,offset):
#     Signal1=np.array(Signal1).tolist()
#     Offset = [0] * (offset)
#     Merge1=np.append(Signal1,Offset)
#     Signal2=np.array(Signal2).tolist()
#     Merge2=np.append(Offset,Signal2)
#     Merge = Merge1+Merge2
#     t = np.linspace(0,
#             c.TotalTime+offset/c.SamplingFrequency, 
#             int(c.SamplingFrequency*(c.TotalTime+ offset/c.SamplingFrequency)))
#     if (len(Merge)>len(t)):
#         Merge=Merge[:-1]
#     return Merge, t

def MergeSignals(Signal1,Signal2,offset):
    Merge = Signal1 + Signal2
    t = np.linspace(0,c.TotalTime, c.SamplingFrequency*c.TotalTime)
    return Merge, t


def MergeTwo(Class1,Class2):
    Signal1=[]
    Signal2=[]
    Merge=[]

    del(Signal1)
    del(Signal2)
    del(Merge)

    options = {0 : RanAMSignal,
               1 : RanFMSignal,
               2 : RanASKSignal,
               3 : RanFSKSignal,
               4 : RanPSKSignal,
               5 : RanQPSKSignal,
               6 : RanQAM16Signal,
    }

    # offset = random.randrange(0, 2000)
    offset = 0
    CarrierFreq = RanCarrierFreq()
    Signal1, t, SamplingFrequency = options[Class1](CarrierFreq)
    Signal2,t, SamplingFrequency = options[Class2](CarrierFreq)
    Merge, t2 = MergeSignals(Signal1,Signal2,offset)
    return Merge

def MergeSpec():
    classes = {0 : 'AM',
               1 : 'FM',
               2 : 'ASK',
               3 : 'FSK',
               4 : 'PSK',
               5 : 'QPSK',
               6 : 'QAM16',
        }

    for i in range(6):
        for j in range (6):         
            for k in tqdm(range(Samples)):
                print('i=' +str(i))
                print('j=' +str(j))
                Merge = MergeTwo(i,j)
                plot.specgram(Merge,SamplingFrequency)
                if i<j :
                    name1 = i
                    name2 = j
                else :
                    name1 = j
                    name2 = i
                plot.savefig('Concurrent/'+str(classes[name1])+
                    str(classes[name2])+'/training'+str(k)+'.jpg')
    return

def MergeScal():
    classes = {0 : 'AM',
               1 : 'FM',
               2 : 'ASK',
               3 : 'FSK',
               4 : 'PSK',
               5 : 'QPSK',
               6 : 'QAM16',
        }

    for i in range(4,5):
        for j in range (4,5):
            print('i=' +str(i))
            print('j=' +str(j))       
            for k in tqdm(range(Samples)):
                Merge = MergeTwo(i,j)
                MergePlot=ScalogramSSQ(Merge)
                if i<j :
                    name1 = i
                    name2 = j
                else :
                    name1 = j
                    name2 = i
                filename = 'Concurrent/'+str(classes[name1])+str(classes[name2])+'/training'+str(k)+'.jpg'
                save_image(MergePlot,filename)
                del(MergePlot)
                del(Merge)
                
    return

MergeScal()