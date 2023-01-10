import pandas as pd
import cfets.lpr

sd = pd.Timestamp(2022, 1, 1)
print(sd)

s = cfets.get_lpr_5y(start_date=sd)
print(s)
s = cfets.get_lpr_1y(start_date=sd)
print(s)
