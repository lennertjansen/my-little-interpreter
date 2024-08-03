"""Main module for the interpreter."""

import sys
from interpreter import (
    run_script,
)  # Assuming the core interpreter functionality is defined in interpreter.py


def main() -> None:
    """Run main script for the interpreter."""
    # Check if the program file path was provided
    if len(sys.argv) != 2:
        print("Usage: python main.py <program_filepath>")
        sys.exit(1)

    # Read the program filepath from command line arguments
    program_filepath = sys.argv[1]

    # Run the script
    try:
        run_script(program_filepath)
    except Exception as e:
        print(f"Error running the script: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
