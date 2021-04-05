### File melody.py
### Representation of a melody

import random

class Melody:
    """
    Simple representation of  melody.  Assumes melody is in C major spanning
    two octaves from c4 to c6 (inclusive) with 0 being c4 and c6 being 14.
    Also assumes a pre-defined rhythmic structure, let's begin with saying
    that they are all eqaul duration notes. The single parameter specifies
    the number of notes in the melody.
    """
    def __init__(self, length):
        self.length = length
        self.notes = [0] * self.length
        i = 0
        while i < self.length:
            self.notes[i] = random.randint(0, 14)
            i += 1
    def displayMelody(self):
        """
        string represetation of melody
        """
        print(self.notes)
    
m1 = Melody(10)
m1.displayMelody()