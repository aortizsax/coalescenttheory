# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:20:50 2022

@author: aorti

This code creates a coalescent model for a set number of sampled nodes.

    Usage:
        python 3 coalescent_1.2.py
    
    Output: random example
    (((a:0.37,e:0.37)o:6.31,((g:0.17,k:0.17)n:3.04,m:3.21)u:3.46)w:17.3,((d:1.71,f:1.71)s:9.29,(((l:1.25,(h:0.61,j:0.61)p:0.64)r:1.08,(c:0.89,i:0.89)q:1.44)t:2.17,b:4.51)v:6.5)x:13.0)y;



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
            self.subtree="("+child1.subtree+":"+str(child1.edgelength)[:4]
            self.subtree+=","+child2.subtree+":"+str(child2.edgelength)[:4]+")"
            self.subtree+=name
        else:
            self.subtree=name

            
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



def nchoose2(n):
    '''
    performs n choose 2 math
    '''
    return ( n * ( n - 1 ) ) / 2 
    
def coalesce(n0,nodes,i):
    N = len(nodes)  # n0 - i +n0 ##i starts at n0 in this code
    Twaitn = n0 / nchoose2(N)  # can simplify if write out n choose 2
    Twaitn = round(Twaitn,2)
    
    #add wait time to all nodes 
    for Ni in nodes:
        Ni.edgelength+=Twaitn
    i+=1# add one for label
    ab = string.ascii_lowercase[i]
     
    if N >2:
        #which ramdom pair  
        r1 = random.sample(range(0,len(nodes)-1),2)
    else:
        #the last pair
        r1=[0,1]
        
    #pull random pair        
    coal1, coal2 = samplednodes[r1[0]], samplednodes[r1[1]]
    
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

    N = 10000000000000000000000000#infinity 
    n0 = 13

    samplednodes = [] #sampled nodes


    # Intitialize sampled nodes 
    for i in range(n0):
        ab = string.ascii_lowercase[i]
        samplednodes.append(Node(ab,0))


    #coalece until 2 theortical samples
    while len(samplednodes)>1:
        samplednodes, i = coalesce(n0,samplednodes,i)


    #set last theorical sample as root
    root = samplednodes[0]
    #initialize tree with root node as head
    tree = Tree(root)
    print(tree)
    

