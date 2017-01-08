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
        self.n = 100
        self.zeroVelocity = 2.3   # m/2
        self.height = 1       # m
        self.windSpeed = 2
        
        self.sHeight = None
        self.sSeeds = None
        self.sWindSpeed = None
        self.sZeroVelocity = None
        
        
    def calculateGauss(self):
        print 'in calculateGauss'
        
        
        for i in range(len(self.board)):
            y = np.abs(i - 25)
            
            #print 'i: ' +  str(i)
            print 'y: ' + str(y)
            
            
            for j in range(len(self.board[0])):
                x = j   # zeby nie zaczynac od same poczatku
                
                if x == 0:
                    x = 0.0001
                
                #print 'j ' +  str(j)
                print 'x: ' + str(x)
                
                frac1 = (self.n*self.zeroVelocity) / (2* np.pi  * self.windSpeed * self.yVariation(x) * self.zVariation(x))
                elem1 = - np.square(y) /  (2*np.square(self.yVariation(x)))
                elem2 = np.square(self.height - self.zeroVelocity *(x/self.windSpeed)) / (2*np.square(self.zVariation(x)))
                
                self.board[i][j] = frac1 * np.exp(elem1 - elem2)
                
                print 'board: ' + str(self.board[i][j])
        
        
        # powinno byc w okolicy 0.12 m/s    - plumed str 5
    def yVariation(self, x):
        A = 1 # wspl dyfuzji
       
        value = np.sqrt((2*A*np.abs(x))/self.windSpeed)
        return value
        
        # powinno byc w okolicy 0.5 m/s 
    def zVariation(self, x):    # to powinno wygladac jakos inaczej
        A = 2 # wspl dyfuzji
        
        value = np.sqrt((2*A*np.abs(x))/self.windSpeed)
        return value
        
        
    def onCalculateClick(self, event):
        print 'button clicked'
        self.calculateGauss()
        self.mat.set_data(self.board)

    
    def onResetClick(self, event):
        print 'reset clicked'
        
        if self.sSeeds != None and self.sHeight != None and self.sWindSpeed != None and self.sZeroVelocity != None:
            self.sSeeds.reset()
            self.sHeight.reset()
            self.sWindSpeed.reset()
            self.sZeroVelocity.reset()
        
            self.n = self.sSeeds.val
            self.height = self.sHeight.val
            self.windSpeed = self.sWindSpeed.val
            self.zeroVelocity = self.sZeroVelocity.val
        
            self.calculateGauss()
            self.mat.set_data(self.board)

    
    def onHeightChanged(self, val):
        self.height = val
        
    
    def onWindSpeedChanged(self, val):
        self.windSpeed = val
        
    
    def onZeroVelocityChanged(self, val):
        self.zeroVelocity = val
        
    def onSeedsNumChanged(self, val):
        self.n = val
     
        
    def start(self):
        
        self.fig, self.ax = plt.subplots()
        
        plt.subplots_adjust(left=0.1, bottom=0.35)
        plt.axis([0, 100, 0, 50])

        
        self.board[25][0] = 10
        
        self.mat = self.ax.matshow(self.board, cmap = plt.get_cmap('Greens'))
        
        
        axSeeds = plt.axes([0.25, 0.25, 0.63, 0.03])
        self.sSeeds = Slider(axSeeds, "Number of seeds", 50, 5000, valinit=self.n)
        self.sSeeds.on_changed(self.onSeedsNumChanged)
        
        axHeight = plt.axes([0.25, 0.2, 0.63, 0.03])
        self.sHeight = Slider(axHeight, "Height", 0.1, 50, valinit=self.height)
        self.sHeight.on_changed(self.onHeightChanged)
        
        axWindSpeed = plt.axes([0.25, 0.15, 0.63, 0.03])
        self.sWindSpeed = Slider(axWindSpeed, "Wind speed", 0.1, 25, valinit=self.windSpeed)
        self.sWindSpeed.on_changed(self.onWindSpeedChanged)
        
        axZeroVelocity = plt.axes([0.25, 0.1, 0.63, 0.03])
        self.sZeroVelocity = Slider(axZeroVelocity, "Free falling velocity", 0.07, 7, valinit=self.zeroVelocity)
        self.sZeroVelocity.on_changed(self.onZeroVelocityChanged)
        
        
        axCalculate = plt.axes([0.7, 0.02, 0.11, 0.06])
        bCalculate = Button(axCalculate, 'Calculate')
        bCalculate.on_clicked(self.onCalculateClick)
        
        axReset = plt.axes([0.85, 0.02, 0.11, 0.06])
        bReset = Button(axReset, 'Reset')
        bReset.on_clicked(self.onResetClick)
        
        self.onCalculateClick(None)
        

        
        plt.show()
        
        