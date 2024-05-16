



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

class World:
    def __init__(self, size):
        self.size = size
        self.grid = [[None for i in range(size[1])] for _ in range(size[0])]

    def is_within_bounds(self, loc):
        return 0 <= loc[0] < self.size[0] and 0 <= loc[1] < self.size[1]

    def is_empty(self, loc):
        return self.is_within_bounds(loc) and self.grid[loc[0]][loc[1]] is None

    def place_agent(self, agent, loc):
        self.grid[loc[0]][loc[1]] = agent
        agent.location = loc

    def remove_agent(self, loc):
        self.grid[loc[0]][loc[1]] = None


class Agent():
    def __init__(self, world, spot = None):
        self.world = world
        self.spot = spot
        self.location = None
#Have agent move in random manner, LRUP if Vacant, stay if full        
    def move(self):
        possible_moves = [
            (self.location[0] - 1, self.location[1]),  # up
            (self.location[0] + 1, self.location[1]),  # down
            (self.location[0], self.location[1] - 1),  # left
            (self.location[0], self.location[1] + 1)   # right
        ]
        random.shuffle(possible_moves)
        for move in possible_moves:
            if self.world.is_empty(move):
                self.world.remove_agent(self.location)
                self.world.place_agent(self, move)
                break        
            
def initialize_world(param):
    world = World(param['world_size'])
    agents = [Agent(world) for i in range(param['num_agents'])]
    
    for agent in agents:
        while True:
            loc = (random.randint(0, param['world_size'][0] - 1), 
                   random.randint(0, param['world_size'][1] - 1))
            if world.is_empty(loc):
                world.place_agent(agent, loc)
                break
    
    return world, agents

def simulate(param):
    world, agents = initialize_world(param)
    
    for _ in range(param['max_iter']):
        for agent in agents:
            agent.move()
    
    return world

def save_world(world, path):
    data = []
    for i in range(world.size[0]):
        for j in range(world.size[1]):
            if world.grid[i][j] is not None:
                data.append({'x': i, 'y': j})
    
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)


world = simulate(param)
