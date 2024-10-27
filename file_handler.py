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

import os

from replacement_algorithms import StdInput


def read_input (filename: str) -> StdInput:
    with open(filename, 'r') as input_file:

        # reference string
        ref_string = input_file.readline()
        ref_string = list(map(int, ref_string[:-1].split(' ')))
        print(ref_string)

        # frames allocated
        frames = input_file.readline()
        frames = int(frames[:-1])
        print(frames)

        mnemonics = input_file.readlines()
        for index, mnemonic in enumerate(mnemonics):
            if mnemonic[-1] == '\n':
                mnemonics[index] = mnemonic[:-1]
        print(mnemonics)
        return StdInput(ref_string, frames, mnemonics)

