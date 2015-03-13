match = re.search(r'.*what is the sum of (\\d+) and (\\d+)', s)
def answer(q):
    if q == 'what is your name':
        return 'HungoverDeltas'
    if match:
        return int(match.group(0)+match.group(1))

