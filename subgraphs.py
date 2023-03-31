
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
from sympy import *

n = int(input("Desired length of subgraph: ")) # user provides an integer greater than or equal to 2

### Make a 3xn trianglar lattice with 2 rightmost edges removed 
grid_3xn = nx.grid_graph([3, n]) # this makes a 3xn graph 
for i in range(n-1):
        grid_3xn.add_edge((i,0), (i+1,1))
        for i in range(n-1): 
                grid_3xn.add_edge((i,1), (i+1, 2))
grid_3xn.remove_edge((n-1,0), (n-1,1))
grid_3xn.remove_edge((n-1, 1), (n-1,2))
plt.figure() # start a figure
nx.draw(grid_3xn, node_size = 1000, node_color = 'pink', with_labels = True, 
        pos = {x:x for x in grid_3xn.nodes()})
plt.show() #display your figure

lapl_3xn = nx.laplacian_matrix(grid_3xn)
lapl_3xn_array = np.matrix(lapl_3xn.toarray())
L_3xn = Matrix(np.array(lapl_3xn_array.data).reshape(3*n,3*n))
num_spanning_trees_3xn = L_3xn.adjugate()[1,1] # this computes determinant of Laplacian, i.e., the number of spanning trees of the graph
print("Number of Spanning Trees: " + str(num_spanning_trees_3xn))


