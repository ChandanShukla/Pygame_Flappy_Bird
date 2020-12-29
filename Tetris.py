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