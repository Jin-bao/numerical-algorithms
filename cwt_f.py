# https://paos.colorado.edu/research/wavelets/bams_79_01_0061.pdf

import numpy as np
from typing import Callable

def cwt_f(x:np.ndarray, psi_f:Callable, a:np.ndarray, dt:float) -> np.ndarray:
  N = x.size
  M = a.size
  x_cwt = np.zeros((M,N), dtype=np.complex64)
  f = np.fft.fftfreq(N,dt)
  x_f = np.fft.fft(x)
  for j in range(M):
    tmp = np.sqrt(a[j]/dt) * x_f * np.conj(psi_f(a[j]*f))
    x_cwt[j,:] = np.fft.ifft(tmp)
  return x_cwt
