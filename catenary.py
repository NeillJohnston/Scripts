from math import cosh, sinh


"""
catenary.py

Generates the block layout of a catenary (the shape of a hanging chain or a perfect arch).
Made this mainly for Minecraft builds but also for fun.

The really interesting bit is the binary search in the middle. The formula for a catenary is
    y = a*cosh(x/a), where a is a constant
which doesn't give much flexibility if you want to solve for a, which is necessary if you want a catenary of specified
height. So instead of doing some difficult math with a function I've never learned before (seriously, never run into the 
hyperbolic cosine until now) we take advantage of the fact that holding x constant and making a the variable results in 
a continuously decreasing function. From here, binary searching is enough to find a value for a that is as accurate as 
you want it to be. Since binary search is O(log(n)), you can start a at an arbitrarily high value (such as 1x10^6) and 
whittle this down to accuracy within 1x10^-8 in less than 50 loops - nearly instantaneously.
"""


print('Catenary plan generator')
w = int(input('width: '))
h = int(input('height (negative for arches): '))
print()

# Make an arch if h is negative
arching = False
if h < 0:
    arching = True
    h = -h

# Catenary function, modified to have vertex at (0, 0)
fcatenary = lambda x, a: a*(cosh(x/a) - 1)

# Continuous binary search with tolerance to find a
a = 0
upper = 1e6         # Upper starts at an arbitrarily high value
lower = 0           # Lower starts at 0
tolerance = 1e-8    # Tolerance is an arbitrarily low value

while lower < upper:
    a = lower + (upper - lower) / 2
    test = fcatenary(w/2, a)
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
    # Divide x into many segments to avoid breaks in the catenary
    for dx in range(1, h):
        xi = x + dx/h - w/2
        y = h - fcatenary(xi, a) if not arching else fcatenary(xi, a)
        try:
            catenary[int(y)][int(x)] = True
        except IndexError:
            # I really don't know how it makes it to this statement, but it does rarely
            # For example a if w=27 and h=10
            continue

# Print catenary + extra info
b = sum(row.count(True) for row in catenary)    # Block count
s = 2 * a*sinh((w/2)/a)                         # Precise arc length

for row in catenary:
    print(' '.join('O' if cell else '.' for cell in row))

print('\na=%f, using %d blocks (arc length=%f)' % (a, b, s))
input('Press enter to exit')
