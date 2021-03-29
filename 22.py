def f22(x):
    e = x & 0xf0000000
    d = x & 0x0e000000
    c = x & 0x01fffe00
    b = x & 0x000001c0
    a = x & 0x0000003f
    return e >> 16 | d >> 16 | c << 7 | b >> 6 | a << 3
