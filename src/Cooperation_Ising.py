# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 13:01:20 2022

@author: qed_g
"""

from random import sample
from numpy.random import uniform
from numpy import linspace

class Thermodynamic:
    def __init__(self, N, a, b1, b2, graph='lattice'):
        self.total = N**2
        self.labels = [i for i in range(self.total)]
        RndInit = [(x <= 0.5) for x in uniform(0,1,N)]
        Init = ['C' if x else 'D' for x in RndInit]
        self.actions = {i : Init[i] for i in range(N)}
        self.a = a
        self.b1 = b1
        self.b2 = b2
        
        if 'lattice' in graph:
            self.Neighborhoods = self.Lattice(N)
    
    def Lattice(self, N):
        '''Lexicographic labeling (by rows)'''
        neighborhoods = {}
        for l in self.labels:
            up = (l-1) % self.total
            down = (l+1) % self.total
            left = (l-N) % self.total
            right = (l+N) % self.total
            Nl = { l : [up, down, left, right]}
            neighborhoods = {**neighborhoods, **Nl}
        return neighborhoods
    
    def SingleFlipSpin(self):
        '''Page 195, Chapter 6'''
        agent = sample(self.labels, 1)
        adversaries = sample(self.Neighborhoods[agent], 2)
        oponent = adversaries[0]
        third = adversaries[-1]
        
        action_a = self.actions[agent]
        action_o = self.actions[oponent]
        action_t = self.actions[third]
        
        u = uniform()
        if 'C' in action_a and 'D' in action_o:
            if u < self.a:
                self.actions[agent] = 'D'
        elif 'D' in action_a and 'C' in action_o:
            if 'C' in action_t:
                if u < self.b1:
                    self.actions[agent] = 'C'
            else:
                if u < self.b2:
                    self.actions[agent] = 'C'
        else:
            pass
            

b2 = 0.66
c = linspace(0, 0.99, 100) / b2
r = linspace(0, 0.99, 100) / b2

MC_Steps = int(1e6)