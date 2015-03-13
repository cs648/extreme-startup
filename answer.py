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


def answer(q):
    if q == 'what is your name':
        return 'HungoverDeltas'
    match = re.search(r'.*what is the sum of (\\d+) and (\\d+)', q)
    if match:
        return int(match.group(0)+match.group(1))
    if q.startswith('which of the following is earliest'):
        return min(q.split(':')[1].split(','), key=timesort)

