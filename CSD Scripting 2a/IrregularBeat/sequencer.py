import time
import random
from midiutil import MIDIFile

# Sequencer class
class Sequencer:
  # Constructor
  def __init__(self, bpm=120, beats=4, beatUnit=4, events=[]):
    self.bpm = bpm # Beats per minute
    self.beats = beats # Number of beats in the bas
    self.beatUnit = beatUnit # Which note represents one beat
    self.events = events # A list of tuples (event time in beats, sample)
    
  # Plays the sequence (blocking method)
  def play(self, sampler):  
    # Copy the event list for re-usage and sort them by time
    events = self.events[:]
    events.sort()
    
    # Calculate the duration of a 16th note
    beatDuration = 60.0 / self.bpm
    noteDuration = beatDuration / self.beatUnit
    
    # Convert event indices to seconds
    events = [(event[0] * noteDuration,event[1]) for event in events]
    
    # If there are no events, then just return
    if not events:
      return
    
    # Retrieve the first event if there is any
    event = events.pop(0)
    
    # Get the start time
    startTime = time.time();
    
    # Play the sequence as long as there are events
    while True:
      # Retrieve the current time
      currentTime = time.time()
      # Check if the time of the event is passed
      if currentTime - startTime >= event[0]:
        # Play the sample of the event
        sampler[event[1]].play()
        # If there are more events
        if events:
          # Get the next event
          event = events.pop(0)
        # Otherwise stop the loop
        else:
          break
    
      # Otherwise wait for a short moment
      else:
        time.sleep(0.001)
        
  # Export the sequence to a MIDI file
  def export_midi(self, fileName, pitches=[36,38,42]):
    # Create a MIDI file
    midi = MIDIFile(1,adjust_origin=True)
    
    # Add the tempo track
    midi.addTempo(0,0,self.bpm)
    
    # Add the events as notes
    for event in self.events:
      # Calculate the time and duration (and other variables)
      channel = 9 # Because 0-15
      pitch = pitches[event[1]]
      time = event[0] / self.beatUnit
      duration = 1
      velocity = 100
      # Add the note
      midi.addNote(0,channel,pitch,time,duration,velocity)
    
    # Export the file
    try:
      # Open the file
      with open(fileName,"wb") as output:
        # Write the MIDI to the file
        midi.writeFile(output)
      return True
    except IOError:
      # Error, return False
      return False
        
  # Recursively generates a list of patterns
  # Returns a list containing lengths of the patterns
  @staticmethod
  def generate_patterns(length):
    if length == 2:
      # Add a 2-pattern
      return [2]
    elif length == 3:
      # Add a 3-pattern
      return [3]
    elif length == 4:
      # Add a 4-pattern or two 2-patterns
      return random.choice([[4],[2,2]])
    elif length == 5:
      # Add a 2-3 or 3-2
      return random.choice([[2,3],[3,2]])
    else:
      # Add a random pattern
      currentLength = random.choice([2,3,4])
      return [currentLength] + Sequencer.generate_patterns(length - currentLength)
  
  # Generate an irregular sequence
  # Returns a sequencer with a generated beat
  @classmethod 
  def generate_irregular_beat(cls, bpm=120, beats=4, beatUnit=4):
    # Calculate the number of 16th notes
    noteCount = 16 / beatUnit * beats
  
    # Generate a list of pattern lengths
    patterns = Sequencer.generate_patterns(noteCount)
        
    # Create an empty event list
    events = []
        
    # Generate a kick and snare pattern using the lengths
    eventPosition = 0
    for pattern in patterns:
      # Append a kick event at the start of the pattern
      events.append((eventPosition,0))
      
      # Append a snare event at a random position in the pattern
      snarePosition = random.randrange(1,pattern)
      events.append((eventPosition + snarePosition,1))
      
      # Fill the gaps with hats
      for hatPosition in range(pattern):
        if hatPosition != snarePosition:
          events.append((eventPosition + hatPosition,2))
    
      # Increase the event position
      eventPosition += pattern
    
    # Return a new sequencer with the event list
    return cls(bpm,beats,beatUnit,events)
