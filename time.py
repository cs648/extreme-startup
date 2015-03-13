def convert_time(t):
    n = 0
    try:
        return int(t)
    except ValueError:
        pass
    if t.endswith('pm'):
        n += 1200
    if '.' in t:
        t = t.split('.')
        return int(t[0])*100+int(t[1])

    return int(t[:-2])*100+n

def timesort(a, b):
    return cmp(convert_time(a), convert_time(b))

def smallest_time(s):
    return min(s.split(':')[1].split(','), key=timesort)
