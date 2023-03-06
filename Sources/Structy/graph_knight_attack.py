import unittest
from collections import deque


def knight_attack(n, kr, kc, pr, pc):

    queue = deque([(kr, kc, 0)])
    visited = set()
    visited.add((kr, kc))

    while queue:

        r, c, distance = queue.popleft()

        if (r, c) == (pr, pc):
            return distance

        neighbor_posistions = get_knight_positions(n, r, c)
        for neighbor_position in neighbor_posistions:

            if neighbor_position not in visited:
                neighbor_row, neighbor_col = neighbor_position
                queue.append((neighbor_row, neighbor_col, distance + 1))
                visited.add(neighbor_position)

    return None


def get_knight_positions(n, kr, kc):

    positions = [
        (kr + 2, kc + 1),
        (kr - 2, kc + 1),
        (kr + 2, kc - 1),
        (kr - 2, kc - 1),
        (kr + 1, kc + 2),
        (kr - 1, kc + 2),
        (kr + 1, kc - 2),
        (kr - 1, kc - 2),
    ]

    valid_positions = []

    for pos in positions:
        r, c = pos

        if 0 <= r < n and 0 <= c < n:
            valid_positions.append(pos)

    return valid_positions


class Test(unittest.TestCase):
    def test_case_1(self):

        res = knight_attack(8, 1, 1, 2, 2)  # -> 2
        expected = 2
        assert res == expected

    def test_case_2(self):

        res = knight_attack(8, 1, 1, 2, 3)  # -> 1
        expected = 1
        assert res == expected

    def test_case_3(self):

        res = knight_attack(8, 0, 3, 4, 2)  # -> 3
        expected = 3
        assert res == expected

    def test_case_4(self):

        res = knight_attack(8, 0, 3, 5, 2)  # -> 4
        expected = 4
        assert res == expected

    def test_case_5(self):

        res = knight_attack(24, 4, 7, 19, 20)  # -> 10
        expected = 10
        assert res == expected

    def test_case_6(self):

        res = knight_attack(100, 21, 10, 0, 0)  # -> 11
        expected = 11
        assert res == expected

    def test_case_7(self):

        res = knight_attack(3, 0, 0, 1, 2)  # -> 1
        expected = 1
        assert res == expected

    def test_case_8(self):

        res = knight_attack(3, 0, 0, 1, 1)  # -> None
        expected = None
        assert res == expected


if __name__ == "__main__":
    unittest.main()
