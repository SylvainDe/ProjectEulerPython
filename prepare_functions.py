import re

with open('euler.py', 'r') as f:
    lines = f.readlines()

last_no = 1
problem_no_re = re.compile('def euler([0-9]+)')
for l in lines:
    m = problem_no_re.match(l)
    if m:
        no = int(m.groups()[0])
        for n in range(last_no, no):
            print('def euler%d_():' % n)
            print('    """Solution for problem %d."""' % n)
            print('    pass')
            print()
            print()
        last_no = no + 1
    print(l, end='')
