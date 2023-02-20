import unittest


def island_count(grid):

    visited = set()
    count = 0

    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):

            if search_island(grid, r, c, visited) is True:
                count += 1

    return count


def search_island(grid, r, c, visited):

    row_inbounds = 0 <= r < len(grid)
    column_inbounds = 0 <= c < len(grid[0])

    # Base case 1 - in bounds
    if row_inbounds is False or column_inbounds is False:
        return False  # Retrun False if a new island is not found

    # Base case 2 - space is water
    if grid[r][c] == "W":
        return False

    # Base case 3 - space is visited
    pos = (r, c)

    if pos in visited:
        return False

    visited.add(pos)

    # Perform traversal on all neighbors of grid

    search_island(grid, r - 1, c, visited)
    search_island(grid, r + 1, c, visited)
    search_island(grid, r, c - 1, visited)
    search_island(grid, r, c + 1, visited)

    # Return true if this is a new island explored
    return True


class Test(unittest.TestCase):
    def test_case_1(self):

        grid = [
            ["W", "L", "W", "W", "W"],
            ["W", "L", "W", "W", "W"],
            ["W", "W", "W", "L", "W"],
            ["W", "W", "L", "L", "W"],
            ["L", "W", "W", "L", "L"],
            ["L", "L", "W", "W", "W"],
        ]

        res = island_count(grid)  # -> 3
        expected = 3
        assert res == expected

    def test_case_2(self):

        grid = [
            ["L", "W", "W", "L", "W"],
            ["L", "W", "W", "L", "L"],
            ["W", "L", "W", "L", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "W", "L", "L", "L"],
        ]

        res = island_count(grid)  # -> 4
        expected = 4
        assert res == expected

    def test_case_3(self):

        grid = [
            ["L", "L", "L"],
            ["L", "L", "L"],
            ["L", "L", "L"],
        ]

        res = island_count(grid)  # -> 1
        expected = 1
        assert res == expected

    def test_case_4(self):

        grid = [
            ["W", "W"],
            ["W", "W"],
            ["W", "W"],
        ]

        res = island_count(grid)  # -> 0
        expected = 0
        assert res == expected


if __name__ == "__main__":
    unittest.main()
