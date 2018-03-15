import argparse
import re

def hextorgb(candidate):
    # if the first character is a hash then remove it
    if candidate.startswith("#"):
        candidate = candidate[1:]

    # check the value is in a valid format
    if is_hex(candidate):
        red = int(candidate[0:2], 16)
        green = int(candidate[2:4], 16)
        blue = int(candidate[4:6], 16)
        return (red, green, blue)
    else:
        return -1

def is_hex(val):
    pattern = re.compile("[0-9A-Fa-f]{6}")
    if pattern.fullmatch(val) is None:
        return False
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Get RGB from Hex.')
    parser.add_argument('hex', type=str, help='The hex value.')
    args = parser.parse_args()
    print("{} is {}".format(args.hex, hextorgb(args.hex)))