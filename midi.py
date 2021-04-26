'''
@author: Colby Bratton, Jack McFarling, Jonathan Gacioch, Jacob DeCampi
'''
from midiutil import MIDIFile

class MIDI:
    '''
    Class to generate MIDI files that will allow the 
    user to listen to the melodies that are created
    in music_generator.py. Takes the notes of the melody
    in their integer representations and creates a MIDI
    file according to the provided notes and options
    '''
    def __init__(self, name, melody):
        """
        Retrieve notes of the melody and the file name
        of the MIDI file to be created
        """
        # Copy the notes of the current melody
        self.degrees = melody.copy()
        # Receive file name of the MIDI file to be created
        self.file_name = name
    
        # Set notes within range (project specific, predefined)
        for index in range(len(self.degrees)):
            self.degrees[index] = int(self.degrees[index]) + 60
        
    def create_MIDI_file(self):
        """
        Creates a MIDI file for the current melody
        """
        track = 0
        channel = 0
        time = 0  # In beats
        duration = 1  # In beats
        tempo = 100  # In BPM
        volume = 100  # 0-127, as per the MIDI standard

        # One track, defaults to format 1 (tempo track is created automatically)
        MyMIDI = MIDIFile(1)
    
        MyMIDI.addTempo(track, time, tempo)

        # Add melody's notes to the MIDI file
        for i, pitch in enumerate(self.degrees):
            MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

        # Open and write melody data to MIDI file
        with open(self.file_name + ".mid", "wb") as output_file:
            MyMIDI.writeFile(output_file)