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
    def __init__(self, ref_string: list[int], frames: int, mnemonics: list[str]) -> None:
        self.__ref_string = ref_string
        self.__frames = frames
        self.__mnemonics = mnemonics


    def __str__(self) -> str:
        return f"{self.__ref_string}\n{self.__frames}\n{self.__mnemonics}"

    def get_ref_string(self) -> list[int]:
        return self.__ref_string

    def get_frames(self) -> int:
        return self.__frames

    def get_mnemonic(self) -> list[str]:
        return self.__mnemonics

