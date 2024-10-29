"""
"
"   File:       replacement_algorithms.py
"   Author:     Xander Palermo <ajp2s@missouristate.edu>
"   Course:     CSC360 - Operating Systems
"   Instructor: Dr. Siming Liu
"   Project:    5 - Simulation of Page Replacement Strategies
"   Date:       30 October 2024
"
"""
from std_input import StdInput

class Algorithm:
    def __init__(self, std_input: StdInput) -> None:
        self.__std_input = std_input


    def __FIFO(self):
        print("FIFO called")
        return 1

    def __LRU(self):
        print("LRU called")
        return 1

    def __OPT(self):
        print("OPT called")
        return 1

    def __RAND(self):
        print("RAND called")
        return 1

    def calculate(self) -> None:
        ref_string =  self.__std_input.get_ref_string()
        frames =  self.__std_input.get_frames()
        mnemonics =  self.__std_input.get_mnemonic()
        for mnemonic in mnemonics:
            if mnemonic == "FIFO":
                self.__FIFO()
            elif mnemonic == "LRU":
                self.__LRU()
            elif mnemonic == "OPT":
                self.__OPT()
            elif mnemonic == "RAND":
                self.__RAND()
            else:
                print(f"ERROR: {mnemonic} is not a valid mnemonic, check input file.")
        return







#end class
