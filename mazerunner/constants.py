"""MazeRunner Constants.

Constants shared by all sub-modules.

Author: Lucas David -- <ld492@drexel.edu>
License: MIT (c) 2016

"""
from enum import Enum


class Actions(Enum):
    FORWARD = 0
    BACKWARD = 1
    CLOCKWISE = 2
    CCLOCKWISE = 3


class AgentStates(Enum):
    CLOSE = 0
    FARAWAY = 1
    COLLISION = 2
    CLOSE_TO_GOAL = 10
    SOME_PLACE = 11
    MOVED_AWAY = 12


STATES = Enum('disabled', 'idle', 'moving', 'thinking', 'stuck', 'dead')

MAX_LEARNING_CYCLES = 1000
IMMINENT_COLLISION_THRESHOLD = .2
