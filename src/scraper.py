import requests
import pandas as pd
from bs4 import BeautifulSoup
from tqdm import tqdm

# companies table headings in www.sec.gov and company ticker and cik
HEADINGS = ['Filings', 'Format', 'Description', 'Filing Date', 'File/Film Number', 'ticker', 'cik']


def get_soup(url: str, headers):
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    return soup


def get_sec_gov_url_from_cik(cik: int):
    return f'https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={cik}&type=10-&dateb=&owner=exclude&count=100'


def parse_companies_information(company_cik, headers):
    all_rows = []
    for ticker, cik in tqdm(company_cik.items()):
        url = get_sec_gov_url_from_cik(cik)
        soup = get_soup(url, headers)
        table = soup.find_all("table", attrs={"class": "tableFile2"})[0]
        # the head will form our column names
        body = table.find_all("tr")
        # Head values (Column names) are the first items of the body list
        body_rows = body[1:]  # All other items becomes the rest of the rows
        for table_row in body_rows:
            row = [row_item.text.strip()
                   for row_item in table_row.find_all("td")]
            row += [ticker, cik]
            all_rows.append(row)
    return all_rows


def parse_save_companies_information(output_file_path, company_cik, headers):
    all_rows = parse_companies_information(company_cik, headers)
    df = pd.DataFrame(data=all_rows, columns=HEADINGS)
    df['Filing Date'] = pd.to_datetime(
        df['Filing Date'].values, format='%Y-%m-%d')
    df.to_csv(output_file_path, index=False)



