# Write a function which formats a duration, given as a number of seconds, in a human-friendly way.
# The function must accept a non-negative integer. If it is zero, it just returns "now".
# Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.


class WrongType(Exception):
    pass

# Solution one
def format_duration(seconds):
    if seconds == 0:
        return 'now'

    units = [
        (60 * 60 * 24 * 365, 'year'),
        (60 * 60 * 24, 'day'),
        (60 * 60, 'hour'),
        (60, 'minute'),
        (1, 'second'),
    ]

    components = []

    for unit_time, unit_name in units:
        if seconds >= unit_time:
            count = seconds // unit_time
            seconds = seconds % unit_time

            if count > 1:
                unit_name = unit_name + 's'

            components.append(f'{count} {unit_name}')

    if len(components) > 1:
        return ' and '.join([', '.join(components[:-1]), components[-1]])
    else:
        return components[0]


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('format_duration(1)')
    cProfile.run('format_duration(62)')

    start_time = time.time()
    format_duration(3662)
    end_time = time.time()
    print('', end_time - start_time)
