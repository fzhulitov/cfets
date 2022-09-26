import pandas as pd
import json
import requests
from io import StringIO


def get_data_frame() -> pd.DataFrame:

    abc = requests.get("https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/LprChrtCSV?startDate=2013-10-01")
    jresp = json.loads(abc.text)
    dat = jresp["data"]
    cs = dat["csv"]
    col = dat["columns"]
    str_name = ""
    for c in col:
        if c == '1Y':
            c = 'Y1'
        if c == '5Y':
            c = 'Y5'
        str_name = str_name+c+','
    str_name = str_name[:-1]
    str_name = str_name+cs
    csfile = StringIO(str_name)
    df = pd.read_csv(csfile)
    df = df.filter(items=['date', 'Y1', 'Y5'])
    return df
