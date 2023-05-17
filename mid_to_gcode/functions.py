from typing import Any

from mido import MidiFile, MidiTrack

from .support_functions import pair_range, number_to_ghz


def prepearing(mid_file: MidiFile) -> tuple[MidiTrack, dict[str, Any]]:
    new_track = MidiTrack()
    config = {
        'control_change': []
    }

    if len(mid_file.tracks) > 1:
        print('WARNING: more than one track')
        [mid_file.tracks.remove(track) for track in mid_file.tracks[1:]]

    use_accords_flag = False
    last_note = None
    for msg in mid_file.tracks[0]:
        if msg.type == 'note_on':
            if not last_note and msg.velocity != 0:
                last_note = msg.note
                new_track.append(msg)

            elif msg.velocity == 0 and last_note == msg.note:
                new_track.append(msg)
                last_note = None
            
            elif last_note and msg.velocity != 0:
                use_accords_flag = True

        elif msg.type == 'control_change':
            config['control_change'].append({
                'channel': msg.channel,
                'control': msg.control,
                'value': msg.value,
                'time': msg.time,
            })
        
        elif msg.type == 'set_tempo':
            config['set_tempo'] = msg.tempo
    
    if use_accords_flag:
        print('WARNING: the library can\'t process chords yet! From them the upper note is taken')
    
    return new_track, config

def convert_to_gcode(track: MidiTrack, config: dict[str, Any]) -> str:
    res = ''

    for note_start, note_finish in pair_range(track):
        note_time = note_finish.time + note_start.time
        ghz = number_to_ghz(note_start.note)
        
        res += f'M300 P{note_time} S{ghz}\n'

    return res