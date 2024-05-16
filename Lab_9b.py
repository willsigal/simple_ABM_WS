#Will Sigal 6a

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)
#%%
def winner (p1, p2):
    if p1 ==p2:
        return 'tie'
    elif(p1 == 'rock' and p2 == 'scissors') or \
         (p1 == 'paper' and p2 == 'rock') or \
         (p1 == 'scissors' and p2== 'paper'):
        return 'p1'
    else:
        return 'p2'
    
#%% Play a round

def game():
    p1 = input('Choose rock, paper, or scissors:')
    p2 = random.choice(choices)
    print(f'computer chooses {p2}')
    result = winner(p1, p2)
    if result == 'tie':
       print("It's a tie!")
    elif result == 'p1':
       print("Player 1 wins!")
    else:
       print("Computer wins!")
    return result

game()

#%% Loop play

def multi_game(num_players, num_loops):
    results = {'p1_wins': 0, 'p2_wins': 0, 'ties': 0}
    for i in range(num_loops):
        result = game()
        if result == 'p1':
            results['p1_wins'] += 1
        elif result == 'p2':
            results['p2_wins'] += 1
        else:
            results['ties'] += 1
    print(f"Results after {num_loops} rounds: {results}")
    return results

multi_game(2, 5)

#%% multi player
def main():
    num_players = int(input("Enter the number of human players (0, 1, or 2): "))
    if num_players not in [0, 1, 2]:
        print("Invalid number of players. Must be 0, 1, or 2.")
        return
    num_loops = int(input("Enter the number of rounds to play: "))
    multi_game(num_players, num_loops)
    
main()



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
