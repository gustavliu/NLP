import json
import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['font.serif'] = ['SimHei']

def get_data():
    f = open('subway.txt', 'r')
    data = json.loads(f.read())
    f.close()
    return data


def process_dict(stations):
    station_connection = defaultdict(list)
    for line, stas in stations.items():
        for i in range(0, len(stas)):
            if i == 0:
                station_connection[stas[i]].append(stas[i+1])
            elif i == len(stas)-1:
                station_connection[stas[i]].append(stas[i-1])
            else:
                station_connection[stas[i]].append(stas[i-1])
                station_connection[stas[i]].append(stas[i+1])
    return station_connection


# 得到路线连接关系，站点：路线数据
def line_path(stations):
    line = [k for k in stations.keys()]
    stas = [v for v in stations.values()]
    line_connection = defaultdict(set)
    sta_line = defaultdict(set)
    for i in range(len(line)):
        for sta in stas[i]:
            sta_line[sta].add(line[i])
            for j in range(len(line)):
                if j == i: continue
                if sta in stas[j]:
                    line_connection[line[i]].add(line[j])
    return line_connection, sta_line


# 搜索站点路径
def search_path(start, destination, sc):
    pathes = [[start]]
    seen = set()
    chosen_pathes = []
    while pathes:
        path = pathes.pop(0)
        frontier = path[-1]
        if frontier in seen: continue
        # get new lines
        for city in sc[frontier]:
            if city in path: continue  # remove loop
            new_path = path + [city]
            pathes.append(new_path)
            if city == destination: return new_path
        seen.add(frontier)
    return chosen_pathes


#搜索最少换乘路线
def search_line(start, destination, line_connection, sta_line):
    start_line = sta_line[start]
    destination_line = sta_line[destination]
    route = search_path(start_line[0], destination_line[0], line_connection)
    print(route)


if __name__ == '__main__':
    data = get_data()
    station_connection = process_dict(data)
    # line_connection, sta_line = line_path(data)
    # search_line('11号线', '4号线', line_connection, sta_line)
    paths = search_path('灵芝站', '沙尾站', station_connection)
    print('->'.join(paths))
    # G = nx.Graph(station_connection)
    # nx.draw(G, with_labels=True, node_size=2, font_size=8)
    # plt.show()


