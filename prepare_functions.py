import re

IN_OUT_FILE = 'euler.py'

with open(IN_OUT_FILE, 'r') as f:
    lines = f.readlines()

with open(IN_OUT_FILE, 'w') as f:
    last_no = 1
    problem_no_re = re.compile('def euler([0-9]+)')
    for l in lines:
        m = problem_no_re.match(l)
        if m:
            no = int(m.groups()[0])
            for n in range(last_no, no):
                f.write('def euler%d_():\n' % n)
                f.write('    """Solution for problem %d."""\n' % n)
                f.write('    pass\n\n\n')
            last_no = no + 1
        f.write(l)
