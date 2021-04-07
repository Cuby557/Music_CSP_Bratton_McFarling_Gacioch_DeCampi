"""
Function to calculate the fitness of a melody object. Analyzes the intervals 
between each note, assigning fitness points to each. Also, add bonus fitness 
value points for ending on certain pitches.
Not it's own class, but I wanted to get the code out to everyone to be checked
"""
def fitness(individual):
	fitness = 0
	index = 0
	
	#assign fitness values for all the intervals
	while index < (individual.notes.length - 1):
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
	lastNote = individual.notes[individual.notes.length - 1]
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
