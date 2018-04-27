"""HTML shenanigans.

Format:
!x:word1|word2
"""


s = input('?:')
ts = []

for t in s.split(' '):
    if t[0] == '!':
        x, ws = t.split(':')
        x = float(x[1:])
        w0, w1 = ws.split('|')
        # Format
        ts.append('<span class="wordswap" word1="%s" word2="%s" threshold="%f"></span>' % (w0, w1, x))
    else:
        ts.append(t)

print(' '.join(ts))
