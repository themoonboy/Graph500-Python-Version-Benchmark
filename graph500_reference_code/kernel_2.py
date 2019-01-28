def kernel_2_reference(G, root):
    """
        Compute s sparse adjacency matrix representation
        of the graph with edges from ij.
        
        root here is zero-based label: 0 to 2^N-1
    """
    import numpy as np
    
    N = G.shape[0]

    # Not adjust from zero labels, just use it.
    parent = np.full((N, 1), -1)
    parent[root][0] = root
    
    vlist = np.full((N, 1), -1)
    vlist[0][0] = root;
    vlist = vlist.astype(int)
    lastk = 1
    for k in range(N):
        v = vlist[k][0];
        if v == -1: break
        nxt_candidate = np.where(G[:, v]!=0)[0]
        for neighbor in nxt_candidate: 
            if parent[neighbor][0] == -1:
                parent[neighbor][0] = v
                vlist[lastk][0] = neighbor
                lastk += 1
    
    # Adjust to zero labels
    #parent = parent - 1
    
    return parent