
import matplotlib.pyplot as plt
import numpy as np

def plott(lamda, Omega, length, t):
    
    L = length
    R = Omega
    lamda = lamda
    g=9.8 
    # we will take the value of C1 and C2 to be equal to 1
    k_1=1
    k_2=1  
    
    a=np.exp(1j*(np.sqrt(g/L)*t))
    b=np.exp(1j*((-1)*np.sqrt(g/L)*t))
    c=np.exp(1j*(R*np.sin(lamda)*(-1)*t))

    u=(k_1*a+k_2*b)*c
    
    ## separating the real part 
    x=u.real
    y=u.imag
    
    plt.plot(x,y,'g')
    plt.grid()