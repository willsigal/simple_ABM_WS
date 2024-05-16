#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:51:14 2024

@author: willsigal
"""
import random 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#%% Agent based code
#Define agent attributes
param = {'world_size': (20,20),
         'num_agents':380,
         'max_iter'  :5,
         'out_path' : "/Users/willsigal/Documents/GitHub/simple_abm.csv"}

class Agent():
    def __init__(self, world, spot):
        self.world = world
        self.spot = spot
        self.location = None
#Have agent move in random manner, LRUP if Vacant, stay if full        
def Move(self): 
    vacancies =self.world.find_vacant(return_all = True)
    for patch in vacancies:
        i_moved = False
        will_i_like_it = self.is_empty(loc=patch)
        if is_empty is True:
                    self.world.grid[self.location] = None #move out of current patch
                    self.location = patch                 #assign new patch to myself
                    self.world.grid[patch] 
        i_moved = True
        
        return 1
    else:
        i_moved = False
        return 0
#Make Boolean for whether the spot the agent tries to move to is empty
def is_empty(self, loc, patch_check = False):
    if not loc:
        starting_loc = self.location
    else:
        starting_loc = loc
   neighbor_patches = self.locate_neighbors(starting_loc)
   neighbor_agents  = [self.world.grid[patch] for patch in neighbor_patches]
   
            





