'''
@author: Colby Bratton, Jack McFarling, Jonathan Gacioch, Jacob DeCampi
'''
from pyeasyga import pyeasyga
from Music_Generator_GA.melody import Melody
import random

'''
Creates initial individual for the GA to utilize
(Otherwise, you get a bunch of ones and zeros
'''
def create_individual(data):
    return data[:]

'''
Fitness function
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
        
    return fitness

'''
Mutation Three: swapping two notes
Mutation function that makes a simple mutation by selection a random
note and swapping it with the note before it (or after it if it is the last
note in the array)
'''
def mutate(individual):
    mutate_index = random.randrange(len(individual) - 1)
    
    if mutate_index == (len(individual) - 1):
        ### swap last two notes
        individual[mutate_index], individual[mutate_index - 1] = \
        individual[mutate_index - 1], individual[mutate_index]
    else:
        ### swap at mutate_index with note in front of it
        individual[mutate_index], individual[mutate_index + 1] = \
        individual[mutate_index + 1], individual[mutate_index]
        
'''
Selection Function
NOT COMPLETED!
'''
def selection(population):
    pop_size = len(population)
    print(population)
    
# Initial melody (nine notes) to utilize in GA
beginning_melody = Melody(9)

# Store notes in modifiable variable to be given to GA
data = beginning_melody.notes.copy()

# Initialize the GA with the given parameters
music_generator = pyeasyga.GeneticAlgorithm(data,
                                            population_size=10,
                                            generations=100,
                                            crossover_probability=0,
                                            mutation_probability=0.1,
                                            elitism=True,
                                            maximise_fitness=True)

# Set GA functions and attributes equal to those we created
music_generator.create_individual = create_individual
music_generator.fitness_function = fitness
music_generator.mutate_function = mutate
###music_generator.selection_function = selection

# Run that sucker!
music_generator.run()

# Print beginning and ending melodies
print("Initial Random Melody: ")
print(beginning_melody.notes)
print("Final Melody: ")
print(music_generator.best_individual())