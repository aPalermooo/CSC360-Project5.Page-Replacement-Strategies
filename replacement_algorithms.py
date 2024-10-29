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


class StdInput:
    def __init__(self, ref_string: list[int], frames: int, mnemonics: list[str]) -> None:
        self.__ref_string = ref_string
        self.__frames = frames
        self.__mnemonics = mnemonics
        return

    def __str__(self):
        return f"{self.__ref_string}\n{self.__frames}\n{self.__mnemonics}"

    def get_ref_string(self) -> list[int]:
        return self.__ref_string

    def get_frames(self) -> int:
        return self.__frames

    def get_mnemonic(self) -> list[str]:
        return self.__mnemonics


class Algorithm:
    def __init__(self, std_input: StdInput) -> None:
        self.__std_input = std_input
        return

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
