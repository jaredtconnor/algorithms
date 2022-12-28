import unittest
from collections import Counter


def intersection_naive(list1, list2):

    result = []

    for i in range(len(list1)):
        for j in range(len(list2)):

            if list1[i] == list2[j]:
                result.append(list1[i])

    return result


def intersection(list1, list2):

    result = []

    list1_set = set(list1)

    for val in list2:
        if val in list1_set:
            result.append(val)

    return result


class Test(unittest.TestCase):

    a_1 = [4, 2, 1, 6]
    b_1 = [3, 6, 9, 2, 10]
    res_1 = [2, 6]

    a_2 = [2, 4, 6]
    b_2 = [4, 2]
    res_2 = [2, 4]

    a_3 = [4, 2, 1]
    b_3 = [1, 2, 4, 6]
    res_3 = [1, 2, 4]

    a_4 = [0, 1, 2]
    b_4 = [10, 11]
    res_4 = []

    def test_1(self):

        assert Counter(intersection_naive(self.a_1, self.b_1)) == Counter(self.res_1)
        assert Counter(intersection_naive(self.a_2, self.b_2)) == Counter(self.res_2)
        assert Counter(intersection_naive(self.a_3, self.b_3)) == Counter(self.res_3)
        assert Counter(intersection_naive(self.a_4, self.b_4)) == Counter(self.res_4)

    def test_2(self):

        assert Counter(intersection(self.a_1, self.b_1)) == Counter(self.res_1)
        assert Counter(intersection(self.a_2, self.b_2)) == Counter(self.res_2)
        assert Counter(intersection(self.a_3, self.b_3)) == Counter(self.res_3)
        assert Counter(intersection(self.a_4, self.b_4)) == Counter(self.res_4)


if __name__ == "__main__":
    unittest.main()
