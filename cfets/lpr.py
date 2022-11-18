from io import StringIO

import pandas as pd
from cfets import request_data

lpr_code = "LprChrtCSV"


def get_lpr_1y(start_date: str = "2013-10-01", end_date: str = None) -> pd.Series:
    d = request_data.get_data_frame(
        code=lpr_code, start_date=start_date, end_date=end_date
    )
    df = prepare_data(d)
    return df.loc[:, "lpr1y"].dropna()


def get_lpr_5y(start_date: str = "2013-10-01", end_date: str = None) -> pd.Series:
    d = request_data.get_data_frame(
        code=lpr_code, start_date=start_date, end_date=end_date
    )
    df = prepare_data(d)
    return df.loc[:, "lpr5y"].dropna()


def prepare_data(d: dict) -> pd.DataFrame:
    df = pd.read_csv(
        StringIO(d),
        usecols=[0, 6, 7],
        names=["date", "lpr1y", "lpr5y"],
        dtype={"lpr1y": float, "lpr5y": float},
        parse_dates=[0],
    )
    df.set_index("date", inplace=True)
    df.index = df.index.to_period(freq="M")
    df.sort_index(ascending=False, inplace=True)
    return df
