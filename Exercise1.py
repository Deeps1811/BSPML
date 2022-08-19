#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  1 15:10:06 2022

@author: chiaramarzi
"""

import matplotlib.pyplot as plt
import numpy as np


# Dirac delta
L = 10
nn = np.arange(-L,L+1)
N = len(nn)
d = np.zeros(N)
# to complete

# Heaviside signal
# to complete

# plots
f, axs = plt.subplots(2, 1, figsize=(10,10))
axes = axs.flatten()
axes[0].stem(nn, d)
axes[0].set(xlabel='time (s)', ylabel='Amplitude', title='Dirac delta')
axes[1].stem(nn, u3)
axes[1].set(xlabel='time (s)', ylabel='Amplitude', title='Translated heaviside function')


# Cosine
Tc = 
A = 
T = 
t=np.arange() # to complete
Ta = 0.001
ta= np.arange() # to complete

Omega = 0
ya = A*np.cos(Omega*ta)
y = A*np.cos(Omega*t)

f, axs = plt.subplots(5, 1, figsize=(10,10))
axes = axs.flatten()
axes[0].plot(ta, ya, color='red')
axes[0].set(xlabel='time (s)', ylabel='Amplitude')
axes[0].stem(t, y)
axes[0].set(xlabel='time (s)', ylabel='Amplitude', title = r'$\Omega = 0$')

Omega = np.pi/2
ya = A*np.cos(Omega*ta)
y = A*np.cos(Omega*t)
axes[1].plot(ta, ya, color='red')
axes[1].set(xlabel='time (s)', ylabel='Amplitude')
axes[1].stem(t, y)
axes[1].set(xlabel='time (s)', ylabel='Amplitude', title = r'$\Omega = \pi/2$')

# to continue
