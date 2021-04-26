'''
@author: Colby Bratton, Jack McFarling, Jonathan Gacioch, Jacob DeCampi
'''

import random

class Melody:
    """
    Simple representation of  melody.  Assumes melody is in C major spanning
    two octaves from c4 to c6 (inclusive) with 0 being c4 and 24 being c6.
    Also assumes a pre-defined rhythmic structure, let's begin with saying
    that they are all equal duration notes. The single parameter specifies
    the number of notes in the melody.
    """
    def __init__(self, length):
        """
        Generate a random melody based off of the provided note list
        """
        # Receive how many notes should be in the melody
        self.length = length
        # Initialize size of melody's note list
        self.notes = [0] * self.length
        
        noteList = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24]
        
        # randomly assign notes to each index in the melody's
        # note list
        i = 0
        while i < self.length:
            self.notes[i] = random.choice(noteList)
            i += 1
            
    def displayMelody(self):
        """
        string representation of melody
        """
        print(self.notes)