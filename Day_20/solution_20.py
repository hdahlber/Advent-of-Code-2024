import networkx as nx
from collections import deque

def read_in_file(filename):
    with open(filename, "r") as file:
        read = file.read().strip().split("\n")
    return read

def make_graph(file):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    Graph = nx.Graph()
    start = None
    end = None

    for i, l in enumerate(file):  # ROW
        for j, x in enumerate(l):  # COLUMN
            pos = (i, j)

            if x == "#":
                continue

            if x == "S":
                start = pos
            if x == "E":
                end = pos

            Graph.add_node(pos)

    for pos in list(Graph.nodes):
        row, col = pos
        for direction in directions:
            new_pos = (row + direction[0], col + direction[1])
            if 0 <= new_pos[0] < len(file) and 0 <= new_pos[1] < len(file[0]) and file[new_pos[0]][new_pos[1]] != "#":
                Graph.add_edge(pos, new_pos)

    return Graph, start, end

def part_1(indexed_weights):
    directions = [(-2, 0), (-1, -1), (0, -2), (1, -1), (2, 0), (1, 1), (0, 2), (-1, 1)]
    summer = 0
    for current_node in indexed_weights:
        current_weight = indexed_weights[current_node]
        #print("node row",current_node[0])
        #print("node column",current_node[1])
        for dx, dy in directions:
            possible_neighbor = (current_node[0] + dx, current_node[1] + dy)
            if possible_neighbor in indexed_weights:
                neighbor_weight = indexed_weights[possible_neighbor]
                if neighbor_weight > current_weight + 101:
                    summer += 1
                    #print(neighbor_weight)
    return summer

def part_2(indexed_weights):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_steps = 20
    summer = 0
    save_time = 100

    for current_node in indexed_weights:
        reachable_nodes = set()

        current_weight = indexed_weights[current_node]
        queue = deque([(current_node, 0)])  # (node, step)
        visited = {current_node}  

        while queue:
            node, steps = queue.popleft()

            if steps > max_steps:
                continue
           
            for dx, dy in directions:
                possible_neighbor = (node[0] + dx, node[1] + dy)

                if possible_neighbor not in visited:

                    visited.add(possible_neighbor)
                    queue.append((possible_neighbor, steps + 1))
                    if possible_neighbor in indexed_weights:
                        neighbor_weight = indexed_weights[possible_neighbor]
                        if steps + 1 <= max_steps and neighbor_weight >= (current_weight+save_time)+steps+1 :
                            #print("we here from",current_node,"right now at",possible_neighbor,"neigh weight",neighbor_weight,"steps",steps,"current weight",current_weight)
                            reachable_nodes.add(possible_neighbor)
        summer += len(reachable_nodes)
        #print("current node",current_node,"Reachable nodes within 20 steps:", reachable_nodes)
    return summer

def main():
    file = read_in_file("input.txt")
    graph, start, end, = make_graph(file)
    print(graph,"start", start,"end" ,end)
    base_short_path = nx.shortest_path(graph, start, end, weight="weight", method="dijkstra")
    indexed_weights = {node: index for index, node in enumerate(base_short_path)}
    result = part_1(indexed_weights)
    print(f"Part 1 results: {result}")
    result2 = part_2(indexed_weights)
    print(f"Part 2 results: {result2}")

if __name__ == "__main__":
    main()
