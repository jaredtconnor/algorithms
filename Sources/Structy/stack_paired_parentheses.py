import unittest


def paired_parentheses(string):
    counter = 0

    for s in string:
        if s == "(":
            counter += 1

        elif s == ")":
            if counter == 0:
                return False
            counter -= 1

    if counter == 0:
        return True
    else:
        return False


class Test(unittest.TestCase):
    def test_1(self):
        res = paired_parentheses("(david)((abby))")  # -> True
        exp = True
        assert res == exp

    def test_2(self):
        res = paired_parentheses("()rose(jeff")  # -> False
        exp = False
        assert res == exp

    def test_3(self):
        res = paired_parentheses(")(")  # -> False
        exp = False
        assert res == exp

    def test_4(self):
        res = paired_parentheses("()")  # -> True
        exp = True
        assert res == exp

    def test_5(self):
        res = paired_parentheses("(((potato())))")  # -> True
        exp = True
        assert res == exp

    def test_6(self):
        res = paired_parentheses("(())(water)()")  # -> True
        exp = True
        assert res == exp

    def test_7(self):
        res = paired_parentheses("(())(water()()")  # -> False
        exp = False
        assert res == exp

    def test_8(self):
        res = paired_parentheses("")  # -> True
        exp = True
        assert res == exp

    def test_9(self):
        res = paired_parentheses("))()")  # False
        exp = False

        assert res == exp


if __name__ == "__main__":
    unittest.main()
