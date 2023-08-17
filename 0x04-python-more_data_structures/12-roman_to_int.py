#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    s = roman_string
    for i in range(len(s)):
        if i < len(s) - 1 and rom_n[s[i]] < rom_n[s[i + 1]]:
            sum -= rom_n[s[i]]
        else:
            sum += rom_n[s[i]]
    return sum
