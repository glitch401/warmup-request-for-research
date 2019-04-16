# -*- coding: utf-8 -*-
from Support_Pack import generate_data

gd1=generate_data.generate_data(numberOfValues=10)

#getting the training bit and the parity label associated with the bits string 
X,y=gd1.get_xy()

