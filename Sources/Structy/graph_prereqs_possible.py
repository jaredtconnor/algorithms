import unittest


def prereqs_possible(num_courses, prereqs):

    graph = build_graph(num_courses, prereqs)

    visiting = set()
    visited = set()

    for node in graph:

        if cycle_detect(graph, node, visiting, visited) is True:
            return False

    return True


def cycle_detect(graph, node, visiting, visited):

    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited) is True:
            return True

    visiting.remove(node)
    visited.add(node)

    return False


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

        numCourses = 6
        prereqs = [
            (0, 1),
            (2, 3),
            (0, 2),
            (1, 3),
            (4, 5),
        ]
        res = prereqs_possible(numCourses, prereqs)  # -> True
        expected = True
        assert res == expected

    def test_case_2(self):

        numCourses = 6
        prereqs = [
            (0, 1),
            (2, 3),
            (0, 2),
            (1, 3),
            (4, 5),
            (3, 0),
        ]
        res = prereqs_possible(numCourses, prereqs)  # -> False
        expected = False
        assert res == expected

    def test_case_3(self):
        numCourses = 5
        prereqs = [
            (2, 4),
            (1, 0),
            (0, 2),
            (0, 4),
        ]
        res = prereqs_possible(numCourses, prereqs)  # -> True
        expected = True
        assert res == expected

    def test_case_4(self):

        numCourses = 6
        prereqs = [
            (2, 4),
            (1, 0),
            (0, 2),
            (0, 4),
            (5, 3),
            (3, 5),
        ]
        res = prereqs_possible(numCourses, prereqs)  # -> False
        expected = False
        assert res == expected

    def test_case_5(self):

        numCourses = 8
        prereqs = [
            (1, 0),
            (0, 6),
            (2, 0),
            (0, 5),
            (3, 7),
            (4, 3),
        ]
        res = prereqs_possible(numCourses, prereqs)  # -> True
        expected = True
        assert res == expected

    def test_case_6(self):

        numCourses = 8
        prereqs = [
            (1, 0),
            (0, 6),
            (2, 0),
            (0, 5),
            (3, 7),
            (7, 4),
            (4, 3),
        ]
        res = prereqs_possible(numCourses, prereqs)  # -> False
        expected = False
        assert res == expected

    def test_case_7(self):

        numCourses = 42
        prereqs = [(6, 36)]
        res = prereqs_possible(numCourses, prereqs)  # -> True
        expected = True
        assert res == expected


if __name__ == "__main__":
    unittest.main()
