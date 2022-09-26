import pandas as pd
from cfets import request_data

def lpr_1y ()->pd.Series:
    df = request_data.get_data_frame()
    s1 = pd.Series(dtype="float")
    for row in df.itertuples():
        value = row.Y1
        date = pd.to_datetime(row.date)
        s1[date] = value
    s1.index = s1.index.to_period("M")
    return s1

def lpr_5y ()->pd.Series:
    df = request_data.get_data_frame()
    s5 = pd.Series(dtype="float")
    for row in df.itertuples():
        value = row.Y5
        date = pd.to_datetime(row.date)
        s5[date] = value
    s5.index = s5.index.to_period("M")
    s5 = s5.dropna()
    return s5


