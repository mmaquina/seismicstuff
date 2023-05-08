#!/usr/bin/python3

import codecs
import sys 
import os

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage:  ./name_from_ebcdic line(1 is the top line) position(1 is the leftomst character position) [length(characters)]")
        print("Example:  ./name_from_ebcdic 5 45 7")
        print("Example:  ./name_from_ebcdic 5 45")
        print("In the latter example length is from position to the end of the line.")
        exit()
    else:
        line = int(sys.argv[1])
        position = int(sys.argv[2])
        length = 80 - position + 1
        if len(sys.argv) == 4:
            length = int(sys.argv[3])


    for path in os.walk('.'):
        print(path)
        
    with open("326023_3.segy", "rb") as ebcdic:
        ascii_txt = codecs.decode(ebcdic.read(80*40), "cp500")
        print(ascii_txt[(line - 1)*80 + position - 1 : (line - 1)*80 + position -1 + length].strip(' '))