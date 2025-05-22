# https://github.com/gwosc-tutorial/LOSC_Event_tutorial

import numpy as np
from scipy import signal

def optimal_snr(x:np.ndarray, template:np.ndarray, f:np.ndarray, psd:np.ndarray, fs:int=4096) -> np.ndarray:
  x_win = x*signal.windows.tukey(x.size, alpha=0.125)
  template_win = template*signal.windows.tukey(template.size, alpha=0.125)
  f_template = np.fft.fftfreq(template.size) * fs
  df = f_template[1] - f_template[0]
  psdi = np.interp(np.abs(f_template), f, psd)
  x_f = np.fft.fft(x_win) / fs
  template_f = np.fft.fft(template_win) / fs
  norm = np.sqrt(np.abs((template_f*np.conj(template_f)/psdi).sum()*df))
  optimal_SNR_f = x_f * np.conj(template_f) / psdi
  optimal_SNR_t = 2 * fs * np.fft.fftshift(np.fft.ifft(optimal_SNR_f)) / norm
  return np.abs(optimal_SNR_t)
