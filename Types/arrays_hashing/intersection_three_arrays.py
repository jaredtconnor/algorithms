import unittest


def intersection_three_list(list1, list2, list3):

    result = []
    i, j, k = 0, 0, 0

    while i < len(list1) and j < len(list2) and k < len(list3):

        if list1[i] == list2[j] == list3[k]:
            result.append(list1[i])
            i += 1
            j += 1
            k += 1

        elif list1[i] < list2[j]:
            i += 1

        elif list2[j] < list3[k]:
            j += 1

        else:
            k += 1

    return result


class Test(unittest.TestCase):

    ar1 = [1, 5, 10, 20, 40, 80]
    ar2 = [6, 7, 20, 80, 100]
    ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

    test_cases = [(ar1, ar2, ar3, [20, 80])]

    test_functions = [intersection_three_list]

    def test_1(self):

        for test_function in self.test_functions:
            for l1, l2, l3, expected in self.test_cases:
                assert test_function(l1, l2, l3) == expected


if __name__ == "__main__":
    unittest.main()
