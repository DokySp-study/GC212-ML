
from scipy.stats import chi2_contingency
from scipy.stats import chi2
import pandas as pd

table = [
    [209, 280],
    [225, 248]
]
df = pd.DataFrame(
    table, 
    columns=["Beach", "Cruise"],
    index=["Male", "Female"]
)

print("\nTable data")
print(df)



calculated, p, df, expected = chi2_contingency(table)

print("\nDegree of Freedom: %d" %df)
print("Expected:")
print(expected)
print("")



prob = 0.95
alpha_value = 1 - prob
critical = chi2.ppf(alpha_value, df)

print('prob: %.3f\ncritical value: %.3f\ncalculated value=%.3f' %(prob, critical, calculated))
print('significance: %.3f\np: %.3f' %(alpha_value, p))
print("")



if alpha_value > p:
    print("Reject H0 <Dependent>")
else:
    print("Fail to reject H0 <Independent>")






# columns=["Republican", "Democrat", "Independent"],
    # [200, 150, 50],
    # [250, 300, 50]