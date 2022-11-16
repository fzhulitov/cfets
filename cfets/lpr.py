from io import StringIO

import pandas as pd
from cfets import request_data


def get_lpr_1y() -> pd.Series:
    df = prepare_data()
    return df.loc[:, 'lpr1y'].dropna()


def get_lpr_5y() -> pd.Series:
    df = prepare_data()
    return df.loc[:, 'lpr5y'].dropna()


def prepare_data() -> pd.DataFrame:
    d = request_data.get_data_frame()
    df = pd.read_csv(StringIO(d),
                     usecols=[0, 6, 7],
                     names=['date', 'lpr1y', 'lpr5y'],
                     dtype={'lpr1y': float, 'lpr5y': float},
                     parse_dates=[0])
    df.set_index('date', inplace=True)
    df.index = df.index.to_period(freq='M')
    return df/100
