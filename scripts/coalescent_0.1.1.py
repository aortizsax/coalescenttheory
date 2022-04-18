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
    Node class for coalescing tree structure 
    """
    def __init__(self,name=None, edgelength=None,child1=None,child2=None):
        self.name=name
        self.edgelength=edgelength
        self.parent=None
        self.child1=child1
        self.child2=child2
    def __repr__(self):
        return self.name

# Coalesent tree 
class Tree:
    def __init__(self,head=None):
        self.head = head
        
    def __repr__(self):
        node = self.head 
        nodes = []
        while node is not None:
            nodes.append(str(node.edgelength)+"|"+node.name)
            node = node.child1
        nodes.append("None\n")
        node = self.head
        while node is not None:
            nodes.append(str(node.edgelength)+"|"+node.name)
            node = node.child2
        nodes.append("None")
        return " -> ".join(nodes)
    #root


N = 10000000000000000000000000#infinity 
Twait = 10
n0 = 14

n0choose2 = n0 * ( n0 - 1 )
n0choose2 /= 2

def nchoose2(n):
    return ( n * ( n - 1 ) ) / 2 

samplednodes = [] #sampled nodes




# Intitialize sampled nodes 
for i in range(n0):
    ab = string.ascii_lowercase[i]
    samplednodes.append(Node(ab,0))


#coalece until 2 theortical samples
while len(samplednodes)>2:
    N = len(samplednodes)
    Twaitn = N / nchoose2(N)
    #print('twait',Twaitn)#add this edge length to all nodes in samplednodes 
    for Ni in samplednodes:
        Ni.edgelength+=Twaitn
    i+=1  
    r1 = random.sample(range(0,len(samplednodes)-1),2)
    ab = string.ascii_lowercase[i]
    
    coal1 = samplednodes[r1[0]]
    coal2 = samplednodes[r1[1]]
    tempparent = Node(ab,0)
    coal1.parent = tempparent
    coal2.parent = tempparent
    tempparent.child1 = coal1
    tempparent.child2 = coal2
    
    samplednodes.pop(samplednodes.index(coal1))
    samplednodes.pop(samplednodes.index(coal2))
    samplednodes.append(tempparent)


#root node
ab = string.ascii_lowercase[i]
coal1,coal2 = samplednodes
root = Node(ab,0,coal1,coal2)
coal1.parent = root
coal2.parent = root


#initialize tree with root node as head
tree = Tree(root)
print(tree)




