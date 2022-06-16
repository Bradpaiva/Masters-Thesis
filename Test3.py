import numpy as np
import matplotlib.pyplot as plt
from ssqueezepy import ssq_cwt, ssq_stft
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
    fig.savefig(filename, dpi=data.shape[0]) 
    plt.show()
    plt.close(fig)


x,t,sf = RanASKSignal()
Scalogram(x,'ASK',0)




# N=sf*c.TotalTime
# xo = np.cos(2 * np.pi * 2 * (np.exp(t / 2.2) - 1))
# xo += xo[::-1]  # add self reflected
# x = xo + np.sqrt(2) * np.random.randn(N)  # add noise




#%%# CWT + SSQ CWT ####################################
# Twxo, Wxo, *_ = ssq_cwt(xo)
# viz(xo, Twxo, Wxo)



# Twx, Wx, *_ = ssq_cwt(x)
# viz(x, Twx, Wx)

#%%# STFT + SSQ STFT ##################################
# Tsxo, Sxo, *_ = ssq_stft(xo)
# viz(xo, np.flipud(Tsxo), np.flipud(Sxo))

# Tsx, Sx, *_ = ssq_stft(x)
# viz(x, np.flipud(Tsx), np.flipud(Sx))