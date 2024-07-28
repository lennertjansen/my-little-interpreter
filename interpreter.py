"""Interpreter for the language."""

import sys

# read arguments
program_filepath = sys.argv[1]

###########################
#     Tokenize Program
###########################

# read file lines
program_lines = []
with open(program_filepath, "r") as program_file:
    program_lines = [line.strip() for line in program_file.readlines()]
