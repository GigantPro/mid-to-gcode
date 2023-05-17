from typing import Iterable, Iterator


def pair_range(subject: Iterable) -> Iterator:
    last = None
    for item in subject:
        if last:
            yield last, item
            last = None
        
        else:
            last = item

def number_to_ghz(number: int) -> str:
    octo_size = 12
    A = 27.0  # ghz
    
    num_at_octo = number % octo_size
    new_A = A * (2 ** (number // (octo_size - 1)))
    
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
    return ghz_str[:2 + ghz_str.index('.')]
