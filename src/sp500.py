import json
import pandas as pd


def get_sp500_company_cik():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    sp500_table = pd.read_html(url)[0]
    sp500_company_cik = {ticker: cik for ticker,
                         cik in sp500_table[['Symbol', 'CIK']].values.tolist()}
    return sp500_company_cik


def save_sp500_company_cik_json(output_file_path):
    sp500_company_cik = get_sp500_company_cik()
    with open(output_file_path, 'w') as fp:
        json.dump(sp500_company_cik, fp, indent=4)
    return sp500_company_cik
