def cargo(crates, T, W, D):
    initial = [[[0] * (D + 1) for _ in range(W + 1)] for __ in range(T + 1)]

    def count(crate):
        return crate.count('t'), crate.count('w'), crate.count('d')

    for crate in crates:
        t_counter, w_counter, d_counter = count(crate)
        for t in range(T, t_counter - 1, -1):
            for w in range(W, w_counter - 1, -1):
                for d in range(D, d_counter - 1, -1):
                    initial[t][w][d] = max(initial[t][w][d], initial[t - t_counter][w - w_counter][d - d_counter] + 1)
                    
    return initial[T][W][D]