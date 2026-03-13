# def convert_number(x):
#
#     if x == '1':
#         print(int(input()))
#     elif x == '2':
#         print(bin(int(input()))[2:])
#     elif x == '3':
#         print(hex(int(input()))[2:].upper())
#
# convert_number(10)



print(bin(10))
print(hex(10))
print(int(str("11111111"), 2))


def type_convert(x,y,z):
    x = bin(x)
    y = hex(y)
    z = int(str(z), 2)
    print(x, y, z)
    return x, y , z

# type_convert(10,10,11111111)

def type_convert(x, y, z):
    return bin(x), hex(y), bin(z)

def test_type_con():
    assert type_convert(15, 16, 1111) == ('0b1111', '0x10', '0b10001010111')

def test_type_con_additional():
        assert type_convert(8, 255, 1024) == ('0b1000', '0xff', '0b10000000000')
        assert type_convert(0, 0, 0) == ('0b0', '0x0', '0b0')
        assert type_convert(1, 10, 255) == ('0b1', '0xa', '0b11111111')
        assert type_convert(100, 256, 1023) == ('0b1100100', '0x100', '0b1111111111')
