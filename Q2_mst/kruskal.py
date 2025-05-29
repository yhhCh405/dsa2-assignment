class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            self.parent[ry] = rx


def kruskal(edges, vertices):
    """
    Compute Minimum Spanning Tree using Kruskal's algorithm.
    edges: list of (u, v, weight)
    vertices: list of all vertex labels
    Returns: list of edges in the MST
    """
    ds = DisjointSet(vertices)
    mst = []
    # sort edges by weight ascending
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
    return mst