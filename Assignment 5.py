from collections import deque, OrderedDict
from heapq import heappush, heappop

def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    def ssp_helper(visited, frontier):
        if len(frontier) == 0:
            return visited
        else:
            distance,node,path = heappop(frontier)
            if node in visited:
                return ssp_helper(visited, frontier)
            else:
                visited[node] = (distance, path)
                for neighbor, weight in graph[node]:
                    heappush(frontier, (distance + weight, neighbor, path + 1 ))
            return ssp_helper(visited,frontier)
        
    frontier = []
    heappush(frontier, (0, source,0))
    visited = dict()  
    return ssp_helper(visited, frontier)
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
    
    def bfs_path_helper(visited, frontier):
        if len(frontier) == 0:
            return visited
        else:
            visiting = frontier[0]
            frontier.pop(0)
            neighborNodes = graph[visiting]
            for n in neighborNodes:
                if n not in visited.keys():
                    frontier.append(n)
                    visited[n] = visiting
            return bfs_path_helper(visited, frontier)
        
    visited = {}
    frontier = [source]
    
    return bfs_path_helper(visited,frontier)
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    print("parents ==", parents)
    print( parents['a'] == 's')
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    print( parents['d'] == 'c')
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    i = 0
    path = ""
    parentz = OrderedDict(reversed(list(parents.items())))
    parentzB = list(parentz.items())
    element = [tupl[i] for tupl in parentz]
    element2 = [tupl[i+1] for tupl in parentzB]
    
    def get_path_helper(parents, destination, path, i):
        if i >= len(element):
            path = path[::-1]
            return path
        if element[i] == destination:
            #print('source not marked yet")
            path += element2[i]
            destination = element2[i]
        return get_path_helper(parentzB, destination,path, i + 1)

    return get_path_helper(parents,destination,path,i)
    
    
def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'


