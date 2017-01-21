'''
Created on 07.01.2017

@author: Mohru
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, Slider, RadioButtons

class Application(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        self.board = [[0 for _ in range(300)] for _ in range(50)]
        self.n = 100
        self.zeroVelocity = 2.3   # m/2
        self.height = 1       # m
        self.windSpeed = 2
        
        self.isBinary = False
        
        self.sHeight = None
        self.sSeeds = None
        self.sWindSpeed = None
        self.sZeroVelocity = None
        
        self.areas = [0 for _ in  range(61)]
        self.xs = [0 for _ in  range(61)]
        self.ys = [0 for _ in  range(61)]
        
    def calculateGauss(self):
        #print 'in calculateGauss'
        
        
        for i in range(len(self.board)):
            y = np.abs(i - 25)
            
            #print 'i: ' +  str(i)
            #print 'y: ' + str(y)
            
            
            for j in range(len(self.board[0])):
                x = j   # zeby nie zaczynac od same poczatku
                
                if x == 0:
                    x = 0.0001
                
                #print 'j ' +  str(j)
                #print 'x: ' + str(x)
                
                frac1 = (self.n*self.zeroVelocity) / (2* np.pi  * self.windSpeed * self.yVariation(x) * self.zVariation(x))
                elem1 = - np.square(y) /  (2*np.square(self.yVariation(x)))
                elem2 = np.square(self.height - self.zeroVelocity *(x/self.windSpeed)) / (2*np.square(self.zVariation(x)))
                
                self.board[i][j] = frac1 * np.exp(elem1 - elem2)
                
                #print 'board: ' + str(self.board[i][j])
        
        
        # powinno byc w okolicy 0.12 m/s    - plumed str 5
    def yVariation(self, x):
        A = 1 # wspl dyfuzji
       
        value = np.sqrt((2.0*A*np.abs(x))/self.windSpeed)
        return value
        
        # powinno byc w okolicy 0.5 m/s 
    def zVariation(self, x):    # to powinno wygladac jakos inaczej
        A = 2 # wspl dyfuzji
        
        value = np.sqrt((2.0*A*np.abs(x))/self.windSpeed)
        return value
         
         
    def binarize(self): 
        
        maxI = 0
        maxJ = 0
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):            
                if self.board[i][j] >= self.board[maxI][maxJ]:
                    maxI = i
                    maxJ = j
           
        for i in range(len(self.board)):
                    for j in range(len(self.board[0])):
                        
                        if self.board[i][j] >=1:
                            self.board[i][j]=1
                        else:
                            self.board[i][j]=0    
                            
        self.board[maxI][maxJ] = 1000
        
    #def onCalculateClick(self, event ''', ind'''):
    def onCalculateClick(self, event):
        #print 'button clicked'
        self.calculateGauss()
        
        if self.isBinary:
            self.binarize()
            
        self.mat.set_data(self.board)
        
        #self.computeArea(ind)
        self.computeArea()

                            
    def onResetClick(self, event):
        #print 'reset clicked'
        
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
            
            if self.isBinary:
                self.binarize()
            
            self.mat.set_data(self.board)

    
    def onHeightChanged(self, val):
        self.height = val
        
    
    def onWindSpeedChanged(self, val):
        self.windSpeed = val
        
    
    def onZeroVelocityChanged(self, val):
        self.zeroVelocity = val
        
    def onSeedsNumChanged(self, val):
        self.n = val
     
        
    def onDandelionClick(self, event):
        #print "onDandelionClick"
        if self.sSeeds != None and self.sHeight != None and self.sWindSpeed != None and self.sZeroVelocity != None:
            self.sSeeds.set_val(100)
            self.sHeight.set_val(0.2)
            self.sWindSpeed.reset()
            self.sZeroVelocity.set_val(0.5)
            self.onCalculateClick(None)
        
    
    def onMapleClick(self, event):
        if self.sSeeds != None and self.sHeight != None and self.sWindSpeed != None and self.sZeroVelocity != None:
            self.sSeeds.set_val(2000)
            self.sHeight.set_val(20)
            self.sWindSpeed.reset()
            self.sZeroVelocity.set_val(1.01)
            self.onCalculateClick(None)
    
    def onFirClick(self, event):
        if self.sSeeds != None and self.sHeight != None and self.sWindSpeed != None and self.sZeroVelocity != None:
            self.sSeeds.set_val(5000)
            self.sHeight.set_val(30)
            self.sWindSpeed.reset()
            self.sZeroVelocity.set_val(1.06)
            self.onCalculateClick(None)
            
    def onRadioClick(self, label):
        self.isBinary = (label == "Binary")
                    
        self.onCalculateClick(None)
        
        
    def computeArea(self):
        
    #    print str(self.windSpeed)
        
    #    if self.isBinary:
    #        print  str(sum([sum(i) for i in self.board]) -999) + ", "
    #        self.areas[ind] = sum([sum(i) for i in self.board]) -999
    #    else:
    #        print  str(sum([sum(i) for i in self.board])) + ", "
            
        
        maxX = 0
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] >=1 and j > maxX:
                    maxX = j
                
        
    #    print  str(maxX) + ", "
    #    self.xs[ind] = maxX
        
        maxY = 0
        
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] >=1 and i > maxY:
                    maxY = i
                
        
    #    print  str(maxY - 25) + ", "
    #    self.ys[ind] = (maxY - 25) *2
        
    #    print ""
        
    def start(self):
        
        self.fig, self.ax = plt.subplots(figsize=(15, 10))
        
        plt.subplots_adjust(left=0.2, bottom=0.35)
        plt.axis([0, 120, 0, 50])

        
        self.board[25][0] = 10
        
        self.mat = self.ax.matshow(self.board, cmap = plt.get_cmap('Greens'))
        
        plt.colorbar(self.mat, fraction=0.046, pad=0.04)
        self.ax.set_yticklabels(['']+['-15', '-5', '5', '15', '25'])
        
        self.ax.set_ylabel('y')
        self.ax.set_xlabel('x')
        
        axSeeds = plt.axes([0.3, 0.25, 0.63, 0.03])
        self.sSeeds = Slider(axSeeds, "Number of seeds", 50, 5000, valinit=self.n)
        self.sSeeds.on_changed(self.onSeedsNumChanged)
        
        axHeight = plt.axes([0.3, 0.2, 0.63, 0.03])
        self.sHeight = Slider(axHeight, "Height (m)", 0.1, 50, valinit=self.height)
        self.sHeight.on_changed(self.onHeightChanged)
        
        axWindSpeed = plt.axes([0.3, 0.15, 0.63, 0.03])
        self.sWindSpeed = Slider(axWindSpeed, "Wind speed (m/s)", 0.1, 21, valinit=self.windSpeed) # max 8 w skali Beauforta
        self.sWindSpeed.on_changed(self.onWindSpeedChanged)
        
        axZeroVelocity = plt.axes([0.3, 0.1, 0.63, 0.03])
        self.sZeroVelocity = Slider(axZeroVelocity, "Free falling velocity (m/s)", 0.07, 7, valinit=self.zeroVelocity)
        self.sZeroVelocity.on_changed(self.onZeroVelocityChanged)
        
        
        axCalculate = plt.axes([0.7, 0.02, 0.11, 0.06])
        bCalculate = Button(axCalculate, 'Calculate')
        bCalculate.on_clicked(self.onCalculateClick)
        
        axReset = plt.axes([0.85, 0.02, 0.11, 0.06])
        bReset = Button(axReset, 'Reset')
        bReset.on_clicked(self.onResetClick)
        
        
        axDandelion = plt.axes([0.03, 0.20, 0.11, 0.06])
        bDandelion = Button(axDandelion, 'Dandelion')
        bDandelion.on_clicked(self.onDandelionClick)
        
        axMaple = plt.axes([0.03, 0.15, 0.11, 0.06])
        bMaple = Button(axMaple, 'Maple')
        bMaple.on_clicked(self.onMapleClick)
        
        axFir = plt.axes([0.03, 0.10, 0.11, 0.06])
        bFir = Button(axFir, 'Fir')
        bFir.on_clicked(self.onFirClick)
        
        axMode = plt.axes([0.03, 0.6, 0.10, 0.15])
        rMode = RadioButtons(axMode, ('Standard', 'Binary'))
        rMode.on_clicked(self.onRadioClick)
        axMode.set_title("Mode")

        
        self.onCalculateClick(None)
        
        self.ax.set_title('Seed dispersal', y=1.08)
        
        '''
        self.onRadioClick("Binary")
        
        self.onDandelionClick(None)
        self.sSeeds.set_val(500)
        ind = 0
        
        for i in np.arange(1, 7.1, 0.1):
            self.sWindSpeed.set_val(i)
            self.onCalculateClick(None, ind)
            ind = ind +1
            
        print self.areas
        print self.xs
        print self.ys
            
        print ""
        
        self.onMapleClick(None)
        ind = 0
        
        for i in np.arange(1, 7.1, 0.1):
            self.sWindSpeed.set_val(i)
            self.onCalculateClick(None, ind)
            ind = ind +1
            
        print self.areas
        print self.xs
        print self.ys
        print ""
        
        self.onFirClick(None)
        ind = 0
        
        for i in np.arange(1, 7.1, 0.1):
            self.sWindSpeed.set_val(i)
            self.onCalculateClick(None, ind)
            ind = ind +1
        
        print self.areas
        print self.xs
        print self.ys
        '''
        
        plt.show()
        
        