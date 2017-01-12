#given a directed graph, find if there is a route between two nodes

#breadth first search
def bfs(graph, node1, end):
    if node1 == end:
        return True
    visited = []
    queue = [node1]
    while queue:
        cur_node = queue.pop(0)
        if cur_node in visited:
            continue
        if cur_node == end:
            return True
        if graph.get(cur_node):
            queue.extend(graph.get(cur_node))
        visited.append(cur_node)

    return False

#depth first search
def dfs(graph, start, end, visited=[]):
    if start == end:
        return True
    found = False
    if graph.get(start):
        for node in graph.get(start):
            if node in visited:
                continue
            visited.append(node)
            found = dfs(graph, node, end, visited=visited)
            if found:
                break
    return found

if __name__ == "__main__":
    graph = {
        '1': ['2', '3', '4'],
        '2': ['1', '5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12'],
        '13': ['0']
        }

    print(bfs(graph, '1', '13'))
    print(dfs(graph, '1', '13'))

