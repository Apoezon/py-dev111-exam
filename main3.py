import networkx as nx
from collections import deque


def components(g: nx.Graph):
    """
    Проверяет связность графа. Реализована в виде поиска в ширину.
    Добавляет компоненты связности графа в список и считает длину этого списка.
    :param g: граф networkx
    :return: количество компонент связности
    """
    all_paths = []
    visited = {node: False for node in g.nodes}
    # print(visited, "<-- visited")
    for node in visited:
        # print(f'checking node {node}')
        if not visited[node]:
            d = deque()
            path = []
            d.append(node)
            visited[node] = True
            while d:
                current_node = d.popleft()
                path.append(current_node)
                for neighbour_ in g.neighbors(current_node):
                    if not visited[neighbour_]:
                        d.append(neighbour_)
                        visited[neighbour_] = True
            # print(visited)
            all_paths.append(path)
    print(all_paths)
    return len(all_paths)

graph_list = [
    ('A', 'B'),
    ('B', 'C'),
    ('C', 'D'),
    ('E', 'E'), # возможно не правильная запись, так как нужно было просто добавить graph.add_node("E")
    ('F', 'G')
]

graph = nx.Graph()
graph.add_edges_from(graph_list)
print(components(graph))