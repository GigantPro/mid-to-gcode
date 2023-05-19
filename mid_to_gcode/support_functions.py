from typing import Iterator

from mido import MidiTrack


def accords_range(subject: MidiTrack) -> Iterator:
    accord = []
    count_closed = 0
    for item in subject:
        if count_closed == len(accord) and accord:
            yield accord
            accord.clear()
            count_closed = 0
        
        if item.type == 'note_on':
            accord.append(item)
        elif item.type == 'note_off':
            for note in accord:
                if note.note == item.note:
                    accord[accord.index(note)].time = note.time + item.time
                    break
            count_closed += 1
    return accord

def number_to_ghz(number: int) -> float:
    octo_size = 12
    A = 27.0  # ghz
    
    num_at_octo = number % octo_size
    new_A = A * (2 ** ((number // octo_size) - 1))
    
    config = {
        9: new_A,
        10: new_A * (16 / 15),
    }
    
    config[11] = config[10] * 1.0546875
    config[8] = config[9] * 0.96
    config[7] = config[8] * 0.9375
    config[6] = config[7] * 0.9375
    config[5] = config[6] * (128 / 135)
    config[4] = config[5] * 0.9375
    config[3] = config[4] * 0.96
    config[2] = config[3] * 0.9375
    config[1] = config[2] * (128 / 135)
    config[0] = config[1] * 0.9375

    ghz_str = str(config[num_at_octo])
    return float(ghz_str[:2 + ghz_str.index('.')])

def get_time_per_note(notes: list) -> float:
    sr = get_sr_per_note(notes)

    # if sr > 70:
    #     return 70
    return sr

def get_sr_per_note(notes: list) -> float:
    sum_ = 0
    for note in notes:
        sum_ += note.time

    return sum_ / len(notes)
