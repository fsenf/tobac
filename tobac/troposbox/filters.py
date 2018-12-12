#!/usr/bin/env python


# Copyright (c) 2012- 2016

# TROPOS,
# Permoserstr. 15
# 04318 Leipzig, Germany. 

# Author:
# ====== 
# Fabian Senf <senf@tropos.de>


# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as 
# published by the Free Software Foundation; either version 3 of 
# the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.


import sys, copy

import numpy as np

try:
    import SimpleITK
except:
    print('SimpleITK not available.')


######################################################################
######################################################################

def curve_flow_filter(f, numberOfIterations = 5):

    '''
    Smoothing filter depending on isoline curvature. Interface for 
    curvature flow filter from simpleITK toolkit.

    USAGE
    =====
    f_sm = curve_flow_filter(f, numberOfIterations = 5)


    INPUT
    =====
    f: 2d field
    numberOfIterations: (optional) number of iterations, increases smooting effect


    OUTPUT
    ======
    f_sm: smoothed 2d field
    '''

    img = SimpleITK.GetImageFromArray(f)
    img_sm = SimpleITK.CurvatureFlow(img, numberOfIterations = numberOfIterations)
    
    f_sm = SimpleITK.GetArrayFromImage(img_sm)

    return f_sm
    

######################################################################
######################################################################
