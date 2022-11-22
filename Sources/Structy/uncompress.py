import unittest


def uncompress(s):

    res = []
    i, j = 0, 0

    while j < len(s):

        if s[j].isalpha():

            num = int(s[i:j])
            res.append(num * s[j])

            i = j + 1

        j += 1

    return "".join(res)


class Test(unittest.TestCase):

    test_cases = {
        ("2c3a1t", "ccaaat"),
        ("4s2b", "ssssbb"),
        ("2p1o5p", "ppoppppp"),
        (
            "127y",
            "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
        ),
    }

    def test_1(self):

        for s, expected in self.test_cases:
            assert uncompress(s) == expected


if __name__ == "__main__":
    unittest.main()
