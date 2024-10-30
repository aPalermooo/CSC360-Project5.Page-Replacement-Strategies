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

import sys

# Default file path is for the input file given in the assignment in the same directory as simpager.py
DEFAULT_FILE_PATH = "p52.txt"

def main (file_path : str = DEFAULT_FILE_PATH) -> int:
    """
    Applies algorithms to calculate number of page faults a specific instance of memory would encounter
    Included algorithms: FIFO, LRU, OPT, and RAND
    :param file_path:       path of input file
    :return:                0 for successful execution, 1 for input formatting error
    """
    if len(sys.argv) > 1:
        file_path = sys.argv[1]

    # open designated file and format contents
    print(f"simpager.py < {file_path}")                                 #echo file path
    program_input = file_handler.read_input(file_path)
    print(f"Page Reference String: {program_input.get_ref_string()}")   #echo ref_string

    # apply algorithms to ref string to calc page faults
    compute_page_faults = Algorithm(program_input)
    successful = compute_page_faults.calculate()
    if not successful:
        return 1
    return 0

if __name__ == "__main__":
    main("p52.txt")

