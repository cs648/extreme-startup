import re
from collections import OrderedDict
from time import smallest_time

def largest(q):
    return str(max([int(i.strip()) for i in q.split(',')]))

def answer(q):
    if q == 'what is your name':
        return 'HungoverDeltas'
    match = re.search(r'.*what is the sum of (\\d+) and (\\d+)', q)
    if match:
        return int(match.group(0)+match.group(1))
    if q.startswith('which of the following is earliest'):
        return smallest_time(q)
    return ""

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return str(a)

def multiply(a,b):
    intA = int(a)
    intB = int(b)
    return str(intA * intB)


def write_roman(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(number):
        num = int(number)
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])
