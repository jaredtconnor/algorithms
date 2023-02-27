import unittest


def semesters_required(num_courses, prereqs):

    graph = build_graph(num_courses, prereqs)

    semesters = {}

    for node in graph:

        if len(graph[node]) == 0:
            semesters[node] = 1

    for node in graph:
        semesters_needed(graph, node, semesters)

    return max(semesters.values())


def semesters_needed(graph, current, semesters):

    if current in semesters:
        return semesters[current]

    max_path = 0

    for neighbor in graph[current]:
        path = semesters_needed(graph, neighbor, semesters)

        if path > max_path:
            max_path = path

    semesters[current] = 1 + max_path
    return semesters[current]


def build_graph(num_courses, prereqs):

    graph = {}

    for course in range(0, num_courses):

        graph[course] = []

    for prereq in prereqs:
        a, b = prereq

        graph[a].append(b)

    return graph


class Test(unittest.TestCase):
    def test_case_1(self):

        num_courses = 6
        prereqs = [
            (1, 2),
            (2, 4),
            (3, 5),
            (0, 5),
        ]
        res = semesters_required(num_courses, prereqs)  # -> 3
        expected = 3
        assert res == expected

    def test_case_2(self):
        num_courses = 7
        prereqs = [
            (4, 3),
            (3, 2),
            (2, 1),
            (1, 0),
            (5, 2),
            (5, 6),
        ]
        res = semesters_required(num_courses, prereqs)  # -> 5
        expected = 5
        assert res == expected

    def test_case_3(self):

        num_courses = 5
        prereqs = [
            (1, 0),
            (3, 4),
            (1, 2),
            (3, 2),
        ]
        res = semesters_required(num_courses, prereqs)  # -> 2
        expected = 2
        assert res == expected

    def test_case_4(self):
        num_courses = 12
        prereqs = []
        res = semesters_required(num_courses, prereqs)  # -> 1
        expected = 1
        assert res == expected

    def test_case_5(self):
        num_courses = 3
        prereqs = [
            (0, 2),
            (0, 1),
            (1, 2),
        ]
        res = semesters_required(num_courses, prereqs)  # -> 3
        expected = 3
        assert res == expected

    def test_case_6(self):
        num_courses = 6
        prereqs = [
            (3, 4),
            (3, 0),
            (3, 1),
            (3, 2),
            (3, 5),
        ]
        res = semesters_required(num_courses, prereqs)  # -> 2
        expected = 2
        assert res == expected


if __name__ == "__main__":
    unittest.main()
