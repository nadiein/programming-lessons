# Function should convert passing in RGB decimal values in a hexadecimal representation


class WrongType(Exception):
    pass

# Solution one
def rgb_one(r, g, b):
    # Round values that are out of range
    r = max(0, min(255, round(r)))
    g = max(0, min(255, round(g)))
    b = max(0, min(255, round(b)))

    # Convert to hexadecimal string and pad with zeros if necessary
    return '{:02X}{:02X}{:02X}'.format(r, g, b)

# Solution two
def rgb_two(r, g, b):
    # Round values that are out of range
    r = max(0, min(255, round(r)))
    g = max(0, min(255, round(g)))
    b = max(0, min(255, round(b)))

    # Convert to hexadecimal using bit-shifting
    hex_value = (r << 16) + (g << 8) + b

    # Format as a 6-digit hexadecimal string
    return '{:06X}'.format(hex_value)

# Solution three
def rgb_three(r, g, b):
    # Round values that are out of range
    r = max(0, min(255, round(r)))
    g = max(0, min(255, round(g)))
    b = max(0, min(255, round(b)))

    # Convert to hexadecimal using the built-in hex() function
    hex_r = hex(r)[2:].zfill(2)
    hex_g = hex(g)[2:].zfill(2)
    hex_b = hex(b)[2:].zfill(2)

    # Concatenate the hexadecimal values
    hex_value = hex_r + hex_g + hex_b

    return hex_value.upper()

# Solution four
import struct

def rgb_four(r, g, b):
    # Round values that are out of range
    r = max(0, min(255, round(r)))
    g = max(0, min(255, round(g)))
    b = max(0, min(255, round(b)))

    # Pack RGB values into a binary string
    binary_str = struct.pack('BBB', r, g, b)

    # Convert binary string to a hexadecimal string
    hex_str = binary_str.hex()

    return hex_str.upper()

# Solution five
def rgb_five(r, g, b):
    # Round values that are out of range
    r = max(0, min(255, round(r)))
    g = max(0, min(255, round(g)))
    b = max(0, min(255, round(b)))

    # Convert RGB values to hexadecimal digits
    hex_r = hex((r >> 4) * 16 + (r & 15))[2:].zfill(2)
    hex_g = hex((g >> 4) * 16 + (g & 15))[2:].zfill(2)
    hex_b = hex((b >> 4) * 16 + (b & 15))[2:].zfill(2)

    # Concatenate the hexadecimal values
    hex_value = hex_r + hex_g + hex_b

    return hex_value.upper()



import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('cut_log(230, 4, xs)')

    start_time = time.time()
    cut_log(230, 4, xs)
    end_time = time.time()

    print('', end_time - start_time)
