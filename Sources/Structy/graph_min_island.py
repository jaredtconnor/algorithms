import unittest


def minimum_island(grid):

    visited = set()
    min_island_size = float("inf")

    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):

            island_size = search_island(grid, r, c, visited)

            if island_size > 0 and island_size < min_island_size:
                min_island_size = island_size

    return min_island_size


# Returns and in representing the size of the island
def search_island(grid, r, c, visited):

    row_inbounds = 0 <= r < len(grid)
    column_inbounds = 0 <= c < len(grid[0])

    # Base case 1 - in bounds
    if row_inbounds is False or column_inbounds is False:
        return 0  # Return False if a new island is not found

    # Base case 2 - space is water
    if grid[r][c] == "W":
        return 0

    # Base case 3 - space is visited
    pos = (r, c)

    if pos in visited:
        return 0

    visited.add(pos)

    # Perform traversal on all neighbors of grid

    size = 1
    size += search_island(grid, r - 1, c, visited)
    size += search_island(grid, r + 1, c, visited)
    size += search_island(grid, r, c - 1, visited)
    size += search_island(grid, r, c + 1, visited)

    # Return true if this is a new island explored
    return size


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

        res = minimum_island(grid)  # -> 2
        expected = 2
        assert res == expected

    def test_case_2(self):
        grid = [
            ["L", "W", "W", "L", "W"],
            ["L", "W", "W", "L", "L"],
            ["W", "L", "W", "L", "W"],
            ["W", "W", "W", "W", "W"],
            ["W", "W", "L", "L", "L"],
        ]

        res = minimum_island(grid)  # -> 1
        expected = 1
        assert res == expected

    def test_case_3(self):
        grid = [
            ["L", "L", "L"],
            ["L", "L", "L"],
            ["L", "L", "L"],
        ]

        res = minimum_island(grid)  # -> 9
        expected = 9
        assert res == expected

    def test_case_4(self):
        grid = [["W", "W"], ["L", "L"], ["W", "W"], ["W", "L"]]

        res = minimum_island(grid)  # -> 1
        expected = 1
        assert res == expected


if __name__ == "__main__":
    unittest.main()
