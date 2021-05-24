from struct import unpack

D_SIZE = 1 + 1 + 2 + 4 + 1 * 4 + 2
C_SIZE = 1 + 2 + 4
B_SIZE = 1 * 5 + 8 + 8 + 4
A_SIZE = 1 + 2 + B_SIZE + 2 + 2 + 4

def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = unpack("bbHIbbbbH", d_bytes);
    return {'D1' : d_parsed[0], 
            'D2' : d_parsed[1], 
            'D3' : d_parsed[0], 
            'D4' : d_parsed[0], 
            'D5' : d_parsed[0], 

def 31():
