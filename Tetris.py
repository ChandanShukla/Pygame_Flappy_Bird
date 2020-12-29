from random import randrange as rand
import pygame, sys  #importing the pygame and sys module

config = {			#defining the game window properties
	'cell_size':25,
	'cols':20,
	'rows':20,
	'delay':750,
	'maxfps':30
}

colors = [			#defining the colors of the blocks
(0,   0,   0  ),
(255, 0,   0  ),
(0,   150, 0  ),
(0,   0,   255),
(255, 120, 0  ),
(255, 255, 0  ),
(180, 0,   255),
(0,   220, 220)
]
tetris_shapes = [
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 2, 2],
    [2, 2, 0]],

    [[3, 3, 0],
    [0, 3, 3]],

    [[4, 0, 0],
    [4, 4, 4]],

    [[0, 0, 5],
    [5, 5, 5]],

    [[6, 6, 6, 6]],

    [[7, 7],
    [7, 7]]

]