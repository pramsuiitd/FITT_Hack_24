class Control_Centre():
    def __init__(self, N) -> None:
        self.route_table = dict()
        self.adj_matrix = [[0 for _ in range(N)] for _ in range(N)]
        self.flow = 0
        self.time_int = 10
        