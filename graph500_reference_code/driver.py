from multiprocessing.dummy import Pool as ThreadPool
from functools import partial
import numpy as np
import time

from kronecker_generator import *
from kernel_1 import *
from kernel_2 import *
from validate import *
from output import *

"""
    Driver, not include kernel_3
"""

SCALE = 16
edgefactor = 16
NBFS = 64

ijw = kronecker_generator(SCALE, edgefactor)

start1 = time.time()

G = kernel_1(ijw);
end1 = time.time()
kernel_1_time = end1 - start1

N = G.shape[0]

#print(G)

# Find all node labels that are not isolated in graph.
valid_node = np.array(np.where(G.any(axis=0)))
search_key = np.random.permutation(valid_node[0])
if len(search_key) > NBFS:
    search_key = search_key[0: NBFS + 1]
else:
    NBFS = len(search_key)
# Search keys are already zero-based

kernel_2_time = np.full((NBFS, 1), np.inf)
kernel_2_nedge = np.zeros((NBFS, 1))

"""
k = 0 : NBFS-1 in python, because it is the index of list,
search_key itself as a list includes zero-based node labels.
"""
for k in range(NBFS):
    t_start = time.time()
    parent = kernel_2_reference(G, search_key[k])
    t_end = time.time()
    kernel_2_time[k] = t_end - t_start
    
    # Validation 
    """
    if not validate(parent, G):
        print("BFS from search key %d failed to be validated" % search_key[k])
    """
    for node in parent:
        if node>=0:
            kernel_2_nedge[k] += len(np.where(G[:,node]>0)[0])
            
    # kernel_3 ignored
    
output(SCALE, NBFS, NBFS, kernel_1_time, kernel_2_time, kernel_2_nedge)
