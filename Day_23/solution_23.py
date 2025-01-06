import networkx as nx


def read_in_file(filename):
    with open(filename, "r") as file:
        read = file.read().strip().split("\n")
    return read


def create_graph(edges):
    G = nx.Graph()
    for edge in edges:
        node1, node2 = edge.split("-")
        G.add_edge(node1, node2)
    for node in G.nodes:
        G.nodes[node]["value"] = node.startswith("t")

    return G


def part_1(graph):
    cliques = [clique for clique in nx.enumerate_all_cliques(graph) if len(clique) == 3]
    #print(len(cliques))
    filtered_cliques = [tuple(sorted(clique)) for clique in cliques if
                        any(graph.nodes[node]["value"] for node in clique)]
    #print(len(filtered_cliques))
    return len(filtered_cliques)


def part_2(graph):
    cliques = list(nx.find_cliques(graph))
    biggest_clique = sorted(max(cliques, key=len))
    result = ",".join(biggest_clique)
    return result


def main():
    file_edges = read_in_file("input.txt")
    graph = create_graph(file_edges)
    result = part_1(graph)
    print(f"Part 1 results: {result}")
    result2 = part_2(graph)
    print(f"Part 2 results: {result2}")


if __name__ == "__main__":
    main()
