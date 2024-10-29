"""
"
"   File:       file_handler.py
"   Author:     Xander Palermo <ajp2s@missouristate.edu>
"   Course:     CSC360 - Operating Systems
"   Instructor: Dr. Siming Liu
"   Project:    5 - Simulation of Page Replacement Strategies
"   Date:       30 October 2024
"
"""

from std_input import StdInput


def read_input (filename: str) -> StdInput:
    """
    Opens file "filename" and parses contents into a format that is more workable
    :param filename: the path of the file that contains input data
    :return: an object that contains all formatted input data
    """
    with open(filename, 'r') as input_file:

        # reference string
        ref_string = input_file.readline()
        ref_string = list(map(int, ref_string[:-1].split(' ')))

        # frames allocated
        frames = input_file.readline()
        frames = int(frames[:-1])

        # algorithms to be run
        mnemonics = input_file.readlines()
        for index, mnemonic in enumerate(mnemonics):
            if mnemonic[-1] == '\n':
                mnemonics[index] = mnemonic[:-1]

        return StdInput(ref_string, frames, mnemonics)

