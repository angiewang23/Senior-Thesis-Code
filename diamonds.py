
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from numpy import random
from sympy import *


s = 21 # if s > 21, the number gets too large for python to handle 
vertices_mat = np.zeros((1, s-1))
lim_mat = np.zeros((1, s-1))


for a in range(2, s+1): 
        grid_sxs = nx.grid_graph([a,a]) # this makes a x a grid graph 
        for c in range (a-1): 
                for i in range(a-1):
                        grid_sxs.add_edge((c,i), (c+1,i+1))
        lapl = nx.laplacian_matrix(grid_sxs).toarray()
        lapl_rowcolremoved = np.delete(np.delete(lapl, 0, 0), 0, 1)
        num_spanning_trees_sxs = round(np.linalg.det(lapl_rowcolremoved))
        print("Number of Spanning Trees for a " + str(a) + " x " + str(a) + " diamond: " + str(num_spanning_trees_sxs))
        limit = np.log(float(num_spanning_trees_sxs))/(a**2)
        print("Limit: "  + str(limit))
        vertices_mat[0, a-2] = int(a*a)
        lim_mat[0, a-2] = limit


# Flatten the arrays
vertices = vertices_mat.ravel()
limits = lim_mat.ravel()

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))
ax.scatter(vertices, limits)
plt.xticks(np.arange(min(vertices), max(vertices)+1, 50))
plt.yticks(np.arange(0, 1.615, 0.1))

# Set the x and y axis labels
ax.set_xlabel("Number of Vertices (n)")
ax.set_ylabel("ln(Num. of Spanning Trees)/(n^2)")

# Show the plot
plt.show()