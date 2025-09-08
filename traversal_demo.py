from collections import deque

def dfs(graph:dict,start_node:str) -> None:
    stack = [start_node]
    visited = {start_node}  #to avoid cycles
    while stack:
        item = stack.pop()
        print(item, end=" ")
        if graph.get(item):
            for neighbour in reversed(graph[item]):
                if neighbour not in visited:
                    visited.add(neighbour)
                    stack.append(neighbour)
    print("")

def bfs(graph:dict,start_node:str) -> None:
    queue = deque([start_node])
    visited = {start_node}  # to avoid cycles
    while queue:
        item = queue.popleft()
        print(item, end=" ")
        if graph.get(item):
            for neighbour in graph[item]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
    print("")

def main() -> None:
    tree = {
        "A" : ["B","C"],
        "B" : ["D","E"],
        "C" : ["F"]
    }

    graph = {
        "A" : ["B","C"],
        "B" : ["A","D","E"],
        "C" : ["A","F"],
        "D" : ["B"],
        "E" : ["B","F"],
        "F" : ["C","E"]
    }

    print("-----------Tree BFS-------------")
    bfs(tree,"A")
    print("-----------Tree DFS-------------")
    dfs(tree,"A")

    print("-----------Graph BFS-------------")
    bfs(graph,"A")
    print("-----------Graph DFS-------------")
    dfs(graph,"A")


if __name__ == "__main__":
    main()
