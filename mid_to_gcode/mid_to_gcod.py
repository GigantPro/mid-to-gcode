from mido import MidiFile

from .functions import prepearing, convert_to_gcode


class MidToGcode:
    def __init__(self, track_name: str) -> None:
        self.track_name = track_name
        self.track, self.track_config = prepearing(MidiFile(self.track_name))
        
        self.gcode = convert_to_gcode(self.track, self.track_config)

    def save_gcode(self, filename: str) -> None:
        with open(filename, 'w') as file:
            file.write(self.gcode)
