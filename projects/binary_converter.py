# binary_converter.py
# Convert decimal to binary and back

# Ask user for decimal number
num = int(input('Enter decimal number:'))

# Convert decimal number to binary
binary = bin(num)[2:] # removes the '0b' string from binary number
print(f'Binary representation: {binary}')

# Convert back to decimal
decimal_back = int(binary, 2)
print(f'Decimal representation: {decimal_back}')