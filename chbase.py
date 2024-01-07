#!/usr/bin/env python

"""
    Created by Red-exe-Engineer (Wallee).
    Converts numbers with a given base to a given base.
"""

import argparse


BASES = {**{str(i): i for i in range(2, 37)}, "bin": 2, "dec": 10, "oct": 12, "hex": 16}
CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# Used some code from https://stackoverflow.com/a/2267446/19348326
def convert_number(number: str) -> str:
    if start_base == end_base:
        return number

    try:
        number = int(number, start_base)
    except:
        parser.error(f'"{number}" is invalid for base "{start_base}"')

    if number > 0:
        invert = False
    elif number < 0:
        invert = True
        number *= -1
    else:
        return "0"

    digits = []

    while number:
        digits.insert(0, CHARS[number % end_base])
        number //= end_base

    return "-" * invert + "".join(digits)


def check_char_pad(value):
    if len(value) not in (0, 1):
        raise argparse.ArgumentTypeError("Value must be a single character")

    return value


parser = argparse.ArgumentParser(
    prog="chbase",
    description="Convert numbers between different bases.",
    epilog="Note: supports bases 2-36 and names like bin, dec, oct, and hex"
)

parser.add_argument("-t", "--to",   metavar="base", choices=BASES.keys(), default=16,  help="output base value, defaults to 16")
parser.add_argument("-f", "--from", metavar="base", choices=BASES.keys(), default=10,  help="input base value, defaults to 10")
parser.add_argument("-p", "--pad",  metavar="char", type=check_char_pad,  default=" ", help="padding character (length 0-1)")
parser.add_argument("values",       metavar="values [...]", nargs=argparse.REMAINDER,  help="input values")

args = parser.parse_args()

if not args.values:
    parser.error("Needs at least 1 value")

start_base, end_base = BASES[str(args._get_kwargs()[1][1])], BASES[str(args.to)]
numbers = tuple(map(convert_number, args.values))
largest = max(map(len, numbers))

if args.pad:
    print(*map(lambda i: i.rjust(largest, args.pad), numbers), sep="\n")
else:
    print(*numbers, sep="\n")
