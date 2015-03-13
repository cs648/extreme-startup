import re
from collections import OrderedDict

def timesort(a, b):
    na = 0
    nb = 0
    if a.endswith('pm'):
        na += 12
    if b.endswith('pm'):
        nb += 12

    a = int(a[:-2])+na
    b = int(b[:-2])+nb

    return cmp(a, b)

def largest(q):
    return str(max([int(i.strip()) for i in q.split(',')]))

def answer(q):
    if q == 'what is your name':
        return 'HungoverDeltas'
    match = re.search(r'.*what is the sum of (\\d+) and (\\d+)', q)
    if match:
        return int(match.group(0)+match.group(1))
    if q.startswith('which of the following is earliest'):
        return min(q.split(':')[1].split(','), key=timesort)
    return ""

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

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