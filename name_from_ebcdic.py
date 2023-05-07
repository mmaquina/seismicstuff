#!/usr/bin/python3

import codecs
import sys 

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:  ./name_from_ebcdic line position")
        print("Example:  ./name_from_ebcdic 5 45")
        exit()
    else:
        line = int(sys.argv[1])
        position = int(sys.argv[2])

    with open("326023_3.segy", "rb") as ebcdic:
        ascii_txt = codecs.decode(ebcdic.read(80*40), "cp500")
        print(len(ascii_txt[(line - 1)*80 + position - 1 : line*80].strip(' ')))