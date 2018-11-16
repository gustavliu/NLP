import networkx
import matplotlib.pyplot as plt

BJ = 'Beijing'
SZ = 'Shenzhen'
GZ = 'Guangzhou'
WH = 'Wuhan'
HLG = 'Heilongjiang'
NY = 'New York City'
CM = 'Chiangmai'
SG = 'Singapore'


air_route = {
    BJ : {SZ, GZ, WH, HLG, NY},
    GZ : {WH, BJ, CM, SG},
    SZ : {BJ, SG},
    WH : {BJ, GZ},
    HLG : {BJ},
    CM : {GZ},
    NY : {BJ}
}


def search_destination(graph, start, destination):
    pathes = [[start]]
    seen = set()
    chosen_pathes = []
    while pathes:
        path = pathes.pop(0)
        frontier = path[-1]
        if frontier in seen: continue
        # get new lines

        for city in graph[frontier]:
            new_path = path + [city]
            pathes.append(new_path)
            if city == destination: return new_path

        seen.add(frontier)
    return chosen_pathes

def draw_route(cities): return ' ✈️ -> '.join(cities)


if __name__ == '__main__':
    air_route = networkx.Graph(air_route)
    networkx.draw(air_route, with_labels=True)
    plt.show()
    route = draw_route(search_destination(air_route, SZ, CM))
    print(route)
