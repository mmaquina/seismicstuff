#!/usr/bin/python3

import codecs
import sys 


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Writes ebcdic header of segy file (from ascii file).")
        print("Usage:  ./write_ebcdic asciifile.txt segyfile.sgy")
        exit()

    with open(sys.argv[1], "r") as ascii:
        ascii_no_newline = ''
        for i in range(1, 41):
            line = ascii.readline()
            if line:
                if len(line) > 80:
                    line = line[:80]
                line = line.strip('\n').ljust(80)
                ascii_no_newline  += line
            else:
                break

        ascii_no_newline.ljust(80 * 40)

        ebcdic = codecs.encode(ascii_no_newline, "cp500")

        with open(sys.argv[2], 'r+b') as fout:
            fout.seek(0)
            fout.write(ebcdic)
