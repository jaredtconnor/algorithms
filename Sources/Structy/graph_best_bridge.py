import unittest
from collections import deque


def best_bridge(grid):

    main_island = None

    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):

            if grid[r][c] == "L":
                potential_island = search_for_main_island(grid, r, c, set())

                if len(potential_island) > 0:
                    main_island = potential_island
                    break

    visited = set(main_island)
    queue = deque([])

    for pos in main_island:
        r, c = pos
        queue.append((r, c, 0))

    while queue:

        r, c, bridge_dist = queue.popleft()

        if grid[r][c] == "L" and (r, c) not in main_island:
            return bridge_dist - 1

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for delta in deltas:
            delta_row, delta_col = delta

            neighbor_row = r + delta_row
            neighbor_col = c + delta_col
            neighbor_pos = (neighbor_row, neighbor_col)

            if (
                is_inbounds(grid, neighbor_row, neighbor_col)
                and neighbor_pos not in visited
            ):
                visited.add(neighbor_pos)
                queue.append((neighbor_row, neighbor_col, bridge_dist + 1))


def is_inbounds(grid, r, c):

    row_inbounds = 0 <= r < len(grid)
    column_inbounds = 0 <= c < len(grid[0])

    return row_inbounds and column_inbounds


# Returns and in representing the size of the island
def search_for_main_island(grid, r, c, visited):

    if not is_inbounds(grid, r, c) or grid[r][c] == "W":
        return visited

    # Base case 1 - space is visited
    pos = (r, c)

    if pos in visited:
        return visited

    visited.add(pos)

    # Perform traversal on all neighbors of grid

    search_for_main_island(grid, r - 1, c, visited)
    search_for_main_island(grid, r + 1, c, visited)
    search_for_main_island(grid, r, c - 1, visited)
    search_for_main_island(grid, r, c + 1, visited)

    # Return true if this is a new island explored
    return visited


class Test(unittest.TestCase):
    def test_case_1(self):
        grid = [
            ["W", "W", "W", "L", "L"],
            ["L", "L", "W", "W", "L"],
            ["L", "L", "L", "W", "L"],
            ["W", "L", "W", "W", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W"],
        ]

        res = best_bridge(grid)  # -> 1
        expected = 1
        assert res == expected

    def test_case_2(self):

        grid = [
            ["W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W"],
            ["L", "L", "W", "W", "L"],
            ["W", "L", "W", "W", "L"],
            ["W", "W", "W", "L", "L"],
            ["W", "W", "W", "W", "W"],
        ]
        res = best_bridge(grid)  # -> 2
        expected = 2
        assert res == expected

    def test_case_3(self):

        grid = [
            ["W", "W", "W", "W", "W"],
            ["W", "W", "W", "L", "W"],
            ["L", "W", "W", "W", "W"],
        ]
        res = best_bridge(grid)  # -> 3
        expected = 3
        assert res == expected

    def test_case_4(self):

        grid = [
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "L", "W", "W"],
            ["W", "W", "W", "W", "L", "L", "W", "W"],
            ["W", "W", "W", "W", "L", "L", "L", "W"],
            ["W", "W", "W", "W", "W", "L", "L", "L"],
            ["L", "W", "W", "W", "W", "L", "L", "L"],
            ["L", "L", "L", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
        ]
        res = best_bridge(grid)  # -> 3
        expected = 3
        assert res == expected

    def test_case_5(self):

        grid = [
            ["W", "L", "W", "W", "W", "W", "W", "W"],
            ["W", "L", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "W", "W"],
            ["W", "W", "W", "W", "W", "W", "L", "W"],
            ["W", "W", "W", "W", "W", "W", "L", "L"],
            ["W", "W", "W", "W", "W", "W", "W", "L"],
        ]
        res = best_bridge(grid)  # -> 8
        expected = 8
        assert res == expected


if __name__ == "__main__":
    unittest.main()
