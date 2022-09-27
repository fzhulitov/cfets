import json
import requests


URL = "https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/"


def get_data_frame(
    code: str = "LprChrtCSV", start_date: str = "2013-10-01", end_date: str = None
) -> dict:
    request_url = URL + code
    params = {"startDate": start_date, "endDate": end_date}
    r = requests.get(request_url, params=params)
    if r.status_code != requests.codes.ok:
        raise Exception(r.status_code, r.reason, request_url)
    jresp = json.loads(r.text)
    return jresp["data"]["csv"]
