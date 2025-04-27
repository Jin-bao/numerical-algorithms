# https://paos.colorado.edu/research/wavelets/bams_79_01_0061.pdf

import numpy as np
from typing import Callable

def cwt_t(x:np.ndarray, psi_t:Callable, a:np.ndarray, dt:float) -> np.ndarray:
  N = x.size
  M = a.size
  x_cwt = np.zeros((M,N), dtype=np.complex64)
  tmpb = (np.arange(N)-N//2) * dt
  for j in range(M):
    t = tmpb / a[j]
    psi = np.sqrt(dt/a[j]) * np.conj(psi_t(t))
    x_cwt[j,:] = np.convolve(x, psi, mode='same')
  return x_cwt

# 三层 for 循环的低效率版本
# def cwt_t(x:np.ndarray, psi_t:Callable, a:np.ndarray, dt:float) -> np.ndarray:
  # N = x.size
  # M = a.size
  # x_cwt = np.zeros((M,N), dtype=np.complex64)
  # for j in range(a.size):
  #   norm = np.sqrt(dt/a[j])
  #   for n in range(x.size):
  #     for p in range(x.size):
  #       x_cwt[j,n] += x[p] * norm * psi_t((p-n)*dt/a[j])
  # return x_cwt
