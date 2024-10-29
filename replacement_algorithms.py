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

    @staticmethod
    def FIFO(ref_string : list[int], frame : int) -> None:
        print("FIFO called")
        return

    @staticmethod
    def LRU(ref_string : list[int], frame : int) -> None:
        print("LRU called")
        return

    @staticmethod
    def OPT(ref_string : list[int], frame : int) -> None:
        print("OPT called")
        return

    @staticmethod
    def RAND(ref_string : list[int], frame : int) -> None:
        print("RAND called")
        return


    def calculate(self) -> int:
        ref_string =  self.__std_input.get_ref_string()
        frames =  self.__std_input.get_frames()
        mnemonics =  self.__std_input.get_mnemonic()
        for mnemonic in mnemonics:
            if mnemonic == "FIFO":
                self.FIFO(ref_string, frames)
            elif mnemonic == "LRU":
                self.LRU(ref_string, frames)
            elif mnemonic == "OPT":
                self.OPT(ref_string, frames)
            elif mnemonic == "RAND":
                self.RAND(ref_string, frames)
            else:
                print(f"ERROR: {mnemonic} is not a valid mnemonic, check input file.")
                return 1
        return 0







#end class
