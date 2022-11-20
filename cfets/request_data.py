import json
import requests


URL = "https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/"


def get_data_frame(code: str = 'LprChrtCSV', start_date: str = '2013-10-01', end_date: str = None) -> dict:
    request_url = URL + code
    user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Chrome/89.0.4389.72 Safari/537.36'}

    params = {"startDate": start_date, "endDate": end_date}
    r = requests.get(request_url, headers=user_agent, params=params)
    if r.status_code != requests.codes.ok:
        raise Exception(r.status_code, r.reason, request_url)
    jresp = json.loads(r.text)
    return jresp["data"]["csv"]
