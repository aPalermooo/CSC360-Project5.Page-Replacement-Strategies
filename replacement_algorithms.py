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
from random import randint

class Algorithm:
    def __init__(self, std_input: StdInput) -> None:
        self.__std_input = std_input

    # FRAME WITH COUNTER
    # init_state = [-1,0]
    # frames_list = []
    # for frame in range(num_of_frames):
    #     frames_list.append(init_state)
    # frames_list = tuple(frames_list)

    #TODO: CHECK ACCURACY

    @staticmethod
    def FIFO(ref_string : list[int], num_of_frames : int) -> int:
        """
        Applies a First in First out algorithm to place pages into frames
            (Using a queue implementation)
        :param ref_string:      order of pages called in memory
        :param num_of_frames:   number of frames available in memory
        :return:                number of page faults
        """
        page_faults = 0
        frames_list = [-1] * num_of_frames
        for page in ref_string:
            if page in frames_list:
                continue
            else:
                frames_list.append(page)
                frames_list.pop(0)
                page_faults += 1
        return page_faults

    @staticmethod
    def LRU(ref_string : list[int], num_of_frames : int) -> int:
        """
        Applies an algorithm to place pages into frames that places pages into frames
        of pages that have been in memory the longest
        :param ref_string:      order of pages called in memory
        :param num_of_frames:   number of frames available in memory
        :return:                number of page faults
        """
        page_faults = 0
        frames_list = [-1] * num_of_frames
        index = 0
        for page in ref_string:
            if page in frames_list:
                continue
            else:
                frames_list[index] = page
                index = (index + 1) % num_of_frames
                page_faults += 1
        return page_faults

    @staticmethod
    def OPT(ref_string : list[int], num_of_frames : int) -> int:
        #TODO: OPTIMAL
        page_faults = 0
        return page_faults

    @staticmethod
    def RAND(ref_string : list[int], num_of_frames : int) -> int:
        """
        Applies an algorithm to place pages into frames that places pages into random frames
        :param ref_string:      order of pages called in memory
        :param num_of_frames:   number of frames available in memory
        :return:                number of page faults
        """
        page_faults = 0
        frames_list = [-1] * num_of_frames
        for page in ref_string:
            if page in frames_list:
                continue
            else:
                index = randint(0, num_of_frames-1)
                frames_list[index] = page
                page_faults += 1
        return page_faults


    def calculate(self) -> int:
        """
        Calls functions listed by input mnemonics to apply algorithms and prints their output
        :return: 0 for success, 1 for formatting error
        """
        ref_string =  self.__std_input.get_ref_string()
        frames =  self.__std_input.get_frames()
        mnemonics =  self.__std_input.get_mnemonic()

        for mnemonic in mnemonics:
            if mnemonic == "FIFO":
                result = "FIFO:\t"
                result += str(self.FIFO(ref_string, frames))
            elif mnemonic == "LRU":
                result = "LRU:\t"
                result += str(self.LRU(ref_string, frames))
            elif mnemonic == "OPT":
                result = "OPT:\t"
                result += str(self.OPT(ref_string, frames))
            elif mnemonic == "RAND":
                result = "RAND:\t"
                result += str(self.RAND(ref_string, frames))
            else:
                print(f"ERROR: {mnemonic} is not a valid mnemonic, check input file.")
                return 1
            print(result)
        return 0
#end class
