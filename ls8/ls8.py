#!/usr/bin/env python3

"""Main."""

import sys
from cpu import *

# if len(sys.argv) != 2:
#     print('USAGE: ls8.py filename')
#     sys.exit(1)

# program = sys.argv[1]

cpu = CPU()

cpu.load(program)
cpu.run()


# print(sys.argv)