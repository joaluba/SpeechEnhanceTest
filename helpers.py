
import matplotlib.pyplot as plt
import numpy as np 
import librosa 



def set_level(sig_in,L_des):
    # set FS level of the signal
    sig_zeromean=np.subtract(sig_in,np.mean(sig_in,axis=0))
    sig_norm_en=sig_zeromean/np.std(sig_zeromean.reshape(-1))
    sig_out =sig_norm_en*np.power(10,L_des/20)
    #print(20*np.log10(np.sqrt(np.mean(np.power(sig_out,2)))))
    return sig_out

def set_snr(s,n,snr):
    # set snr between signal and noise
    s=set_level(s,-30)
    n=set_level(n,-30+snr)
    return s,n

def plot_spectrogram(y, fs, title=None, ylabel="freq_bin"):
    D = np.abs(librosa.stft(y))
    D_db = librosa.amplitude_to_db(D, ref=np.max)
    librosa.display.specshow(D_db, sr=fs, x_axis='time', y_axis='log')
    plt.title(title)