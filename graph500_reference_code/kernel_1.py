def kernel_1(ijw):
    """
        Compute a sparse adjacency matrix representation
        of the graph with edges from ijw
    """
    import numpy as np

    #print(ijw)

    # Remove self-edges
    delete_index = []
    for j in range(ijw.shape[1]):
        if ijw[0][j] == ijw[1][j]:
            delete_index.append(j)
    ijw = np.delete(ijw, np.s_[delete_index], axis = 1)
    
    # Adjust away from zero labels.
    ijw[0:2,:] = ijw[0:2,:] + 1
    
    #print(ijw)

    # Order into a single triangle.
    mask = ijw[0] < ijw[1]
    for j in range(len(mask)):
        if mask[j]:
            ijw[0][j], ijw[1][j] = ijw[1][j], ijw[0][j]
        
    #print(ijw)
    
    # Find the maximum label from sizing.
    N = int(max(max(ijw[0]), max(ijw[1])))
    
    # Create the matrix, ensure it is square.
    G = np.zeros((N, N))
    for j in range(ijw.shape[1]):
        r = int(ijw[0][j] - 1)
        c = int(ijw[1][j] - 1)
        if G[r][c] != 0:
            G[r][c] = min(G[r][c], ijw[2][j])
        else:
            G[r][c] = ijw[2][j]
      
    G = G + G.T
    
    return G