INF = 9999999
N = 5
cost = 0
G = [
    [0, 19, 5, 0, 0],
    [19, 0, 5, 9, 2],
    [5, 5, 0, 1, 6],
    [0, 9, 1, 0, 1],
    [0, 2, 6, 1, 0]
]

selected = [0] * N  # Track whether a node is included in the MST
selected[0] = 1  # Start with the first node
num_edges = 0  # Track the number of edges in the MST

print("Edge : Weight")

# Iterate N-1 times to select N-1 edges for the MST
while num_edges < N - 1:
    min_cost = INF
    x, y = 0, 0  # Variables to store the indices of the selected edge

    # Find the minimum cost edge that connects a selected node to an unselected node
    for i in range(N):
        if selected[i]:
            for j in range(N):
                if not selected[j] and G[i][j]:
                    if G[i][j] < min_cost:
                        min_cost = G[i][j]
                        x, y = i, j

    # Include the selected edge in the MST
    print(f"{x} - {y} : {G[x][y]}")
    cost += G[x][y]
    selected[y] = 1
    num_edges += 1

print(f"Minimum Cost: {cost}")
