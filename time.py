def convert_time(t):
    n = 0
    if t.endswith('pm'):
        n += 12

    return int(t[:-2])+n

def timesort(a, b):
    return cmp(convert_time(a), convert_time(b))

def smallest_time(s):
    return min(s.split(':')[1].split(','), key=timesort)
