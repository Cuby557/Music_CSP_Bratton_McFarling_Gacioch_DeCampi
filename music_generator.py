'''
@author: Colby Bratton, Jack McFarling, Jonathan Gacioch, Jacob DeCampi

Genetic Algorithm to generate music of a specific genre. Works
via the usage of the pyeasyGA library which gives us a baseline
for constructing a Genetic Algorithm. Requires the creation of 
functions and definitions for the fitness function, mutation functions,
selection function, and the classification of how a single individual
is to be represented in the algorithm itself. Allows us to provide these
functions and then execute to algorithm through simple functions calls.
All of the finer details are handled under the hood by the library.
'''

'''
HOW TO RUN:
It's quite simple! Adjust the number of notes you want in the
melody by changing the initial parameter, x, of Melody(x)
(see below) to whatever you'd like! Once you have the desired
number of notes set, you may execute the code and the rest
is handled for you!

Note: You can also play around with the different options
of the GA in the initialization function of the GA (see below).
This will affect the generation of the melody depending on the
options you choose to change or not change.
'''

from pyeasyga import pyeasyga
from Music_Generator_GA.melody import Melody
from Music_Generator_GA.midi import MIDI
import random

'''
Creates initial individual for the GA to utilize.
(Otherwise, you get a bunch of ones and zeros)
Does so by taking a random melody, shuffling the
melody, and using that as an individual in the GA
'''
def create_individual(data):
    individual = data[:]
    random.shuffle(individual)
    return individual

'''
Fitness Function
Evaluates the intervals between each note by using the 
absolute value between each value. Then, based on 
the corresponding interval we add a set amount of 
fitness "points" to the fitness variable. Since higher 
fitness is desired we set the more pleasing intervals 
to higher values. Furthermore, after the interval checking
we add fitness if a couple key musical elements occur 
at the end of our melody.
'''
def fitness (individual, data):
    fitness = 0
    index = 0
    
    #assign fitness values for all the intervals
    while index < (len(individual) - 1):
        interval = abs(individual[index] - individual[index + 1])
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
    lastNote = individual[len(individual) - 1]
    #Ends on the 1 of the chord - C
    if lastNote == 0 or lastNote == 12 or lastNote == 24:
        fitness += 7
    #ends on the 3 of the chord - E
    elif lastNote == 4 or lastNote == 16:
        fitness += 6
    #ends on the 5 of the chord - G
    elif lastNote == 7 or lastNote == 19:
        fitness += 4

    #add fitness to melodies with penultimate pitch being part of the dominant
    penultNote = individual[len(individual) - 2]
    #5 to 1, G natural
    if penultNote == 7 or penultNote == 19:
        fitness += 7
    #7 to 1, B natural
    elif penultNote == 11 or penultNote == 23:
        fitness += 6
    #2 to 1, D natural
    elif penultNote == 2 or penultNote == 14:
        fitness += 4
        
    return fitness

'''
Mutation Two and Three
Mutation function Two makes a simple mutation by selecting a random
note and incrementing/decrementing it according to the noteList. In
effect, we are making the note higher or lower by one with each
mutation.
Mutation function Three makes a simple mutation by selecting a random
note and swapping it with the note before it (or after it if it is the last
note in the array)
'''
def mutate(individual):
    ### choose random operation and random note to mutate
    mutation_selection = random.randint(0, 1);
    mutate_index = random.randrange(len(individual) - 1)
    
    ### mutation two
    if mutation_selection == 0:
        ### get note's index in noteList
        noteList = [0, 2, 4, 5, 7, 9, 11, 12, 14, 16, 17, 19, 21, 23, 24]
        noteList_index = noteList.index(individual[mutate_index])
        
        ### randomly choose to increment/decrement
        mutation_selection = random.randint(0, 1);
        
        ### increment note according to noteList
        if mutation_selection == 0:
            if noteList_index + 1 >= len(noteList):
                individual[mutate_index] = noteList[noteList_index - 1]
            else:
                individual[mutate_index] = noteList[noteList_index + 1]
            
        ### decrement note according to noteList
        else:
            if noteList_index - 1 > 0:
                individual[mutate_index] = noteList[noteList_index - 1]
            else:
                individual[mutate_index] = noteList[noteList_index + 1]
        
    ### mutation three
    else:
        if mutate_index == (len(individual) - 1):
            # ## swap first and last notes
            individual[0], individual[mutate_index - 1] = \
            individual[mutate_index - 1], individual[0]
        else:
            # ## swap at mutate_index with note in front of it
            individual[mutate_index], individual[mutate_index + 1] = \
            individual[mutate_index + 1], individual[mutate_index]
        
'''
Selection Function
This Selection Function find the Individual with the
best Fitness result and keeps that. Only one Individual
may be passed back to the GA. If multiple Individuals
have the same Fitness result, the first one is returned.
'''
def selection(population):
    best_individual = None
    best_fitness_result = 0
     
    # find individual with best fitness result and save it
    for individual in population:
        if individual.fitness > best_fitness_result:
            best_individual = individual
            best_fitness_result = individual.fitness
              
    return best_individual
         
"""
To Garvey: 
The number of notes in the melody may be changed
to whatever value you would like; in our example, we
use 9 notes. To adjust this, change the initial parameter, x,
of Melody(x) to whatever you'd like! The larger it is,
the longer the melody you will produce!
"""
# Initial melody (nine notes) to utilize in GA
beginning_melody = Melody(9)

# Store notes in modifiable variable to be given to GA
data = beginning_melody.notes.copy()

# The code below is provided by the library to allow us to 
# initialize the GA however we see fit/in a way which 
# best suits our needs. The defined options, which are
# passed as initial parameters, are also provided by the
# library and defined by us. 

# Initialize the GA with the given parameters
# These values may be changed to experience different outputs of the GA
music_generator = pyeasyga.GeneticAlgorithm(data,
                                            population_size=200,
                                            generations=200,
                                            crossover_probability=0,
                                            mutation_probability=0.1,
                                            elitism=True,
                                            maximise_fitness=True)

# The code below is provided by the library to allow us to
# assign our own personally generated functions and definitions
# to the GA to be used during execution. The assignment and execution
# of these functions are handled by the library but the creation
# of the functions is handled by use.

# Set GA functions and attributes equal to those we created
music_generator.create_individual = create_individual
music_generator.fitness_function = fitness
music_generator.mutate_function = mutate
music_generator.selection_function = selection

# Provided by pyeasyGA to execute the algorithm
# Run that sucker!
music_generator.run()

# Retrieve optimal melody; provided and performed by pyeasyGA library
final_melody = music_generator.best_individual()

# Create MIDI files for initial and final
initial_melody_MIDI = MIDI("initial_melody", beginning_melody.notes)
initial_melody_MIDI.create_MIDI_file()
final_melody_MIDI = MIDI("final_melody", final_melody[1])
final_melody_MIDI.create_MIDI_file()


# Print beginning and ending melodies
print("Initial Random Melody: ")
print(beginning_melody.notes)
print("Final Melody: ")
print(final_melody)