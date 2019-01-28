def kronecker_generator(SCALE, edgefactor):
    """
        Generate an edgelist according to the Graph500 parameters.
        In this sample, the edge list is returned in an array with three
        rows, where StartVertex is first row, EndVertex is the second row,
        and Weight is the third row. The vertex labels start at zero.
    """
    import numpy as np
    
    # Set number of vertices.
    N = 2**SCALE

    # Set number of edges.
    M = edgefactor * N

    # Set initiator probabilities.
    [A, B, C] = [0.57, 0.19, 0.19]

    # Create index arrays.
    ijw = np.ones((3, M))
    # Loop over each order of bit
    ab = A + B
    c_norm = C / (1 - (A + B))
    a_norm = A / (A + B)

    for ib in range(1, SCALE + 1):
        # Compare with probabilities and set bits of indices.
        ii_bit = np.random.uniform(0, 1, size = (1, M)) > ab
        jj_bit = np.random.uniform(0, 1, size = (1, M)) > (c_norm * ii_bit + a_norm * (~ii_bit))
        ijw[0:2] = ijw[0:2] + 2**(ib - 1) * np.append(ii_bit, jj_bit, axis = 0)

    # Generate weights.
    ijw[2] = np.random.uniform(0, 1, size = (1, M))

    # Permute vertex labels and edge list.
    ijw[0] = np.random.permutation(ijw[0])
    ijw[1] = np.random.permutation(ijw[1])

    # Adjust to zero-based labels.
    ijw[0:2] = ijw[0:2] - 1

    return ijw
    