# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 2022

@author: scannon
"""

# Import necessary packages
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
from sympy import *

# Section 1: Networkx
"""
Main python class for working with graphs: documentation at https://networkx.org/
"""

n = int(input("Desired length: ")) # user designates how long the lattice is


grid_3xn = nx.grid_graph([3,n]) # this makes a 3 x n grid graph 
for i in range(n-1):
        grid_3xn.add_edge((i,0), (i+1,1))
        for i in range(n-1): 
                grid_3xn.add_edge((i,1), (i+1, 2))
plt.figure() # start a figure
nx.draw(grid_3xn, node_size = 1000, node_color = 'pink', with_labels = True, 
        pos = {x:x for x in grid_3xn.nodes()}) # this plots the 3 x n grid graph 
plt.show()

lapl_3xn = nx.laplacian_matrix(grid_3xn)
lapl_3xn_array = np.matrix(lapl_3xn.toarray())
L_3xn = Matrix(np.array(lapl_3xn_array.data).reshape(3*n,3*n))
num_spanning_trees_3xn = L_3xn.adjugate()[1,1] # this computes determinant of Laplacian, i.e., the number of spanning trees of the graph
print("Number of Spanning Trees: " + str(num_spanning_trees_3xn))

alpha = (num_spanning_trees_3xn*5)**(1/n)
print("Lower Bound Constant: " + str(alpha))

