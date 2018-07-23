import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class GraphVertex:
    def __init__(self, label):
        self.label = label
        self.edges = []


def clone_graph(graph):
    if not graph:
        return None

    my_queue = collections.deque([graph])
    vertex_map = {graph: GraphVertex(graph.label)}
    while my_queue:
        vertex = my_queue.popleft()
        for edge in vertex.edges:
            if edge not in vertex_map:
                vertex_map[edge] = GraphVertex(edge.label)
                my_queue.append(edge)
            vertex_map[vertex].edges.append(vertex_map[edge])
    return vertex_map[graph]


def copy_labels(edges):
    return [edge.label for edge in edges]


def check_graph(node, graph):
    if node is None:
        raise TestFailure('Graph was not copied')

    vertex_set = set()
    my_queue = collections.deque()
    my_queue.append(node)
    vertex_set.add(node)
    while my_queue:
        vertex = my_queue.popleft()
        if vertex.label >= len(graph):
            raise TestFailure('Invalid vertex label')
        label1 = copy_labels(vertex.edges)
        label2 = copy_labels(graph[vertex.label].edges)
        if sorted(label1) != sorted(label2):
            raise TestFailure('Edges mismatch')
        for edge in vertex.edges:
            if edge not in vertex_set:
                vertex_set.add(edge)
                my_queue.append(edge)


def clone_graph_test(k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex(i) for i in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    result = clone_graph(graph[0])
    check_graph(result, graph)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("graph_clone.py", 'graph_clone.tsv',
                                       clone_graph_test))
