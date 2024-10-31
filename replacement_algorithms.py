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
from random import randint

from std_input import StdInput

class Algorithm:
    """
    Encapsulates page replacement algorithms that can be performed on a reference string of pages
    Supported Algorithms:
        - FIFO (First In First Out)
        - LRU  (Least Recently Used)
        - OPT  (Optimized; Minimal Page Faults)
        - RAND (Random Selection)
    All Algorithms can be called statically

    Attributes:
        __std_input (StdInput): a formatted input structure that contains a reference string of pages, the number of frames available
                                and the desired algorithms to be applied to them

    Methods:
        FIFO() : Applies a First in First out algorithm to place pages into frames
                    (Using a queue implementation)
        LRU()  : Applies an algorithm to place pages into frames that places pages into frames
                 of pages that have been in memory the longest
                    (Through a stack implementation)
        OPT()  : Applies an algorithm to place pages into optimally chosen frames by replacing values that
                 will not be used for the longest period of time
                    (Through a recursive implementation)
        RAND() : Applies an algorithm to place pages into frames that places pages into random frames

        calculate() : Calls functions listed by input mnemonics to apply algorithms and prints their output
    """

    def __init__(self, std_input: StdInput) -> None:
        self.__std_input = std_input

    @staticmethod
    def FIFO(ref_string: list[int], frames_list: list[int]) -> int:
        """
        Applies a First in First out algorithm to place pages into frames
            (Using a queue implementation)
        :param ref_string:      order of pages called in memory
        :param frames_list:     a representation of the state of the memory and the pages it currently holds
        :return:                number of page faults
        """
        page_faults = 0
        for page in ref_string:
            if page in frames_list:
                # Do Nothing
                continue
            else:
                frames_list.append(page)
                frames_list.pop(0)
                page_faults += 1
        return page_faults

    @staticmethod
    def LRU(ref_string: list[int], frames_list: list[int]) -> int:
        """
        Applies an algorithm to place pages into frames that places pages into frames
        of pages that have been in memory the longest
            (Through a stack implementation)
        :param ref_string:      order of pages called in memory
        :param frames_list:     a representation of the state of the memory and the pages it currently holds
        :return:                number of page faults
        """
        page_faults = 0
        for page in ref_string:
            if page in frames_list:
                frames_list.append(page)
                frames_list.pop(0)
                continue
            else:
                frames_list.append(page)
                frames_list.pop(0)
                page_faults += 1
        return page_faults

    @staticmethod
    def OPT(ref_string: list[int], frames_list: list[int]) -> int:
        """
        Applies an algorithm to place pages into optimally chosen frames by replacing values that
        will not be used for the longest period of time
            (Through a recursive implementation)
        :param ref_string:      order of pages called in memory
        :param frames_list:     a representation of the state of the memory and the pages it currently holds
        :return:                number of page faults
        """
        # End Condition
        if len(ref_string) == 0:
            return 0

        if ref_string[0] in frames_list:
            # Do nothing; continue recursion
            return Algorithm.OPT(ref_string[1:], frames_list)
        else:
            # Find the page that will go the longest without use (the victim)
            victim_index = 0
            victim_next_occurrence = ref_string.index(ref_string[victim_index])
            for index in range(len(frames_list)):
                if frames_list[index] not in ref_string:
                    victim_index = index
                    break
                elif victim_next_occurrence < ref_string.index(frames_list[index]):
                    victim_index = index
            frames_list[victim_index] = ref_string[0]

            # Add 1 to page fault count; continue recursion
            return Algorithm.OPT(ref_string[1:], frames_list) + 1

    @staticmethod
    def RAND(ref_string: list[int], frames_list: list[int]) -> int:
        """
        Applies an algorithm to place pages into frames that places pages into random frames
        :param ref_string:      order of pages called in memory
        :param frames_list:     a representation of the state of the memory and the pages it currently holds
        :return:                number of page faults
        """
        page_faults = 0
        for page in ref_string:
            if page in frames_list:
                # Do Nothing
                continue
            else:
                index = randint(0, len(frames_list) - 1)
                frames_list[index] = page
                page_faults += 1
        return page_faults

    def calculate(self) -> int:
        """
        Calls functions listed by input mnemonics to apply algorithms and prints their output
        :return:    0 for success,
                    1 for formatting error
        """
        ref_string = self.__std_input.get_ref_string()
        frames = self.__std_input.get_frames()
        mnemonics = self.__std_input.get_mnemonic()

        # Perform Algorithms and print Result
        for mnemonic in mnemonics:
            frames_list = [-1] * frames
            if mnemonic == "FIFO":
                result = "FIFO:\t"
                result += str(self.FIFO(ref_string, frames_list))
            elif mnemonic == "LRU":
                result = "LRU:\t"
                result += str(self.LRU(ref_string, frames_list))
            elif mnemonic == "OPT":
                result = "OPT:\t"
                result += str(self.OPT(ref_string, frames_list))
            elif mnemonic == "RAND":
                result = "RAND:\t"
                result += str(self.RAND(ref_string, frames_list))
            else:
                print(f"ERROR: {mnemonic} is not a valid mnemonic, check input file.")
                return 1
            print(result)
        return 0

