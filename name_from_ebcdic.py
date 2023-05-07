import codecs

with open("326023_3.segy", "rb") as ebcdic:
    ascii_txt = codecs.decode(ebcdic.read(400), "cp500")
    print(ascii_txt)