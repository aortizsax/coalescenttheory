# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:20:50 2022

@author: aorti
"""
import random
import string

### NODE

class Node:
    """
    
    """
    def __init__(self,name=None, Tw=None):
        self.name=name
        self.Tw=Tw
        self.parent=None
        self.child1=None
        self.child2=None
        
# =============================================================================
#     def __str__(self):
#         print(self.name)
# =============================================================================

# Coalesent tree 
class Tree:
    def __init__(self, fnode=None, gnode=None):
        pass
    #root


N = 10000000000000000000000000#infinity 
Twait = 10
n0 = 26

n0choose2 = n0 * ( n0 - 1 )
n0choose2 /= 2

def nchoose2(n):
    return ( n * ( n - 1 ) ) / 2 

samplednodes = [] #sampled nodes

for i in range(n0):
    ab = string.ascii_lowercase[i]
    samplednodes.append(Node(ab,Twait))
    #print(samplednodes[i].name)

while len(samplednodes)>2:
    N = len(samplednodes)
    Twaitn = #n / ncoohse2
    i+=1  
    r1 = random.sample(range(0,len(samplednodes)-1),2)
    #for n in samplednodes:
        #print(n.name)
    #print(r1,samplednodes[r1[0]].name, samplednodes[r1[1]].name)    
    ab = '('+samplednodes[r1[0]].name + ',' + samplednodes[r1[1]].name+')'
    #string.ascii_lowercase[i]
    
    coal1 = samplednodes[r1[0]]
    coal2 = samplednodes[r1[1]]
    
    samplednodes.pop(samplednodes.index(coal1))
    samplednodes.pop(samplednodes.index(coal2))
    samplednodes.append(Node(ab,Twait))
    i+=1

print('('+samplednodes[0].name+','+samplednodes[1].name+')')
