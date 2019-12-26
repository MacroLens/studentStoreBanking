#!/usr/bin/python3
import subprocess


def decode():
    try:
        var = subprocess.check_output('./chip_reader').decode('utf-8').strip()  # declare variable var, read the output of quick_start_example1 script and decode it from the UTF-8 format and strip it of any extra trailing characters like line breaks
        hex_list = var.split()  # takes the string, splits it by spaces, and makes it into a list
        for x in range(len(hex_list)):  # for every hex number in the list go through it and turn it into a decimal interger
            hex_list[x] = int(hex_list[x], 16) # converts Hexidecimal to decimal so it's easy to mess with.
        nfcUID = hex_list[3]  # Creating a unique code to identify a card, take the decimals and bitshift them around
        nfcUID <<= 8; nfcUID |= hex_list[2]  # Shift left 8 bits, += the third decimal
        nfcUID <<= 8; nfcUID |= hex_list[1]  # etc
        nfcUID <<= 8; nfcUID |= hex_list[0]  # etc
    except (OSError, subprocess.CalledProcessError) as e:
        return False
    return str(nfcUID)