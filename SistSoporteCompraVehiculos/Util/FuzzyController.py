import skfuzzy as skf
import numpy as np
import matplotlib.pyplot as plt
'''
Created on 29/08/2014

@author: anibal
'''

Y_AXIS_LIM = [0.0, 1.1]

class FuzzyController:

    _instance = None
    
    def __init__(self):
        self._consumo = ConsumeMf()
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FuzzyController, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
class ConsumeMf:
    X = np.arange(10,100,1.0)
    
    def __init__(self):
        self._low = skf._membership.trapmf( self.X, [10,20,30,40] )
        self._midlow = skf._membership.trapmf( self.X, [30,40,50,60] )
        self._midhigh = skf._membership.trapmf( self.X, [60,70,80,90] )
        self._high = skf._membership.trapmf( self.X, [80,90,100,100] )
        
    @property
    def low(self):
        return self._low
    @property
    def midlow(self):
        return self._midlow
    @property
    def midhigh(self):
        return self._midhigh
    @property
    def high(self):
        return self._high
    @property
    def plot(self):
        img = plt.figure()
        ax = img.add_subplot(111)
        ax.plot( self.X, self.low )
        ax.plot( self.X, self.midlow )
        ax.plot( self.X, self.midhigh )
        ax.plot( self.X, self.high )
        ax.set_ylim(Y_AXIS_LIM)
        ax.legend(loc='upper center', shadow=True)
        return img
        
class MantenienceCostMf:
    X = np.arange(100.0,10000.0,0.5)
        
    def __init__(self):
        self._low = skf._membership.trapmf( self.X, [100.0,250.0,500.0,750.0] )
        self._midlow = skf._membership.trapmf( self.X, [500.0,750.0,1000.0,1500.0] )
        self._midhigh = skf._membership.trapmf( self.X, [1250.0,1750.0,2000.0,2500.0] )
        self._high = skf._membership.trapmf( self.X, [2000.0,3000.0,10000,10000] )
        
    @property
    def low(self):
        return self._low
    @property
    def midlow(self):
        return self._midlow
    @property
    def midhigh(self):
        return self._midhigh
    @property
    def high(self):
        return self._high
    @property
    def plot(self):
        img = plt.figure()
        ax = img.add_subplot(111)
        ax.plot( self.X, self.low )
        ax.plot( self.X, self.midlow )
        ax.plot( self.X, self.midhigh )
        ax.plot( self.X, self.high )
        ax.set_ylim(Y_AXIS_LIM)
        ax.legend(loc='upper center', shadow=True)
        return img
    
class PriceMf:
    X = np.arange(9000.0,150000.0,1.0)
        
    def __init__(self):
        self._accessible = skf._membership.trapmf( self.X, [9000.0,20500.0,32000.0,43500.0] )
        self._midlow = skf._membership.trapmf( self.X, [32000.0,43500.0,45000.0,55500.0] )
        self._midhigh = skf._membership.trapmf( self.X, [45500.0,55500.0,67000.0,78500.0] )
        self._high = skf._membership.trapmf( self.X, [67000.0,80500.0,150000,150000] )
        
    @property
    def accessible(self):
        return self._accessible
    @property
    def midlow(self):
        return self._midlow
    @property
    def midhigh(self):
        return self._midhigh
    @property
    def high(self):
        return self._high
    @property
    def plot(self):
        img = plt.figure()
        ax = img.add_subplot(111)
        ax.plot( self.X, self.accessible )
        ax.plot( self.X, self.midlow )
        ax.plot( self.X, self.midhigh )
        ax.plot( self.X, self.high )
        ax.set_ylim(Y_AXIS_LIM)
        ax.legend(loc='upper center', shadow=True)
        return img
    
class PowerMf:
    X = np.arange(50.0,500.0,1.0)
        
    def __init__(self):
        self._low = skf._membership.trapmf( self.X, [50.0,50.0,100.0,120.0] )
        self._midlow = skf._membership.trapmf( self.X, [100.0,150.0,180.0,200.0] )
        self._midhigh = skf._membership.trapmf( self.X, [170.0,250.0,300.0,350.0] )
        self._high = skf._membership.trapmf( self.X, [250.0,500.0,500.0,500.0] )
        
    @property
    def low(self):
        return self._low
    @property
    def midlow(self):
        return self._midlow
    @property
    def midhigh(self):
        return self._midhigh
    @property
    def high(self):
        return self._high
    @property
    def plot(self):
        img = plt.figure()
        ax = img.add_subplot(111)
        ax.plot( self.X, self.low )
        ax.plot( self.X, self.midlow )
        ax.plot( self.X, self.midhigh )
        ax.plot( self.X, self.high )
        ax.set_ylim(Y_AXIS_LIM)
        ax.legend(loc='upper center', shadow=True)
        return img
    
class DurabilityMf:
    X = np.arange(5.0,15.0,1.0)
        
    def __init__(self):
        self._low = skf._membership.trapmf( self.X, [5.0,5.0,6.0,10.0] )
        self._mid = skf._membership.trapmf( self.X, [7.0,9.0,10.0,12.0] )
        self._high = skf._membership.trapmf( self.X, [10.0,14.0,15.0,15.0] )
        
    @property
    def low(self):
        return self._low
    @property
    def mid(self):
        return self._mid
    @property
    def high(self):
        return self._high
    @property
    def plot(self):
        img = plt.figure()
        ax = img.add_subplot(111)
        ax.plot( self.X, self.low )
        ax.plot( self.X, self.mid )
        ax.plot( self.X, self.high )
        ax.set_ylim(Y_AXIS_LIM)
        ax.legend(loc='upper center', shadow=True)
        return img
    
class SalaryMf:
    X = np.arange(350.0,10000.0,1.5)
        
    def __init__(self):
        self._lowlvl = skf._membership.trapmf( self.X, [350.0,1100.0,1900.0,2700.0] )
        self._midlowlvl = skf._membership.trapmf( self.X, [1900.0,2700.0,3500.0,4300.0] )
        self._midhighlvl = skf._membership.trapmf( self.X, [4300.0,5100.0,6000.0,6800.0] )
        self._highlvl = skf._membership.trapmf( self.X, [6800.0,7600,8400,10000] )
        
    @property
    def low_level(self):
        return self._lowlvl
    @property
    def midlow_level(self):
        return self._midlowlvl
    @property
    def midhigh_level(self):
        return self._midhighlvl
    @property
    def high_level(self):
        return self._highlvl
    @property
    def plot(self):
        img = plt.figure()
        ax = img.add_subplot(111)
        ax.plot( self.X, self.low_level )
        ax.plot( self.X, self.midlow_level )
        ax.plot( self.X, self.midhigh_level )
        ax.plot( self.X, self.high_level )
        ax.set_ylim(Y_AXIS_LIM)
        ax.legend(loc='upper center', shadow=True)
        return img
    
class WorkingFamilyMembersMf:
    X = np.arange(1.0,10.0,1.0)
        
    def __init__(self):
        self._few = skf._membership.trapmf( self.X, [1.0,1.0,4.0,5.0] )
        self._many = skf._membership.trapmf( self.X, [5.0,6.0,10.0,10.0] )
        
    @property
    def few(self):
        return self._few
    @property
    def many(self):
        return self._many
    @property
    def plot(self):
        img = plt.figure()
        ax = img.add_subplot(111)
        ax.plot( self.X, self.few )
        ax.plot( self.X, self.many )
        ax.set_ylim(Y_AXIS_LIM)
        ax.legend(loc='upper center', shadow=True)
        return img
    
class SeatingCapacityMf:
    X = np.arange(2.0,10.0,1.0)
        
    def __init__(self):
        self._low = skf._membership.trapmf( self.X, [2.0,2.0,3.0,4.0] )
        self._mid = skf._membership.trapmf( self.X, [3.0,4.0,6.0,7.0] )
        self._high = skf._membership.trapmf( self.X, [6.0,7.0,10.0,10.0] )
        
    @property
    def low(self):
        return self._low
    @property
    def mid(self):
        return self._mid
    @property
    def high(self):
        return self._high
    @property
    def plot(self):
        img = plt.figure()
        ax = img.add_subplot(111)
        ax.plot( self.X, self.low )
        ax.plot( self.X, self.mid )
        ax.plot( self.X, self.high )
        ax.set_ylim(Y_AXIS_LIM)
        return img