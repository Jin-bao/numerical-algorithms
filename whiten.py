# https://github.com/gwosc-tutorial/LOSC_Event_tutorial

import numpy as np
from scipy.interpolate import interp1d

def whiten(x:np.ndarray, f:np.ndarray, psd:np.ndarray, dt:float) -> np.ndarray:
  x_len = len(x)
  psdi = interp1d(f, psd)
  freq = np.fft.rfftfreq(x_len, dt)
  x_fd = np.fft.rfft(x)
  whitened_x_fd = np.sqrt(dt*2) * x_fd / np.sqrt(psdi(freq))
  whitened_x_td = np.fft.irfft(whitened_x_fd, n=x_len)
  return whitened_x_td
