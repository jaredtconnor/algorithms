import unittest


def befitting_brackets(string):
    stack = []
    brackets = {
        "(": ")",
        "[": "]",
        "{": "}",
    }

    for c in string:
        if c in brackets:
            stack.append(brackets[c])
        else:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                return False

    return len(stack) == 0


class Test(unittest.TestCase):
    def test_1(self):
        res = befitting_brackets("(){}[](())")  # -> True
        exp = True
        assert res == exp

    def test_2(self):
        res = befitting_brackets("({[]})")  # -> True
        exp = True
        assert res == exp

    def test_3(self):
        res = befitting_brackets("[][}")  # -> False
        exp = False
        assert res == exp

    def test_4(self):
        res = befitting_brackets("{[]}({}")  # -> False
        exp = False
        assert res == exp

    def test_5(self):
        res = befitting_brackets("[]{}(}[]")  # -> False
        exp = False
        assert res == exp

    def test_6(self):
        res = befitting_brackets("[]{}()[]")  # -> True
        exp = True
        assert res == exp

    def test_7(self):
        res = befitting_brackets("[]{}()[]")  # -> True
        exp = True
        assert res == exp

    def test_8(self):
        res = befitting_brackets("]{}")  # -> False
        exp = False
        assert res == exp

    def test_9(self):
        res = befitting_brackets("")  # -> True
        exp = True
        assert res == exp

    def test_10(self):
        res = befitting_brackets("{[(}])")  # -> False
        exp = False
        assert res == exp


if __name__ == "__main__":
    unittest.main()
