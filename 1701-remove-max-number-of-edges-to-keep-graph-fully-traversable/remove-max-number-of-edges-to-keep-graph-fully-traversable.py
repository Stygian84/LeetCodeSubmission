class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n + 1)
        uf_alice = UnionFind(n + 1)
        uf_bob = UnionFind(n + 1)

        edges.sort(reverse=True, key=lambda x: x[0])

        removed_edges = 0
        alice_edges = 0
        bob_edges = 0

        for edge in edges:
            edge_type, u, v = edge
            if edge_type == 3:
                if uf.union(u, v):
                    uf_alice.union(u, v)
                    uf_bob.union(u, v)
                    alice_edges += 1
                    bob_edges += 1
                else:
                    removed_edges += 1
            elif edge_type == 1:
                if uf_alice.union(u, v):
                    alice_edges += 1
                else:
                    removed_edges += 1
            elif edge_type == 2:
                if uf_bob.union(u, v):
                    bob_edges += 1
                else:
                    removed_edges += 1

        if alice_edges == n - 1 and bob_edges == n - 1:
            return removed_edges
        return -1
        
class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
            return True
        return False