# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:20:50 2022

@author: aorti
"""
import random
import string
import math

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
        if (self.child1 is not None) & (self.child2 is not None):
            self.subtree="("+child1.subtree+":"+str(child1.edgelength)[:6]
            self.subtree+=","+child2.subtree+":"+str(child2.edgelength)[:6]+")"
            self.subtree+=name
        else:
            self.subtree=name

            
    def __repr__(self):
        return self.name

# Coalesent tree 
class Tree:
    """
    Tree class for coalesing
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
        print(self.head.subtree)
        node = self.head 
        nodes = []
        while node.child1 is not None:
            nodes.append(str(node.edgelength)+"|"+node.name)
            node = node.child1
        nodes.append(str(node.edgelength)+"|"+node.name)
        
        while node.parent is not None:
            node = node.parent
            nodes.append(node.name+"|"+str(node.edgelength))
        nodes.append(node.name+"|"+str(node.edgelength))
        return " -> ".join(nodes)


def nchoose2(n):
    return ( n * ( n - 1 ) ) / 2 
    
## driver
if __name__ == '__main__':

    N = 10000000000000000000000000#infinity 
    Twait = 10
    n0 = 13
    n0 = 4
    n0 = 13
    #n0 = 13

    samplednodes = [] #sampled nodes


    # Intitialize sampled nodes 
    for i in range(n0):
        ab = string.ascii_lowercase[i]
        samplednodes.append(Node(ab,0))


    #coalece until 2 theortical samples
    while len(samplednodes)>2:
        N = len(samplednodes)
        Twaitn = n0 / nchoose2(N)
        Twaitn = round(Twaitn,4)
        #Twaitn *= 100
        #Twaitn = math.floor(Twaitn)
        #Twaitn /= 100
        
        #print('twait',Twaitn)#add this edge length to all nodes in samplednodes 
        for Ni in samplednodes:
            Ni.edgelength+=Twaitn
        i+=1# add one for label
        ab = string.ascii_lowercase[i]
                
        #which ramdom pair  
        r1 = random.sample(range(0,len(samplednodes)-1),2)

        #pull random pair        
        coal1 = samplednodes.pop(r1[0])#samplednodes[r1[0]]
        coal2 = samplednodes.pop(r1[1])#samplednodes[r1[1]]
        tempparent = Node(ab,0,coal1,coal2)
        coal1.parent = tempparent
        coal2.parent = tempparent
        
        #append coalesed sample
        samplednodes.append(tempparent)



    #root node label
    i+=1
    ab = string.ascii_lowercase[i]
    
    #Last coales time
    N = len(samplednodes)
    Twaitn = n0 / nchoose2(N)
    Twaitn = round(Twaitn,4)
    for Ni in samplednodes:
        Ni.edgelength+=Twaitn
    coal1,coal2 = samplednodes

    #coales last pair
    root = Node(ab,Twait,coal1,coal2)
    coal1.parent = root
    coal2.parent = root


    #initialize tree with root node as head
    tree = Tree(root)
    print(tree)#traverses down and back up

    print(tree.inorder(tree.head))


