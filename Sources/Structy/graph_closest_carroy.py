import unittest


def closest_carrot(grid, starting_row, starting_col): 







    return 0


class Test(unittest.TestCase):
    def test_case_1(self):

        grid = [
            ['O', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'O', 'O'],
            ['O', 'X', 'X', 'O', 'O'],
            ['O', 'X', 'C', 'O', 'O'],
            ['O', 'X', 'X', 'O', 'O'],
            ['C', 'O', 'O', 'O', 'O'],
        ]

        res = closest_carrot(grid, 1, 2)  # -> 4
        expected = 4
        assert res == expected

    def test_case_2(self):

        grid = [
            ['O', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'O', 'O', 'O'],
            ['O', 'X', 'X', 'O', 'O'],
            ['O', 'X', 'C', 'O', 'O'],
            ['O', 'X', 'X', 'O', 'O'],
            ['C', 'O', 'O', 'O', 'O'],
        ]

        res = closest_carrot(grid, 0, 0)  # -> 5
        expected = 5
        assert res == expected

    def test_case_3(self):

        grid = [
            ['O', 'O', 'X', 'X', 'X'],
            ['O', 'X', 'X', 'X', 'C'],
            ['O', 'X', 'O', 'X', 'X'],
            ['O', 'O', 'O', 'O', 'O'],
            ['O', 'X', 'X', 'X', 'X'],
            ['O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'C', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O'],
        ]

        res = closest_carrot(grid, 3, 4)  # -> 9
        expected = 9
        assert res == expected

    def test_case_4(self):
        grid = [
            ['O', 'O', 'X', 'O', 'O'],
            ['O', 'X', 'X', 'X', 'O'],
            ['O', 'X', 'C', 'C', 'O'],
        ]

        res = closest_carrot(grid, 1, 4)  # -> 2
        expected = 2
        assert res == expected

    def test_case_5(self):
        grid = [
            ['O', 'O', 'X', 'O', 'O'],
            ['O', 'X', 'X', 'X', 'O'],
            ['O', 'X', 'C', 'C', 'O'],
        ]

        res = closest_carrot(grid, 2, 0)  # -> -1
        expected = -1
        assert res == expected

    def test_case_6(self):
        grid = [
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'X'],
            ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'X', 'C'],
        ]

        res = closest_carrot(grid, 0, 0)  # -> -1
        expected = -1
        assert res == expected

    def test_case_7(self):

        grid = [
            ['O', 'O', 'X', 'C', 'O'],
            ['O', 'X', 'X', 'X', 'O'],
            ['C', 'X', 'O', 'O', 'O'],
        ]

        res = closest_carrot(grid, 2, 2)  # -> 5
        expected = 5
        assert res == expected


if __name__ == "__main__":
    unittest.main()
