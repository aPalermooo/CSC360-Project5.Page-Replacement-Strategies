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
from replacement_algorithms import Algorithm

def debug_print():
    print("\n"*5)

def main (file_path : str) -> int:
    """
    Applies algorithms to calculate number of page faults a specific instance of memory would encounter
    Included algorithms: FIFO, LRU, OPT, and RAND
    :param file_path:       path of input file
    :return:                0 for successful execution, 1 for input formatting error
    """
    #open designated file and format contents
    in_file = "p52.txt"
    print(f"simpager.py < {in_file}")                                   #echo file path
    program_input = file_handler.read_input(in_file)
    print(f"Page Reference String: {program_input.get_ref_string()}")   #echo ref_string

    # apply algorithms to ref string to calc page faults
    compute_page_faults = Algorithm(program_input)
    compute_page_faults.calculate()
    return 0

if __name__ == "__main__":
    main("p52.txt")