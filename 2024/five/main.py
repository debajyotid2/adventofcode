"""
Advent of code day 5
"""
from collections import defaultdict

Graph = dict[int, tuple[int, int]]

def build_graph_and_paths(input_val: list[str]) -> tuple[Graph, list[int]]:
    graph = defaultdict(list)
    all_nodes = set()
    while True:
        line = input_val.pop(0)
        if line == "\n":
            break
        key, value = line[:-1].split("|")
        graph[int(key)].append(int(value))
        all_nodes.add(int(key))
        all_nodes.add(int(value))
    for node in all_nodes:
        if node not in graph:
            graph[node] = []
    return graph, [list(map(int, val.split(","))) for val in input_val]

def part_one(paths: list[list[int]], graph: Graph) -> int:
    middle_page_sum = 0
    for path in paths:
        left = []
        stop = False
        for el in path:
            in_hist = any([el_2 in graph[el] for el_2 in left])
            if in_hist:
                stop = True
                break
            left.append(el)
        if stop:
            continue
        middle_page_sum += path[len(path) // 2]
    return middle_page_sum

def main():
    with open("input", "r") as f:
        data = f.readlines()
    graph, paths = build_graph_and_paths(data)
    
    # Part one
    middle_page_sum = part_one(paths, graph)
    print(f"Part one answer: {middle_page_sum}")

if __name__=="__main__":
    main()
