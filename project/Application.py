'''
Created on 07.01.2017

@author: Mohru
'''

import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from matplotlib.widgets import Button, Slider

class Application(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.board = [[0 for _ in range(100)] for _ in range(50)]
        self.n = 1
        
        
    def calculateGauss(self):
        for i in len(self.board):
            y = np.abs(i - 25)
            
            for j in range(len(self.board[0])):
                x = j + 10
                
                self.board[i][j] = ((self.n*self.zeroVelocity) / \
                                    (2* np.pi * self.windSpeed * self.yVariation(x) * self.zVariation(x))) * \
                 np.exp((np.square(y*y)/(2*np.square(self.yVariation(x)))) - \
                        (np.square(self.height - self.zeroVelocity *(x/self.windSpeed))/(2*np.square(self.zVariation(x)))))
        
        
        
    def yVariation(self, x):
        A = 1 # wspl dyfuzji
        value = (2*A*x)/self.windSpeed
        return value
        
        
    def zVariation(self, x):    # to powinno wygladac jakos inaczej
        A = 2 # wspl dyfuzji
        value = (2*A*x)/self.windSpeed
        return value
        
        
    def onCalculateClick(self, event):
        self.calculateGauss()
        #self.mat = self.ax.matshow(self.board)
        self.mat = plt.matshow(self.board, cmap = plt.get_cmap('gray'))

    
    def onHeightChanged(self, val):
        self.height = val
        
    
    def onWindSpeedChanged(self, val):
        self.windSpeed = val
        
    
    def onZeroVelocityChanged(self, val):
        self.zeroVelocity = val
        
    
     
        
    def start(self):
        
        self.fig, self.ax = plt.subplots()
        
        plt.subplots_adjust(left=0.1, bottom=0.3)
        plt.axis([0, 100, 0, 50])

        
        #self.mat = self.ax.matshow(self.board)
        for i in range(len(self.board[0])):
            self.board[20][i] = 5
            self.board[40][i] = 0.5
            self.board[10][i] = 50
        
        self.mat = self.ax.matshow(self.board, cmap = plt.get_cmap('Greens'))
        
        
        axHeight = plt.axes([0.25, 0.1, 0.63, 0.03])
        sHeight = Slider(axHeight, "Height", 0.1, 100, valinit=0.1)
        sHeight.on_changed(self.onHeightChanged)
        
        axWindSpeed = plt.axes([0.25, 0.15, 0.63, 0.03])
        sWindSpeed = Slider(axWindSpeed, "Wind speed", 0.1, 100, valinit=0.1)
        sWindSpeed.on_changed(self.onWindSpeedChanged)
        
        axZeroVelocity = plt.axes([0.25, 0.2, 0.63, 0.03])
        sZeroVelocity = Slider(axZeroVelocity, "Free falling velocity", 0.1, 100, valinit=0.1)
        sZeroVelocity.on_changed(self.onZeroVelocityChanged)
        
        
        axCalculate = plt.axes([0.8, 0.02, 0.11, 0.06])
        bCalculate = Button(axCalculate, 'Calculate')
        bCalculate.on_clicked(self.onCalculateClick)
        
        '''
        fig, ax = plt.subplots()
        plt.subplots_adjust(left=0.25, bottom=0.25)
        t = np.arange(0.0, 1.0, 0.001)
        a0 = 5
        f0 = 3
        s = a0*np.sin(2*np.pi*f0*t)
        plt.axis([0, 1, -10, 10])
        '''
        
        plt.show()
        
        