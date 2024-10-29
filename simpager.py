"""
"
"   File:       simpager.py
"   Author:     Xander Palermo <ajp2s@missouristate.edu>
"   Course:     CSC360 - Operating Systems
"   Instructor: Dr. Siming Liu
"   Project:    5 - Simulation of Page Replacement Strategies
"   Date:       30 October 2024
"
"""
import file_handler
import replacement_algorithms
from replacement_algorithms import Algorithm, calculate


def main () -> int:
    in_file = "p52.txt"
    print(f"simpager.py < {in_file}")
    program_input = file_handler.read_input(in_file)
    print(f"Page Reference String: {program_input.get_ref_string()}")
    compute_page_faults = Algorithm
    print( f"\n\n\n\ndebug:"
           f"{type(program_input)}\n"
           f"{program_input.get_ref_string()}\n"
           f"{program_input.get_frames()}\n"
           f"{program_input.get_mnemonic()}\n")
    replacement_algorithms.calculate(program_input)
    return 0

if __name__ == "__main__":
    main()