'''
Reference: Leetcode Study Guide

There are 2 Approaches to implement the Union Find algorithm:
1. The Quick Find Approach:
    Find():O(1)
    Union():O(N)

2. The Quick Union Approach:
    Find():O(N)
    Union():O(1)

'''

#
# Approach 1: The Quick Find Approach
# 
# In this approach we have an array with indexes representing the nodes 
# and values representing the root/head of the group in which the node is.
#

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
    
    # find the root node
    def find(self, x):
        return self.root[x]
    
    # Link 2 nodes
    def union(self, x, y):
        # get the root for x and y
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            for i in range(len(self.root)):
                if self.root[i] == rootY:
                    self.root[i] = rootX
    
    # Say if 2 nodes are connected. 2 nodes are connected if they have the same root
    def connected(self, x, y):
        return self.find(x) == self.find(y)



#
# Approach 2: The Quick Union Approach
#
# Here we have an array with indexes representing the nodes
# and values representing the parent of the node
#

class UnionFind2:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
    
    # find the root node
    def find(self, x):
        while self.parent[x] != x:
            x = self.parent[x]
        
        return x
    
    # Link 2 node
    def union(self, x, y):
        # get the root of x and y
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = x
    
    # say if 2 nodes are connected.
    def connected(self, x, y):
        return self.find(x) == self.find(y)



#Testing

graph = [[0,1], [0,2],[1,3],[4,8],[5,6],[5,7],[9,9]]
N = 10        

uF1 = UnionFind2(N)

for edge in graph:
    uF1.union(edge[0], edge[1])

print(uF1.parent)
print(uF1.connected(7,8))

# link 7 and 8
uF1.union(7, 8)
print(uF1.parent)
print(uF1.connected(7,8))
        
