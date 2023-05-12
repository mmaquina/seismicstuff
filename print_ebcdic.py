#!/usr/bin/python3

import codecs
import sys 


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Prints ebcdic header from segy file.")
        print("Usage:  ./print_ebcdic filename.sgy")
        exit()

    with open(sys.argv[1], "rb") as ebcdic:
        ascii_txt = codecs.decode(ebcdic.read(80*40), "cp500")
        out = ''
        for i in range(40):
            out += ascii_txt[i*80 : i*80 + 80] + '\n'
        
        print(out)