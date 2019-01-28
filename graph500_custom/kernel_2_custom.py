def kernel_2_custom(G, root):
    """
        Compute s sparse adjacency matrix representation
        of the graph with edges from ij.
        
        root here is zero-based label: 0 to 2^N-1
    """
    import numpy as np
    from multiprocessing.dummy import Pool as ThreadPool
    from functools import partial

    N = G.shape[0]
    
    frontier = [root]
    nxt = []
    parent = np.full((N, 1), -1)
    parent[root] = root
    
    
    while len(frontier)>0:
        partial_work = partial(top_down, G, parent, nxt) 
        pool = ThreadPool()
        pool.map(partial_work, frontier)
        pool.close()
        pool.join()
        frontier = nxt
        nxt = []
        
    return parent

def top_down(G, parent, nxt, key):
    import numpy as np
    
    #for key in frontier: # This part could be parallelized
    cur_nxt = np.where(G[:,key]!=0)[0]
    cur_nxt = np.delete(cur_nxt, np.where(parent[cur_nxt]!=-1)[0], axis = 0)
    parent[cur_nxt] = key
    nxt += cur_nxt.tolist()