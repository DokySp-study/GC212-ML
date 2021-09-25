import numpy as np
import pandas as pd
import math


b1 = 1
b2 = 4
s1 = 2
s2 = 3

gini1 = 0
gini2 = 0

if b1+b2 != 0:
    gini1 = 1 - (b1/(b1+b2))*(b1/(b1+b2)) - (b2/(b1+b2))*(b2/(b1+b2))
if s1+s2 != 0:
    gini2 = 1 - (s1/(s1+s2))*(s1/(s1+s2)) - (s2/(s1+s2))*(s2/(s1+s2))

print(gini1)
print(gini2)

w = s1+s2+b1+b2

gini3 = ((b1+b2)/w)*gini1 + ((s1+s2)/w)*gini2

print(gini3)