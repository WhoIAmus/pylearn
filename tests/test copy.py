def roman_to_int(roman):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0

    for numeral in reversed(roman):
        value = roman_dict[numeral]
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result

def int_to_roman(integer):
    roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L',
                  90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    result = ""

    for value, numeral in sorted(roman_dict.items(), key=lambda x: x[0], reverse=True):
        while integer >= value:
            result += numeral
            integer -= value

    return result

def add_roman_numerals(roman1, roman2):
    int_sum = roman_to_int(roman1) + roman_to_int(roman2)
    return int_to_roman(int_sum)

# Приклад використання:
input_str = input("Введіть два числа в римській системі, розділені знаком +: ")
numbers = input_str.split('+')
result = add_roman_numerals(numbers[0].strip(), numbers[1].strip())
print("Сума чисел: " + result)