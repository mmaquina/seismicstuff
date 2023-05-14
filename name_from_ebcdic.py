#!/usr/bin/python3

import codecs
import sys 
import os


includes_subdirs = 'n'

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Renames segy files using a specific location in the EBCDIC header, where the name of the line is. Line number and position where the name is in ebcdic header must be specified.")
        print("Usage:  ./name_from_ebcdic line(1 is the top line) position(1 is the leftomst character position) [length(characters)]")
        print("Example:  ./name_from_ebcdic 5 45 7")
        print("Example:  ./name_from_ebcdic 5 45")
        print("In the latter example length is from position to the end of the line.")
        exit()
    else:
        includes_subdirs = input("Do you want to include subdirectories? [Y/n]:")
        line = int(sys.argv[1])
        position = int(sys.argv[2])
        length = 80 - position + 1
        if len(sys.argv) == 4:
            length = int(sys.argv[3])

    if includes_subdirs.lower() == 'y':
        for path in os.walk('.'):
            print(path)
    else:
        for path in os.listdir():
            print(path)
        
    with open("326023_3.segy", "rb") as ebcdic:
        ascii_txt = codecs.decode(ebcdic.read(80*40), "cp500")
        print(ascii_txt[(line - 1)*80 + position - 1 : (line - 1)*80 + position -1 + length].strip(' '))