def fifteen_puzzle(board: list[list[int]]):
    def get_empty_cell(board: list[list[int]]) -> tuple[int, int]:
        for i in range(4):
            for j in range(4):
                if board[i][j] == 0:
                    return i, j
        raise ValueError("No empty cell found in the board")

    def is_valid_move(x: int, y: int) -> bool:
        return 0 <= x < 4 and 0 <= y < 4

    def get_moves(board: list[list[int]], x: int, y: int):
        moves = []
        directions = [(0, 1, 'R'), (0, -1, 'L'), (1, 0, 'D'), (-1, 0, 'U')]
        for dx, dy, move_char in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y):
                new_board = [row[:] for row in board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                moves.append((new_board, move_char))
        return moves

    def solve(board: list[list[int]], max_depth=10):
        goal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
        queue = [(board, '', 0)]
        visited = set()
        while queue:
            board, path, depth = queue.pop(0)
            if board == goal:
                return list(path)
            if depth >= max_depth:
                return None
            x, y = get_empty_cell(board)
            for new_board, move in get_moves(board, x, y):
                board_str = str(new_board)
                if board_str not in visited:
                    visited.add(board_str)
                    queue.append((new_board, path + move, depth + 1))
        return None
    return solve(board)

puzzle = [[2, 3, 4, 0], [1, 5, 7, 8], [9, 6, 10, 12], [13, 14, 11, 15]]
solution = fifteen_puzzle(puzzle)
if solution is None:
    print("This puzzle is not solvable.")
else:
    print('Moves:',''.join(solution))

#puzzle = [[2, 3, 4, 0], [1, 5, 7, 8], [9, 6, 10, 12], [13, 14, 11, 15]]
#puzzle = [[13, 1, 2, 4], [5, 0, 3, 7], [9, 6, 10, 12], [15, 8, 11, 14]]