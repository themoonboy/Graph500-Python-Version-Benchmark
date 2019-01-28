def validate(parent, G):
    for i in len(parent):
        if G[i][parent[i]] == 0:
            return False
    return True