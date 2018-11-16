import networkx
import matplotlib.pyplot as plt

graph = {
    'A' :'B B B C',
    'B' : 'A C',
    'C' : 'A B D E',
    'D' : 'C',
    'E' : 'C F',
    'F' : 'E'
}

graph_long = {
    '1': '2 7',
    '2': '3',
    '3': '4',
    '4': '5',
    '5': '6 10',
    '7': '8',
    '6': '5',
    '8': '9',
    '9': '10',
    '10': '5 11',
    '11': '12',
    '12': '11',
}


def breadth_first_search(graph):
    for k in graph:
        graph[k] = set(graph[k].split())
    # Graph = networkx.Graph(graph)
    # networkx.draw(Graph, with_labels=True)
    # plt.show()
    seen = set()
    need_visited = ['A']
    while need_visited:
        node = need_visited.pop(0)
        if node in seen:
            print('{} has been seen'.format(node))
            continue
        print('I am looking at : {}'.format(node))
        need_visited += graph[node]
        seen.add(node)


# 合并广度优先和深度优先解法
def search(graph, concat_func):
    seen = set()
    need_visited = ['1']

    while need_visited:
        node = need_visited.pop(0)
        if node in seen:
            print('{} has been seen'.format(node))
            continue
        print('I am looking at : {}'.format(node))
        seen.add(node)
        new_discoveried = graph[node]
        need_visited = concat_func(new_discoveried, need_visited)


def treat_new_discover_more_important(new_discoveried, need_visited):
    return new_discoveried + need_visited


def treat_already_discoveried_more_important(new_discoveried, need_visited):
    return need_visited + new_discoveried


if __name__ == '__main__':
    # breadth_first_search(graph)
    search(graph_long, treat_new_discover_more_important)


