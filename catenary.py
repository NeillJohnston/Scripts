from math import cosh, sinh

print('Catenary plan generator')
w = int(input('width: '))
h = int(input('height: '))
arching = False
if h < 0:
    arching = True
    h = -h
fcatenary = lambda x, a: a*cosh(x/a) - a

# Continuous binary search to find a
a = 0
upper = 1000000
lower = 0
tolerance = 1e-8

while lower < upper:
    a = lower + (upper - lower) / 2
    # Choose x to be the right-most side of the catenary
    x = w/2
    test = fcatenary(x, a)
    # If we're under tolerance, break
    if abs(h - test) < tolerance:
        break
    # If test is too low, then a is too high
    if test < h:
        upper = a
    elif test > h:
        lower = a
    else:
        break

# Catenary should fit into a w*h box
catenary = [[False for x in range(w)] for y in range(h)]
for x in range(w):
    # Divide x into many segments
    for dx in range(1, h):
        x_ = x + dx/h - w/2
        y = h - fcatenary(x_, a) if not arching else fcatenary(x_, a)
        try:
            catenary[int(y)][int(x)] = True
        except:
            continue

# Print catenary + extra info
print()
for row in catenary:
    print(' '.join('O' if cell else '.' for cell in row))
b = sum(row.count(True) for row in catenary)
s = 2 * a*sinh((w/2)/a)
print('\na=%f, using %d blocks (arc length=%f)' % (a, b, s))
input('Press enter to exit')
