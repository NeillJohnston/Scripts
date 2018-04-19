from math import cosh, sinh


"""
catenary_slabs.py

This is the predecessor to catenary.py (although git doesn't show it that way).
Generates a catenary plan that shows the necessary height to the nearest half for each block along x.
Made for Minecraft because I wanted to have cute hanging bridges made of slabs in my world. Not really useful for 
anything else.

Largely uses the exact same math as catenary.py but the code itself isn't as clean because it was my first go.
"""


catenary = lambda x, a: a*cosh(x/a) - a
# Width of catenary
w = int(input('w: '))
# Desired height
h = int(input('h: '))

# (Continuous) binary search with tolerance break to find right a value for given h
a = 0
upper = 1000000
lower = 0
tolerance = 1e-6

while lower < upper:
    a = lower + (upper-lower)/2
    test = catenary((w-1)/2, a)
    # If we're under tolerance threshold, break
    if abs(h - test) < tolerance:
        break
    
    # If test is too small, then a is too large
    if test < h:
        upper = a
    elif test > h:
        lower = a
    else:
        break

# Print the catenary
print()
for i in range(w):
    x = i - (w-1)/2
    y = catenary(x, a)
    # Math magic to round catenary to the nearest 0.5
    print('{0}\t{1:}'.format(i, round(2*y) / 2))

input('')
