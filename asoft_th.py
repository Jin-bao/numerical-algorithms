# 不对称软阈值处理

import numpy as np

def asoft_th(x:np.ndarray, lower:float, upper:float) -> np.ndarray:
  x = np.where((lower<=x)&(x<0), 0, x)
  x = np.where((0<x)&(x<=upper), 0, x)
  x = np.where(x<lower, x-lower, x)
  x = np.where(x>upper, x-upper, x)
  return x
