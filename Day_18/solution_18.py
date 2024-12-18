import networkx as nx


def read_in_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    coordinates = [tuple(map(int, line.strip().split(','))) for line in lines]
    return coordinates


def make_graph(w, h):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    Graph = nx.Graph()
    for x in range(w):
        for y in range(h):
            Graph.add_node((x, y))

    for x in range(w):
        for y in range(h):
            for dx, dy in directions:
                neighbor = (x + dx, y + dy)
                if 0 <= neighbor[0] < w and 0 <= neighbor[1] < h:
                    Graph.add_edge((x, y), neighbor)

    return Graph


def part_1(file):
    width = 71
    height = 71
    start = (0, 0)
    end = (width - 1, height - 1)
    graph = make_graph(width, height)
    for x in enumerate(file):
        #print(x)
        if x[0] == 1024:
            result = nx.shortest_path_length(graph, start, end, weight="weight", method="dijkstra")
            return result
        graph.remove_node(x[1])


def part_2(file):
    width = 71
    height = 71
    start = (0, 0)
    end = (width - 1, height - 1)
    graph = make_graph(width, height)
    last_one = 0
    for x in enumerate(file):
        try:
            result = nx.shortest_path_length(graph, start, end, weight="weight", method="dijkstra")
            print(result)
            last_one = x[1]
            graph.remove_node(x[1])
        except:
            return last_one


def main():
    file = read_in_file("input.txt")
    result = part_1(file)
    print(f"Part 1 results: {result}")
    result2 = part_2(file)
    print(f"Part 2 results: {result2}")


if __name__ == "__main__":
    main()
