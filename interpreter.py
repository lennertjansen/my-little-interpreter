"""Interpreter for a simple language."""

import sys

# read arguments
if len(sys.argv) != 2:
    print("Usage: python interpreter.py <program_filepath>")
    sys.exit(1)

program_filepath = sys.argv[1]

###########################
#     Tokenize Program
###########################

tokens = []

# read file lines and tokenize
with open(program_filepath, "r") as program_file:
    for line in program_file:
        stripped_line = line.strip()
        if stripped_line:
            # Simple tokenizer: splits on spaces, assumes no strings or
            # complex expressions
            tokens.extend(stripped_line.split())

###########################
#     Parse Tokens
###########################

# Placeholder for a simple parser - creates a list of (command, value) tuples
commands = []
i = 0
while i < len(tokens):
    if tokens[i] == "PRINT":  # For example, a command
        commands.append(("PRINT", tokens[i + 1]))
        i += 2
    else:
        print(f"Unknown command {tokens[i]}")
        sys.exit(1)

###########################
#     Execute Commands
###########################

# Execute parsed commands
for command, value in commands:
    if command == "PRINT":
        print(value)
