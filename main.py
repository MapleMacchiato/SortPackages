import unittest
from test_sort import TestPackageSort


def main():
    tests = unittest.TestSuite()
    tests.addTest(unittest.makeSuite(TestPackageSort))
    test_runner = unittest.TextTestRunner()
    results = test_runner.run(tests)
    print(results)


main()
