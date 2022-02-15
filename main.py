import argparse
import json
from src.scraper import parse_save_companies_information


def main(args):
    with open(args.input_cik_file_path) as json_file:
        company_cik = json.load(json_file)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'
    }
    parse_save_companies_information(args.output_file_path, company_cik, headers)
    return


# python main.py --input_cik_file_path ./data/sp500_companies_cik.json --output_file_path .data/out.csv
if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(
            description="scraper"
        )
        parser.add_argument('--input_cik_file_path', dest='input_cik_file_path',
                            type=str, help='Input cik json file, for example: ./data/sp500_companies_cik.json')
        parser.add_argument('--output_file_path', dest='output_file_path',
                            type=str, help='Output csv file for cik information ')
        args = parser.parse_args()
        main(args)

    except RuntimeError as e:
        raise
