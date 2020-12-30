import numpy as np
import math


def get_segment_lengths(colours):
    '''
        Decides how long each 'submap' should be.
        basically a bit of math to divide 256 into even chunks,
        and evenly distributing the remainders.
    '''

    segment_length = math.floor(256/(len(colours)-1))
    lengths = list([segment_length for n in range(len(colours)-1)])
    remainder = 256%(len(colours)-1)

    if remainder != 0:
        for i in np.linspace(0,len(lengths)-1,remainder):
            lengths[int(i)] += 1

    return lengths


def linear(colours):
    '''
        Creates a colourmap of a linear fade between the specified colours.
        
        Colours should be an n by 3 2d list/tuple eg [[0,0,0], [255,255,255]].
        This would create a colourmap of white to black/off.
        
        More than 2 colours may be specified eg: [[255,0,0],[0,255,0],[0,0,255]].
        This will create a map from red to green to blue.
    '''

    lengths = get_segment_lengths(colours)
    
    cmap = []
    
    for i in range(len(lengths)):
        cmap.extend(np.linspace(colours[i],colours[i+1],lengths[i]).astype(int))
    
    return cmap


def save(colourmap, name):
    with open(name+".cmap", "wb") as file:
        for colour in colourmap:
            for RGB in colour:
                file.write(int(RGB).to_bytes(1,"big"))
            file.write(b'\n')


def new_map(colours, name, fade = "linear"):
    '''
        Creates and saves a new colourmap.
        Colours should be entered in a 2d n by 3 list/tuple with values ranging from
        0-255 (inclusive) eg:
        [[0,0,0],[255,255,255],[255,0,0]]
    '''
    if fade == "linear":
        cmap = linear(colours)
    save(cmap, name)

    
