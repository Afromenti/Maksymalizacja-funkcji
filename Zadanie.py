import random

def encode_binary(x, numOfBits):
    scaled_x = x / 10.0
    r = 10 - num_of_bits
    
    binary_string = format(int(scaled_x * 2**numOfBits), '010b')
    if r:
        return binary_string[r:]

    return binary_string

def decode_binary(binary_string, numOfBits):
    decimal_value = int(binary_string, 2)
    scaled_value = decimal_value / 2**numOfBits * 10.0

    return scaled_value

num_of_bits = 8
x = 6.5
encoded_x = encode_binary(x,num_of_bits)
print("Zakodowany x:", encoded_x)

decoded_x = decode_binary(encoded_x, num_of_bits)
print("Odkodowany x:", float(decoded_x))
