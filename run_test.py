env = globals().copy()

import sys
import unittest
from unittest.mock import patch
from io import StringIO


def runfile(name, *inputs):
    filename = name + '.py'
    with open(filename, encoding='utf8') as file:
        source = file.read()
    if source[0] == '\ufeff':
        source = source[1:]
    code = compile(source, filename, 'exec')

    if inputs:
        with patch('builtins.input', side_effect=list(inputs)):
            with patch('sys.stdout', new_callable=StringIO) as stdout:
                exec(code, env)
                return stdout.getvalue()
    else:
        with patch('sys.stdout', new_callable=StringIO) as stdout:
            exec(code, env)
            return stdout.getvalue()


########################################################################################################################


class MostFrequent(unittest.TestCase):

    def test_single(self):
        results = [letter for letter in (runfile('most_frequent', "KaluKaMa KaDo").upper().split('\n')) if letter]
        self.assertEqual(['A'], results)

    def test_one_of_many(self):
        results = [letter for letter in (runfile('most_frequent', "KaluKaMa KaKo").upper().split('\n')) if letter]
        self.assertGreaterEqual(len(results), 1)
        self.assertIn(results[0], ('A', 'K'))

    def test_all(self):
        results = [letter for letter in (runfile('most_frequent', "KaluKaMa KaKo").upper().split('\n')) if letter]
        if len(results) == 1:
            self.skipTest("not required")
        self.assertEqual({'A', 'K'}, set(results))


class Remove3(unittest.TestCase):

    def test_removal(self):
        self.assertEqual("OiaheeahniDashjeZ4inoy", runfile('remove3', "Oiwah1eesah2nieDaeshijeeZ4oingoy").strip())


class SwapNeighbors(unittest.TestCase):

    def test_even(self):
        self.assertEqual("2 1 4 3 6 5 8 7 0 9", runfile('swap_neighbors', "1 2 3 4 5 6 7 8 9 0").strip())

    def test_odd(self):
        self.assertEqual("2 1 4 3 6 5 8 7 9", runfile('swap_neighbors', "1 2 3 4 5 6 7 8 9").strip())


if __name__ == '__main__':
    test = unittest.main(exit=False)
    sys.exit(not test.result.wasSuccessful())
