import unittest

from lib import Options


class TestCommandLineParameters(unittest.TestCase):

    def setUp(self):
        self.options = Options()

    def test_defaults_options_are_set(self):
        opts = self.options.parse()
        self.assertEquals(opts.cuboid_file, '../cuboid.dat')

    def test_options_example_is_set(self):
        opts = self.options.parse(['-c', 'foobar'])
        self.assertEquals(opts.cuboid_file, 'foobar')

        opts = self.options.parse(['--cuboid', 'not-a-foobar'])
        self.assertEquals(opts.cuboid_file, 'not-a-foobar')


if __name__ == '__main__':
    unittest.main()
