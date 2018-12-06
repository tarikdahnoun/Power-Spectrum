#Day 18 Homework
#Homework 3
#Power Spectrum

import numpy as np
import pylab as py

A = np.loadtxt("C:\\Users\\dahno\\Documents\\PHY251\\Day 18\\Lesson18_Data.txt")
N=len(A)
dt=A[1,0]-A[0,0]
fn=np.fft.fftfreq(N/2, dt)
f0=0
fc= 1/(2*dt)

tdata=np.zeros(len(A))
Adata=np.zeros(len(A))

for i in range(len(A)):
    tdata[i]=A[i,0]
    Adata[i]=A[i,1]
    
A=np.fft.fft(Adata,norm="ortho")

P=np.zeros(N/2,dtype=complex)
for i in range(1,N/2-1):
    P[i]=(1./N**2)*((np.conj(A[i])**2)+(np.conj(A[-i])**2))
    
P[0]=(1./N**2)*(np.conj(A[0]))**2
P[N/2-1]=(1./N**2)*(np.conj(A[N/2]))**2

py.figure(1)
py.plot(tdata,Adata,"-")
py.title("Amplitudes")
py.xlabel("t", fontsize=16)
py.ylabel("A(t)", fontsize=16)
py.show()

py.figure(2)
py.plot(fn,P,"-")
py.title("Periodogram")
py.xlabel("f", fontsize=16)
py.ylabel("P(f)", fontsize=16)
py.show()

