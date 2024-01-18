import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0,5,100)
y1 = np.sin(x)
y2 = np.cos(x**3+1)
y3 = np.tan(x+1)
y4 = np.tanh(2*x**3)
y5 = np.log(x**4+ 2)
y6 = np.exp(x + 1)

# now we decide the actual figure size in inches
fig = plt.figure(figsize=(14,7))

plt.suptitle('Trigonometric Functions',fontweight='bold', fontsize='x-large')
plt.subplots_adjust(hspace=0.3, top=0.8) 
# create subplots 231 means make a 2x3 grid and this is the first plot

plt.subplot(231)
#these are here to show that you can do the same here as for a single plot
plt.title('A plot of Sin function',fontsize = 'large',fontstyle='italic',fontweight='bold')
plt.ylabel('sin(x)',fontsize = 'xx-large',fontstyle='oblique',fontweight = 'heavy')
plt.xlabel('$x$ axis(m)',fontsize = 'xx-large',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y1,color='r')

plt.subplot(232)
plt.title('A plot of Cos function',fontsize = 'large',fontstyle='italic',fontweight='bold')
plt.ylabel('cos(x**3+1)',fontsize = 'xx-large',fontstyle='oblique',fontweight = 'heavy')
plt.xlabel('$x$ axis(m)',fontsize = 'xx-large',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y2,color='g')

plt.subplot(233)
plt.title('A plot of Tan function',fontsize = 'large',fontstyle='italic',fontweight='bold')
plt.ylabel('tan(x+1)',fontsize = 'xx-large',fontstyle='oblique',fontweight = 'heavy')
plt.xlabel('$x$ axis(m)',fontsize = 'xx-large',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y3,color='b')

plt.subplot(234)
plt.title('A plot of Tanh function',fontsize = 'large',fontstyle='italic',fontweight='bold')
plt.ylabel('tanh(2*x**3)',fontsize = 'xx-large',fontstyle='oblique',fontweight = 'heavy')
plt.xlabel('$x$ axis(m)',fontsize = 'xx-large',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y4,color='y')

plt.subplot(235)
plt.title('A plot of Log function',fontsize = 'large',fontstyle='italic',fontweight='bold')
plt.ylabel('log(x**4+ 2)',fontsize = 'xx-large',fontstyle='oblique',fontweight = 'heavy')
plt.xlabel('$x$ axis(m)',fontsize = 'xx-large',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y5,color='c')

plt.subplot(236)
plt.title('A plot of an Exponential function',fontsize = 'large',fontstyle='italic',fontweight='bold')
plt.ylabel('exp(x + 1)',fontsize = 'xx-large',fontstyle='oblique',fontweight = 'heavy')
plt.xlabel('$x$ axis(m)',fontsize = 'xx-large',fontstyle='normal',fontweight = 'medium')
plt.plot(x,y6,color='m')
# removed extra white space
plt.tight_layout()
#plt.show()
plt.savefig("Trig functions(plot).pdf") 