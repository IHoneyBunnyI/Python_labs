from struct import unpack


D_SIZE = 1 + 1 + 2 + 4 + 1 * 4 + 2
def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = unpack("bbHIbbbbH", d_bytes);
    return {'D1' : d_parsed[0], 
            'D2' : d_parsed[1],

C_SIZE = 1 + 2 + 4
def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_paesed = unpack("bHI", c_bytes)
    c2_bytes = byte_string[c_paesed[2]:c_paesed[2] + c_paesed[1]);
    c2_parsed = unpack("I" * c_paesed[1], c2_bytes);
    return {'C1' : c_paesed[0],
            'C2' : list(c2_parsed)}



B_SIZE = 1 * 5 + 8 + 8 + 4
def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = unpack("cccccQqI", b_bytes)
    return {'B1' : list(b_parsed[:5],
            'B2' : b_parsed[5],
            'B3' : b_parsed[6],
            'B4' : parse_c(b_parsed[7], byte_string)}



A_SIZE = 1 + 2 + B_SIZE + 2 + 2
def parse_a(offset, byte_string):
    a12_bytes = byte_string[offset:offset + 3]
    a12_parsed = unpack("BH", a12_bytes);
    a3_parsed = parse_b(offset + 3, byte_string);
    a4_bytes = byte_string[3 + B_SIZE : 3 + B_SIZE + 2 + 2]
    a4_parsed = unpack("HH", a4_bytes); #тут не правильно
    a4_list = [parse_d(addr, byte_string) for addr in a4_parsed]
    return {'A1' : a12_parsed[0],
            'A2' : a12_parsed[1],
            'A3' : a3_parsed,
            'A4' : a4_parsed}





def 31():
