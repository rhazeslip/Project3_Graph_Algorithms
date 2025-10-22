#Undirected Graph Problem 1
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Create the undirected graph from the first dataset
G1 = nx.Graph()
nodes_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
G1.add_nodes_from(nodes_1)

# Add edges (you'll need to specify the actual connections)
# For demonstration, I'll create a sample connected graph
edges_1 = [('A','B'), ('A','F'), ('A','E'), ('B','C'), ('B','F'), ('C','D'), ('C','G'), ('D','G'), ('E','F'), 
           ('E','I'), ('F','I'), ('G','J'), ('I','J'), ('I','M'), ('M','N'),
           ('H','K'), ('H','L'), ('K','O'), ('K','L'), ('L','P')]  
G1.add_edges_from(edges_1)

def dfs_components(graph, start):
    """Find connected components using DFS"""
    visited = set()
    component = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            component.append(node)
            stack.extend([n for n in graph.neighbors(node) if n not in visited])
    
    return component

def bfs_components(graph, start):
    """Find connected components using BFS"""
    visited = set()
    component = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            component.append(node)
            queue.extend([n for n in graph.neighbors(node) if n not in visited])
    
    return component

def find_path_bfs(graph, start, end):
    """Find path between two nodes using BFS"""
    if start == end:
        return [start]
    
    visited = set()
    queue = deque([(start, [start])])
    
    while queue:
        current, path = queue.popleft()
        for neighbor in graph.neighbors(current):
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None

def find_path_dfs(graph, start, end):
    """Find path between two nodes using DFS"""
    if start == end:
        return [start]
    
    visited = set()
    stack = [(start, [start])]
    
    while stack:
        current, path = stack.pop()
        for neighbor in graph.neighbors(current):
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))
    
    return None

# Test the algorithms
print("Part 1: Undirected Graph Analysis")
print("=" * 50)

# a) Find connected components
start_node = 'A'
dfs_comp = dfs_components(G1, start_node)
bfs_comp = bfs_components(G1, start_node)
print(f"DFS found component: {dfs_comp}")
print(f"BFS found component: {bfs_comp}")
print(f"Both find all connected components: {set(dfs_comp) == set(bfs_comp)}")

# b) Check path existence
node_u, node_v = 'A', 'N'
bfs_path = find_path_bfs(G1, node_u, node_v)
dfs_path = find_path_dfs(G1, node_u, node_v)
print(f"\nPath from {node_u} to {node_v}:")
print(f"BFS path: {bfs_path}")
print(f"DFS path: {dfs_path}")
print(f"Both can find path: {bfs_path is not None and dfs_path is not None}")

# c) Compare paths
print(f"\nBFS and DFS find same path: {bfs_path == dfs_path}")