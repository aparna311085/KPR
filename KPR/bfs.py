from collections import deque
def bfs(graph,start_node):
    visited=set()
    queue=deque()
    queue.append(start_node)
    visited.add(start_node)
    print("BFS traversal order")
    while queue:
        current_node=queue.popleft()
        print(current_node,end=' ')
        for neighbour in graph.get(current_node,[]):
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
graph_input={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F','G'],
    'D':[],
    'E':[],
    'F':[],
    'G':[]
}
bfs(graph_input,'A')
            