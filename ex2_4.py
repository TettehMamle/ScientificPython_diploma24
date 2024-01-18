import numpy as np
from matplotlib import pyplot as plt

def Sequence(N):
    list = [0]
    i = 1
    while(i<N+1):
        a = list[i - 1] -i
        if a  > 0 and a not in list: 
           list.append(list[i - 1] -i)
        else:
            list.append(list[i - 1] +i)
        i = i +1     # n += 1
    return list
seq = Sequence(20)
for i in range(1, len(seq)):
    h = (seq[i] + seq[i-1])/2
    r = abs((seq[i] - seq[i-1]))/2
    x = np.linspace(seq[i], seq[i-1], 40)
    y = (-1)**i * np.sqrt(r**2 - (x-h)**2)
    plt.plot(x, y)
plt.savefig("Racaman plot.png") 