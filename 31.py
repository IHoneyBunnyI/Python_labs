from struct import unpack


D_SIZE = 1 + 1 + 2 + 4 + 1 * 4 + 2
def parse_d(offset, byte_string):
    d_bytes = byte_string[offset:offset + D_SIZE]
    d_parsed = unpack("bbHIbbbbH", d_bytes);
    d3_bytes = byte_string[d_parsed[3] : d_parsed[3] + d_parsed[4]] 
    d3_parsed = unpack('d' * d_parsed[4], e4_bytes);
    return {'D1' : d_parsed[0], 
            'D2' : d_parsed[1],
            'D3' : d3_parsed,
            'D4' : list(d_parsed[4:8]),
            'D5' : d_parsed[8]}


C_SIZE = 1 + 2 + 4
def parse_c(offset, byte_string):
    c_bytes = byte_string[offset:offset + C_SIZE]
    c_paesed = unpack("bHI", c_bytes)
    c2_bytes = byte_string[c_paesed[2]:c_paesed[2] + c_paesed[1]];
    c2_parsed = unpack("I" * c_paesed[1], c2_bytes);
    return {'C1' : c_paesed[0],
            'C2' : list(c2_parsed)}



B_SIZE = 1 * 5 + 8 + 8 + 4
def parse_b(offset, byte_string):
    b_bytes = byte_string[offset:offset + B_SIZE]
    b_parsed = unpack("cccccQqI", b_bytes)
    return {'B1' : list(b_parsed[:5]),
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





def f31(byte_string):
    parse_a(5, byte_string)

print(f31(b'4MQXWP.lebpqy{\xe6\xf3j\xc5\x80P5?U\xd1\r[\x05\xbbY-\x00\x00\x00\x02\x00x'
b'\x00\xae[\x82\xbeXV7\xbe\r\x02\x00%\x00\x00\x000\x0e+)v\xc7\xe8\xbf'
b'\xe0\n\x1dd\xaf\x9e\xe7\xbfT\n\xac\xb4`\xa6\xee?4\xf5\x03\x004\x00\x00\x00'
b'-\xe8\xdf\xe0#%\xc0\xa8;\x1b6r\xa5\xbf\xe2bKAu[\xe0?\x9f\xc0\x02\x00Z\x00'
b'\x00\x00\xf1u\xf3\x0c2)L\x00\x00\x00j\x00\x00\x00'))
