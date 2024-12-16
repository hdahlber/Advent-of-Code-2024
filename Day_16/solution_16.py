import networkx as nx

def read_in_file(filename):
    with open(filename, "r") as file:
        read = file.read().strip().split("\n")
    return read

def make_graph(file):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    Graph = nx.DiGraph()
    start = None
    end = None

    for i, l in enumerate(file): # ROW
        for j, x in enumerate(l): # COLUMN
            if x == "#":
                continue  
            pos = (i, j)  
            if x == "S":
                start = (pos, (0, 1))  
            if x == "E":
                end = pos  
            for direction in directions: # add node
                Graph.add_node((pos, direction))

    for (pos, direction) in list(Graph.nodes):
        row, col = pos
        direction_row, direction_column = direction

        # current direction weight = 1
        new_pos = (row + direction_row, col + direction_column)
        if 0 <= new_pos[0] < len(file) and 0 <= new_pos[1] < len(file[0]) and file[new_pos[0]][new_pos[1]] != "#":
            Graph.add_edge((pos, direction), (new_pos, direction), weight=1)

        # changing direction weight = 1000
        for rotation in directions:
            if rotation != direction:
                Graph.add_edge((pos, direction), (pos, rotation), weight=1000)

    # stop
    for direction in directions:
        Graph.add_edge((end, direction), "end", weight=0)

    return Graph, start, end


def part_2(graph,start):
    # https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.all_shortest_paths.html
    paths =nx.all_shortest_paths(graph, start, "end", weight="weight", method="dijkstra")
    nodes = set()
    for path in paths:
        for edge in path:
            nodes.add(edge[0])
    print(nodes)
    return len(nodes)-1 # end node remove
def main():
    file = read_in_file("input.txt")
    graph, start, end = make_graph(file)
    result = nx.shortest_path_length(graph, start, "end", weight="weight",method="dijkstra")
    print(f"Part 1 results: {result}")
    result2 = part_2(graph,start)
    print(f"Part 2 results: {result2}")



if __name__ == "__main__":
    main()