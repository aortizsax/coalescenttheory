# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:20:50 2022
FINAL 1 constant N_e
@author: aorti

This code creates a coalescent model for a set number of sampled nodes.

    Usage:
        python 3 coalescent_1.2.2.py
    
    Output: random example
        ((l:512820.53,k:512820.53)w:1333333.33,((((j:68376.07,d:68376.07)q:63492.07,h:131868.14)s:214285.72,(f:179487.19,((i:12820.51,c:12820.51)n:83333.34,e:96153.85)r:83333.34)t:166666.66999999998)v:500000.0,((b:46153.85,m:46153.85)p:200000.01,(g:27972.03,a:27972.03)o:218181.83000000002)u:600000.0)x:1000000.0)y;


##add sister

"""
import random
import string
import math

### NODE
class Node:
    """
    Node class for coalescing tree structure 
    """
    #constructor
    def __init__(self,name=None, edgelength=None,child1=None,child2=None):
        self.name=name
        self.edgelength=edgelength
        self.parent=None
        self.child1=child1
        self.child2=child2
        
        #set subtree as newick string of the subtree subtending from this node
        if (self.child1 is not None) & (self.child2 is not None):
            self.subtree="("+child1.subtree+":"+str(child1.edgelength)
            self.subtree+=","+child2.subtree+":"+str(child2.edgelength)+")"
            self.subtree+=name
        else:
            self.subtree=name+':'+str(self.edgelength)

            
    def __repr__(self):
        return self.name

# Coalesent tree 
class Tree:
    """
    Tree class for coalescing process
    """
    #constructor
    def __init__(self,head=None):
        self.head = head
    
    def inorder(self,node):
        #return if the tree is empty
        if (node is None):
            return 
        
        #traverse the left subtree
        self.inorder(node.child1)
        print(node.name,end=' ')
        self.inorder(node.child2)
    

    #printing tree representation
    def __repr__(self):
        print(self.head.subtree+';')
        
        #printing tree representation
    def __str__(self):
        return self.head.subtree +';'

class Population(Node):
    """
    Population class for Multi-population-coalescence 
    
    """
    #constructor 
#    def __init__(self):
#        Node.__init__(self)
#        pass
    
def nchoose2(n):
    '''
    performs n choose 2 math
    '''
    return ( n * ( n - 1 ) ) / 2 
    
def coalesce(N,nodes,i):
    '''
    coalescent method for random set of nodes 
    '''
    
    n = len(nodes)  # n0 - i +n0 ##i starts at n0 in this code
    Twaitn = N / nchoose2(n)  # can simplify if write out n choose 2
    
    Twaitn = round(Twaitn,2)
    
    #add wait time to all nodes 
    for Ni in nodes:
        Ni.edgelength+=Twaitn
    i+=1# add one for label
    ab = string.ascii_lowercase[i]
     
    if n >2:
        #which ramdom pair  
        r1 = random.sample(range(0,4-1),2)
        #set random pair
        coal1, coal2 = samplednodes[r1[0]], samplednodes[r1[1]]
    else:
        #set last pair        
        coal1, coal2 = samplednodes[0], samplednodes[1]
    
    #pop from array
    samplednodes.pop(samplednodes.index(coal1))
    samplednodes.pop(samplednodes.index(coal2))
    
    #create coalesced node
    tempparent = Node(ab,0,coal1,coal2)
    coal1.parent, coal2.parent = tempparent, tempparent
    
    #append coalesed sample
    nodes.append(tempparent)
    return nodes, i
    
## driver
if __name__ == '__main__':
    intLab = string.ascii_lowercase[3:]
    pop_tree_str = '((A:100,B:100):100,C:200):50;'
    
    lastEdge = pop_tree_str.split(':')[-1][:-1]
    pop_tree = Tree(Node('D',lastEdge))
    for subtree in pop_tree_str.split(','):
        print(subtree)
        print('child of:',subtree.count('('))
        print('up back:',subtree.count(')'))
    print(pop_tree,lastEdge)
    
    
    N = 100#population size 
    n0 = 12#sample size
    samplednodes = [] #sampled nodes


    # Intitialize sampled nodes with alphabet as names
    for i in range(n0):
        ab = string.ascii_lowercase[i]
        samplednodes.append(Node(ab,0))


    #coalesce until 1 theorical sample 
    while len(samplednodes)>1:
        samplednodes, i = coalesce(N,samplednodes,i)


    #set last theorically coalesced sample as root
    root = samplednodes[0]
    
    #initialize tree with root node as head
    tree = Tree(root)
    print(tree)
    

