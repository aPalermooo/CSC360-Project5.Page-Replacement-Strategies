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
    file_handler.read_input(in_file)
    return 0

if __name__ == "__main__":
    main()