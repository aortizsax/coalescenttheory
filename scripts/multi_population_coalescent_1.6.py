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
import copy
import re
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

class Population(Node):
    """
    Population class for Multi-population-coalescence 
    
    """
    def set_size(self,size=None):
        self.size = size
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
        coal1, coal2 = nodes[r1[0]], nodes[r1[1]]
    else:
        #set last pair        
        coal1, coal2 = nodes[0], nodes[1]
    
    #pop from array
    nodes.pop(nodes.index(coal1))
    nodes.pop(nodes.index(coal2))
    
    #create coalesced node
    tempparent = Node(ab,0,coal1,coal2)
    coal1.parent, coal2.parent = tempparent, tempparent
    
    #append coalesed sample
    nodes.append(tempparent)
    return nodes, i
    
def multiPopCoal(N,nodes,i,max_time,coal_time):
    '''
    coalescent method for random set of nodes 
    '''
    
    n = len(nodes)  # n0 - i +n0 ##i starts at n0 in this code
    Twaitn = N / nchoose2(n)  # can simplify if write out n choose 2
    
    Twaitn = round(Twaitn,2)
    
    #set trunc to false
    trunc_fin = False
    
    if Twaitn + coal_time > max_time: #truncate coalesce
        truncate_time = max_time - coal_time
        #add wait time to all nodes 
        for Ni in nodes:
            Ni.edgelength+=truncate_time
        trunc_fin = True
        return nodes, i, max_time, trunc_fin
    
    else: # continue coalescence
    
        #add wait time to all nodes 
        for Ni in nodes:

            Ni.edgelength+=Twaitn
        i+=1# add one for label
        ab = string.ascii_lowercase[i]
         
        if n >2:
            #which ramdom pair  
            r1 = random.sample(range(0,4-1),2) 
            #set random pair
            coal1, coal2 = nodes[r1[0]], nodes[r1[1]]
        else:
            #set last pair        
            coal1, coal2 = nodes[0], nodes[1]
        
        #pop from array
        nodes.pop(nodes.index(coal1))
        nodes.pop(nodes.index(coal2))
        
        #create coalesced node
        tempparent = Node(ab,0,coal1,coal2)
        coal1.parent, coal2.parent = tempparent, tempparent
        
        #append coalesed sample
        nodes.append(tempparent)
        
        return nodes, i, Twaitn+coal_time, trunc_fin
    
def find_parens(s):
    toret = {}
    pstack = []

    for i, c in enumerate(s):
        if c == '(':
            pstack.append(i)
        elif c == ')':
            if len(pstack) == 0:
                raise IndexError("No matching closing parens at: " + str(i))
            toret[pstack.pop()] = i

    if len(pstack) > 0:
        raise IndexError("No matching opening parens at: " + str(pstack.pop()))

    return toret


## driver
if __name__ == '__main__': 
    intLab = string.ascii_uppercase[3:] 
    pop_tree_str = '((A:100,B:100):100,C:200):50;' 
    
    ### READ TREE
    working_str = copy.copy(pop_tree_str)
    c = 0
    num_merge = 0
    print(find_parens(pop_tree_str))
    for i,j in find_parens(pop_tree_str).items():
        tmp_name = intLab[c]
        j = find_parens(pop_tree_str)[i]
        print(i,j)
        node_info = working_str[i+1:j]
        print('node',node_info)
        edge_info = working_str[j+1:]
        print('edge', edge_info)
        
        edge_len = re.split(',|;', edge_info)[0][1:]
        print('len',edge_len)
        
        
        if num_merge == 0:
            child1_info, child2_info = node_info[:].split(',')
            child1_name, child1_edge = child1_info.split(':')
            child2_name, child2_edge = child2_info.split(':')
            print(child1_name,child1_edge , child2_name,child1_edge)
            tmp_1 = Population(child1_name,child1_edge)
            print(tmp_1)
            tmp_2 = Population(child2_name,child2_edge)

            
            tmp_parent = Population(tmp_name,edge_len,tmp_1,tmp_2)
    #       tmp_parent.edge_length = edge_len
            print(tmp_parent)
            tmp_1.parent = tmp_parent
            tmp_2.parent = tmp_parent
            
            tmp_parent.child1, tmp_parent.child2 = tmp_1, tmp_2
            
            tmp_1 = copy.copy(tmp_parent)
        
        elif num_merge == 1:
            child2_index = -1 * ( node_info[::-1].find(',') + 1 )
            child2_info = node_info[child2_index:]
            child2_name, child2_edge = child2_info.split(':')
            child2_name = child2_name.replace(',','')
            print(child2_name,child2_edge)
            tmp_2 = Population(child2_name,child2_edge)
            tmp_parent = Population(tmp_name,edge_len,tmp_1,tmp_2)
            print(tmp_parent)
            tmp_1.parent = tmp_parent
            tmp_2.parent = tmp_parent
            
            tmp_parent.child1, tmp_parent.child2 = tmp_1, tmp_2
            
        num_merge += 1
        c+=1
        print()
    


    root = tmp_parent
    pop_tree = Tree(root) 
    print(pop_tree)
    #READ TREE END -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    print(pop_tree.inorder(pop_tree.head))
    print(pop_tree)
    
    
    
    
     
    N = 100#population size 
    n0 = 12#sample size 
    n00 = 4 # sample size per populations 
    num_pop = 3
    
    #Three Population coalescence
    samplednodes = [[]] #sampled nodes 
    for j in range(num_pop):
        samplednodes.append([])
    
    ii = 0
    # Intitialize sampled nodes with alphabet as names 
    for i in range(int(n0 / num_pop)):
        for j in range(num_pop):
            ab = string.ascii_lowercase[ii]
            samplednodes[i].append(Node(ab,0))
            ii += 1
    
    print(samplednodes)    
    
    
    
    #coalesce populations until time runs out 
    for sampled_population in samplednodes:
        #coalesce until 1 theorical sample 
        coal_time = 0
        pop_time = 50
        trunc_T = False
        while (len(sampled_population)>1)&(not trunc_T):
            print("sampled pop:",sampled_population)
            
            sampled_population, ii, coal_time, trunc_T = multiPopCoal(N,
                                                          sampled_population,
                                                          ii,pop_time,coal_time)

            print('remaining nodes', sampled_population,coal_time)
            
        #first append
        
        #set last theorically coalesced sample as root
        root = sampled_population[0]
        
        #initialize tree with root node as head
        tree = Tree(root)
        print(tree)
    
    
    
    
    
    
    
    # ONE Population coalescence  
    
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
    

