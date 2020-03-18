#Se repite una letra en un string - Programa con tuplas


def find_first_no_repeat_char(char_sequence):
    for char in char_sequence:
        if char_sequence.count(char) == 1:
            return char
    return'_'

char_sequence = input('Ingrese sus variables')
print(char_sequence)
print(find_first_no_repeat_char(char_sequence))    