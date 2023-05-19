from typing import Any

from mido import MidiFile, MidiTrack

from .support_functions import accords_range, number_to_ghz, get_time_per_note, get_sr_per_note


def prepearing(mid_file: MidiFile) -> tuple[MidiTrack, dict[str, Any]]:
    new_track = MidiTrack()
    config = {
        'control_change': []
    }

    if len(mid_file.tracks) > 1:
        print('WARNING: more than one track')
        [mid_file.tracks.remove(track) for track in mid_file.tracks[1:]]

    for msg in mid_file.tracks[0]:
        if msg.type == 'note_on' or msg.type == 'note_off':
            new_track.append(msg)

        elif msg.type == 'control_change':
            config['control_change'].append({
                'channel': msg.channel,
                'control': msg.control,
                'value': msg.value,
                'time': msg.time,
            })
        
        elif msg.type == 'set_tempo':
            config['set_tempo'] = msg.tempo
    
    return new_track, config

def convert_to_gcode(track: MidiTrack, config: dict[str, Any]) -> str:
    res = ''

    for accord in accords_range(track):
        note_time = get_time_per_note(accord)
        for note in range(len(accord) - 1, -1, -1):
            ghz = number_to_ghz(accord[note].note)
            
            # if note == 0:
            #     res += f'M300 P{get_sr_per_note(accord) - (len(accord) - 1) * note_time} S{ghz}\n'
            # else:
            #     res += f'M300 P{note_time} S{ghz}\n'
            res += f'M300 P{note_time} S{ghz}\n'

    return res