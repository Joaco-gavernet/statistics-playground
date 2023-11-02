from statistics import *
from math import *
from itertools import filterfalse

data = [20.7, float("NaN"), 19.2, 18.3, float("NaN"), 14.4]
print("data: ", sorted(data))

print("median (random value) = ", median(data))

sum(map(isnan, data))

clean = list(filterfalse(isnan, data))
clean

print("clean: ", sorted(clean))

print("median = ", median(clean))
