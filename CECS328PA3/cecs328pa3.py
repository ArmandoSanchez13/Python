def max_gold(weight, capacity):
    x = len(weight)
    y = [[0] * (capacity + 1) for _ in range(x + 1)]

    for i in range(1, x + 1):
        for z in range(1, capacity + 1):
            if weight[i - 1] <= z:
                y[i][z] = max(weight[i - 1] + y[i - 1][z - weight[i - 1]], y[i - 1][z])
            else:
                y[i][z] = y[i - 1][z]

    return y[x][capacity]
