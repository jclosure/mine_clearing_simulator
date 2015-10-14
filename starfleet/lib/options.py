from argparse import ArgumentParser


class Options:

    def __init__(self):
        self._init_parser()

    def _init_parser(self):
        usage = 'bin/project'
        self.parser = ArgumentParser(usage=usage)
        self.parser.add_argument('-f',
                                 '--field',
                                 default='cuboid.dat',
                                 dest='cuboid_file',
                                 help='This is the cuboid definition file')

        self.parser.add_argument('-s',
                                 '--script',
                                 default='student_minesweeping_script.steps',
                                 dest='steps_file',
                                 help='This is the file containing the instruction steps to fall through the cuboid')
                                 
        
    def parse(self, args=None):
        return self.parser.parse_args(args)
