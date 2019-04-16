# -*- coding: utf-8 -*-
import numpy

class generate_data:
    
    def __init__(self,length=0,numberOfValues=100000):
        #constructor
        if length==0:
            self.length=50
        else:
            
        self.numberOfValues=numberOfValues
        self.binary_strings=[]
        self.parity=[]
        self.get_data()
    
    def get_data(self):
        '''
        this function generates 100,000 binary strings
        of length given or by default 50
        '''
        length=50#self.length
        for i in range(self.numberOfValues):
            arr = numpy.random.randint(2, size=(length,))
            stri=''
            for xi in arr:
                stri+=str(xi)
            self.binary_strings.append(stri)
            self.parity.append(self.find_partiy(stri))
    
    def find_partiy(self,bits):
        '''
        this function is to find the parity of the binary string formed
        returns 1 is even parity and 0 if odd parity
        '''
        
        count_1=0
        for x in bits:
            if int(x)==1:
                count_1+=1
        
        if count_1%2==0:
            return 1
        
        return 0
    
    def get_xy(self):
        return self.binary_strings,self.parity
    
                
            
        