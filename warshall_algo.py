

def Warshall_trans_clsure(relation):
    """warshall algorithm for finding transitive closure"""
    size = len(relation)
    for i in range(size):
        for j in range(size):
            for k in range(size):
                relation[i][j] = relation[i][j] or (
                    relation[i][k] and relation[k][j])


def utility():
    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if temp[i][j]:
                print(f'({i+1},{j+1})')
