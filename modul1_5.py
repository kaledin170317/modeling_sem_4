
import numpy as np
from scipy.fftpack import rfft, irfft, fftfreq
import pylab as plt

time = np.linspace(0,100,100000)
signal = np.load('signal_1.npy')
W = fftfreq(signal.size, d=time[1]-time[0])
f_signal = abs(rfft(signal))


cut_f_signal_1 = f_signal.copy()
cut_f_signal_2 = f_signal.copy()
cut_f_signal_3 = f_signal.copy()


ma = max(cut_f_signal_1)
for i in range(0,len(cut_f_signal_1)):
    if cut_f_signal_1[i] < ma:
        cut_f_signal_1[i] = 0

cut_f_signal_2[cut_f_signal_2.argmax()] = 0
ma = max(cut_f_signal_2)
for i in range(0,len(cut_f_signal_2)):
    if cut_f_signal_2[i] < ma:
        cut_f_signal_2[i] = 0

cut_f_signal_3[cut_f_signal_3.argmax()] = 0
cut_f_signal_3[cut_f_signal_3.argmax()] = 0
ma = max(cut_f_signal_3)
for i in range(0,len(cut_f_signal_3)):
    if cut_f_signal_3[i] < ma:
        cut_f_signal_3[i] = 0


cut_signal_1 = irfft(cut_f_signal_1)
cut_signal_2 = irfft(cut_f_signal_2)
cut_signal_3 = irfft(cut_f_signal_3)


plt.subplot(421)
plt.title("Входной сигнал")
plt.plot(time[:100],signal[:100])

plt.subplot(422)
plt.title("Преобразование Фурье")
plt.plot(W,f_signal)

plt.subplot(423)
plt.title("Частота 1")
plt.plot(W,cut_f_signal_1)

plt.subplot(424)
plt.title("Обратное преобразование")
plt.plot(time[:100],cut_signal_1[:100])

plt.subplot(425)
plt.title("Частота 2")
plt.plot(W,cut_f_signal_2)

plt.subplot(426)
plt.title("Обратное преобразование")
plt.plot(time[:100],cut_signal_2[:100])

plt.subplot(427)
plt.title("Частота 3")
plt.plot(W,cut_f_signal_3)

plt.subplot(428)
plt.title("Обратное преобразование")
plt.plot(time[:100],cut_signal_3[:100])

plt.tight_layout()
plt.show()