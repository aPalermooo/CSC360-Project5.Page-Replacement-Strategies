"""
"
"   File:       std_input.py
"   Author:     Xander Palermo <ajp2s@missouristate.edu>
"   Course:     CSC360 - Operating Systems
"   Instructor: Dr. Siming Liu
"   Project:    5 - Simulation of Page Replacement Strategies
"   Date:       30 October 2024
"
"""

class StdInput:
    """
    A class that acts as a container for input data
    Attributes:
        __ref_string    the reference string (order that pages are called in)
        __frames        number of frames available for pages to be stored in
        __mnemonics     shorthand keywords that tell the program which algorithms to run
    """

    ''' Override methods '''
    def __init__(self, ref_string: list[int], frames: int, mnemonics: list[str]) -> None:
        """
        Creates new instance of a standard input object
        :param ref_string:  list[int];
                            reference string (order that pages are called in)
        :param frames:      int;
                            number of frames available for pages to be stored in
        :param mnemonics:   list[str];
                            shorthand keywords that tell the program which algorithms to run
        """
        self.__ref_string = ref_string
        self.__frames = frames
        self.__mnemonics = mnemonics


    def __str__(self) -> str:
        return f"{self.__ref_string}\n{self.__frames}\n{self.__mnemonics}"

    ''' Getter Methods '''
    def get_ref_string(self) -> list[int]:
        """
        :return: reference string from input
        """
        return self.__ref_string

    def get_frames(self) -> int:
        """
        :return: number of frames available from input
        """
        return self.__frames

    def get_mnemonic(self) -> list[str]:
        """
        :return: shorthand keywords of algorithms to run from input
        """
        return self.__mnemonics

