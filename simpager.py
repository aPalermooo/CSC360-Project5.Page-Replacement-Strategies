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


def main () -> int:
    in_file = "p52.txt"
    print(f"simpager.py < {in_file}")
    program_input = file_handler.read_input(in_file)
    print(f"Page Reference String: {program_input.get_ref_string()}")
    compute_page_faults = Algorithm(program_input)
    compute_page_faults.calculate()
    return 0

if __name__ == "__main__":
    main()