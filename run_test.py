
env = globals().copy()

import sys
import unittest
from unittest.mock import patch
from io import StringIO


def runfile(filename):
    filename += '.py'
    with open(filename, encoding='utf8') as file:
        source = file.read()
    if source[0] == '\ufeff':
        source = source[1:]
    code = compile(source, filename, 'exec')
    exec(code, env)


def patchio(*args):
    if args:
        return lambda meth: \
            patch('builtins.input', side_effect=list(args))(
                patch('sys.stdout', new_callable=StringIO)(lambda self, stdout, _: meth(self, stdout)))
    else:
        return lambda meth: \
            patch('sys.stdout', new_callable=StringIO)(meth)

########################################################################################################################


class MostCommon(unittest.TestCase):
    @patchio("KaluKaMa KaDo")
    def test_single(self, stdout):
        runfile('most_frequent')
        results = [letter for letter in (stdout.getvalue().upper().split('\n')) if letter]
        self.assertEqual(results, ['A'])

    @patchio("KaluKaMa KaKo")
    def test_one_of_many(self, stdout):
        runfile('most_frequent')
        results = [letter for letter in (stdout.getvalue().upper().split('\n')) if letter]
        self.assertGreaterEqual(len(results), 1)
        self.assertIn(results[0], ('A', 'K'))

    @patchio("KaluKaMa KaKo")
    def test_all(self, stdout):
        runfile('most_frequent')
        results = [letter for letter in (stdout.getvalue().upper().split('\n')) if letter]
        if len(results) == 1:
            self.skipTest("not required")
        self.assertEqual(set(results), {'A', 'K'})


class Remove3(unittest.TestCase):
    @patchio("Oiwah1eesah2nieDaeshijeeZ4oingoy")
    def test_removal(self, stdout):
        runfile('remove3')
        self.assertEqual(stdout.getvalue().strip()  , "OiaheeahniDashjeZ4inoy")


class SwapNeighbors(unittest.TestCase):

    @patchio("1 2 3 4 5 6 7 8 9 0")
    def test_even(self, stdout):
        runfile('swap_neighbors')
        self.assertEqual(stdout.getvalue().strip(), "2 1 4 3 6 5 8 7 0 9")

    @patchio("1 2 3 4 5 6 7 8 9")
    def test_odd(self, stdout):
        runfile('swap_neighbors')
        self.assertEqual(stdout.getvalue().strip(), "2 1 4 3 6 5 8 7 9")


if __name__ == '__main__':
    test = unittest.main(exit=False)
    sys.exit(not test.result.wasSuccessful())
