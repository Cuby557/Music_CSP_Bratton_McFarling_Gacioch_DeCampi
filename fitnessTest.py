### File melody.py
### Representation of a melody

import random

class Melody:
    """
    Simple representation of  melody.  Assumes melody is in C major spanning
    two octaves from c4 to c6 (inclusive) with 0 being c4 and 24 being c6.
    Also assumes a pre-defined rhythmic structure, let's begin with saying
    that they are all eqaul duration notes. The single parameter specifies
    the number of notes in the melody.
    """
    def __init__(self, length):
        self.length = length
        self.notes = [0] * self.length
        noteList = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24]
        i = 0
        while i < self.length:
            self.notes[i] = random.choice(noteList)
            i += 1
    def displayMelody(self):
        """
        string represetation of melody
        """
        print(self.notes)
    
def fitness(individual):
	fitness = 0
	index = 0
	
	#assign fitness values for all the intervals
	while index < (len(individual.notes) - 1):
		interval = abs(individual.notes[index] - individual.notes[index + 1])
		#Unison, Perfect 4th, Perfect 5th, Octave
		if interval == 0 or interval == 5 or interval == 7 or interval == 12:
			fitness += 10
		#Minor 3rd, Major 3rd, Minor 6th, Major 6th
		elif interval == 3 or interval == 4 or interval == 8 or interval == 9:
			fitness += 7
		#Minor 2nd, Major 2nd, Minor 7th, Major 7th
		elif interval == 1 or interval == 2 or interval == 10 or interval == 11:
			fitness += 4
		#Tri-Tone, Greater than an octave
		elif interval == 6 or interval > 12:
			fitness += 1
		index += 1
	
	#add extra fitness to melodies ending on certain "good" pitches
	lastNote = individual.notes[len(individual.notes) - 1]
	#Ends on the 1 of the chord - C
	if lastNote == 0 or lastNote == 12 or lastNote == 24:
		fitness += 7
	#ends on the 3 of the chord - E
	elif lastNote == 4 or lastNote == 16:
		fitness += 6
	#ends on the 5 of the chord - G
	elif lastNote == 7 or lastNote == 19:
		fitness += 4
		
	return fitness

m1 = Melody(9)
m1.displayMelody()
fit = fitness(m1)
print(fit)
