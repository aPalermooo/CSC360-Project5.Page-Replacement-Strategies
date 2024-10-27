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
        self.ref_string = ref_string
        self.frames = frames
        self.mnemonics = mnemonics
        return