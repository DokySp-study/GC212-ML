
from scipy import stats
import pandas as pd
import numpy as np

table = [
    [45, 34],
    [38, 22],
    [52, 15],
    [48, 27],
    [25, 37],
    [39, 41],
    [51, 24],
    [46, 19],
    [55, 26],
    [46, 36],
]
df = pd.DataFrame(
    table, 
    columns=["Older Adults", "Younger Adults"],
)

print("\nTable data")
print(df)


N = len(df)
a = df["Older Adults"].to_numpy()
b = df["Younger Adults"].to_numpy()

var_a = a.var(ddof=1)
var_b = b.var(ddof=1)


# Independent sample t test
t = (a.mean() - b.mean()) / np.sqrt( var_a/N + var_b/N )

# For independent sample t test
df = 2 * N - 2 

p = 1 - stats.t.cdf(t, df=df)

print("\nT-score: %.3f" %t)
print("Degree of Freedom: %d" %df)
print("p: %.4f" %p)
print("")

if t > p:
    print("Reject H0 <Dependent>")
else:
    print("Fail to reject H0 <Independent>")