import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt



def calc(p, q, tn):

    tn = 10-hn
    a = p
    b = 1-p

    result = 1

    for i in range(0, hn):
        result *= a

    for i in range(0, tn):
        result *= b

    psa = result
    # print("P(S|A)")
    # print(format(result, ".10f"))


    a = q
    b = 1-q
    result = 1

    for i in range(0, hn):
        result *= a

    for i in range(0, tn):
        result *= b

    psb = result
    # print("P(S|B)")
    # print(format(result, ".10f"))


    # print("")
    # print("P(A|S)")
    pas = (psa * 0.5) / ( psa * 0.5 + psb * 0.5 )
    # print(format(pas, ".10f"))

    # print("P(B|S)")
    pbs = (psb * 0.5) / ( psa * 0.5 + psb * 0.5 )
    # print(format(pbs, ".10f"))

    return psa, psb, pas, pbs



p = 0.59
q = 0.85

ah = 0
bh = 0
at = 0
bt = 0





hn = 5
tn = 10 - hn

_, _, pas, pbs = calc(p, q, hn)
print("")
print("Expecting A Head and Tail")
ah += pas * hn
print(format(pas * hn, ".5f"))
at += pas * tn
print(format(pas * tn, ".5f"))

print("Expecting B Head and Tail")
bh += pbs * hn
print(format(pbs * hn, ".5f"))
bt += pbs * tn
print(format(pbs * tn, ".5f"))


hn = 9
tn = 10 - hn
_, _, pas, pbs = calc(p, q, hn)
print("")
print("Expecting A Head and Tail")
ah += pas * hn
print(format(pas * hn, ".5f"))
at += pas * tn
print(format(pas * tn, ".5f"))

print("Expecting B Head and Tail")
bh += pbs * hn
print(format(pbs * hn, ".5f"))
bt += pbs * tn
print(format(pbs * tn, ".5f"))



hn = 8
tn = 10 - hn
_, _, pas, pbs = calc(p, q, hn)
print("")
print("Expecting A Head and Tail")
ah += pas * hn
print(format(pas * hn, ".5f"))
at += pas * tn
print(format(pas * tn, ".5f"))

print("Expecting B Head and Tail")
bh += pbs * hn
print(format(pbs * hn, ".5f"))
bt += pbs * tn
print(format(pbs * tn, ".5f"))







print("")
print("Coin A Head: ", format(ah, ".5f"))
print("Coin A Head: ", format(at, ".5f"))
print("Coin B Tail: ", format(bh, ".5f"))
print("Coin B Tail: ", format(bt, ".5f"))

print("")
print("p: ", format(ah/(ah+at), ".5f"))
print("q: ", format(bh/(bh+bt), ".5f"))