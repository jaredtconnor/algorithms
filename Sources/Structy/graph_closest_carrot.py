import unittest
from collections import deque


def closest_carrot(grid, starting_row, starting_col): 

    # Create our queue that stores (row, col, distance)
    visited = set([(starting_row, starting_col)])
    queue = deque([(starting_row, starting_col, 0)])

    while queue: 

        # Pop the current from our queue
        row, col, distance = queue.popleft()

        # Check if the queue is the carrot
        if grid[row][col] == "C":
            return distance

        movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for move in movements:
            move_row, move_col = move

            neighbor_row = row + move_row
            neighbor_col = col + move_col

            row_inbounds = 0 <= neighbor_row < len(grid)
            col_inbounds = 0 <= neighbor_col < len(grid[0])

            pos = (neighbor_row, neighbor_col)

            if row_inbounds and col_inbounds and grid[neighbor_row][neighbor_col] != "X" and pos not in visited:
                queue.append((neighbor_row, neighbor_col, distance + 1))  
                visited.add(pos)

    return -1


class Test(unittest.TestCase):
    def test_case_1(self):

        grid = [
            ["O", "O", "O", "O", "O"],
            ["O", "X", "O", "O", "O"],
            ["O", "X", "X", "O", "O"],
            ["O", "X", "C", "O", "O"],
            ["O", "X", "X", "O", "O"],
            ["C", "O", "O", "O", "O"],
        ]

        res = closest_carrot(grid, 1, 2)  # -> 4
        expected = 4
        assert res == expected

    def test_case_2(self):

        grid = [
            ["O", "O", "O", "O", "O"],
            ["O", "X", "O", "O", "O"],
            ["O", "X", "X", "O", "O"],
            ["O", "X", "C", "O", "O"],
            ["O", "X", "X", "O", "O"],
            ["C", "O", "O", "O", "O"],
        ]

        res = closest_carrot(grid, 0, 0)  # -> 5
        expected = 5
        assert res == expected

    def test_case_3(self):

        grid = [
            ["O", "O", "X", "X", "X"],
            ["O", "X", "X", "X", "C"],
            ["O", "X", "O", "X", "X"],
            ["O", "O", "O", "O", "O"],
            ["O", "X", "X", "X", "X"],
            ["O", "O", "O", "O", "O"],
            ["O", "O", "C", "O", "O"],
            ["O", "O", "O", "O", "O"],
        ]

        res = closest_carrot(grid, 3, 4)  # -> 9
        expected = 9
        assert res == expected

    def test_case_4(self):
        grid = [
            ["O", "O", "X", "O", "O"],
            ["O", "X", "X", "X", "O"],
            ["O", "X", "C", "C", "O"],
        ]

        res = closest_carrot(grid, 1, 4)  # -> 2
        expected = 2
        assert res == expected

    def test_case_5(self):
        grid = [
            ["O", "O", "X", "O", "O"],
            ["O", "X", "X", "X", "O"],
            ["O", "X", "C", "C", "O"],
        ]

        res = closest_carrot(grid, 2, 0)  # -> -1
        expected = -1
        assert res == expected

    def test_case_6(self):
        grid = [
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "X"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "C"],
        ]

        res = closest_carrot(grid, 0, 0)  # -> -1
        expected = -1
        assert res == expected

    def test_case_7(self):

        grid = [
            ["O", "O", "X", "C", "O"],
            ["O", "X", "X", "X", "O"],
            ["C", "X", "O", "O", "O"],
        ]

        res = closest_carrot(grid, 2, 2)  # -> 5
        expected = 5
        assert res == expected


if __name__ == "__main__":
    unittest.main()
