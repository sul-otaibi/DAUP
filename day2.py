import numpy as np
import matplotlib.pyplot as plt

def subPlotSetup(title:str=None, funcName:str=None, function=None, lineStyle:str='-r'):
    '''Helper function to setup subplots in matplotlib.pyplot'''
    plt.title(title)
    plt.xlabel('x axis')
    plt.ylabel('y axis')
    plt.grid()
    plt.plot(x, function, lineStyle)
    plt.legend([funcName])

x = np.linspace(1, 30, 1000)
yLog10x = np.log10(x)

x = np.linspace(-30, 30, 1000)
yEx = np.e ** x
yLinearx = 2 * x 
yCoshx = np.cosh(x)

plt.figure('DAUP - Assignment 2', figsize=(16,5))

plt.subplot(1, 4, 1)
subPlotSetup('Logarithm function', 'y = log10(x)', yLog10x, '-r')

plt.subplot(1, 4, 2)
subPlotSetup('exponential function', 'y = $e^{x}$', yEx, '-g')

plt.subplot(1, 4, 3)
subPlotSetup('Linear function', 'y = ax', yLinearx, '-b')

plt.subplot(1, 4, 4)
subPlotSetup('Hyperbolic Function', 'y = cosh(x)', yCoshx, '-k')

plt.subplots_adjust(wspace=0.5)
plt.savefig('fig.png')
plt.show()