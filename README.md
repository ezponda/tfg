TFG
==============================

To install python requirements:
```bash
pip install -r requirements.txt
```

For extracting companies information in [input cik data](#input-data-format) stored in input/file/path 
and saving it in output/file/path:


```bash
python main.py --input_cik_file_path input/cik/file/path --output_file_path output/file/path
```

For example:

```bash
python main.py --input_cik_file_path ./data/sp500_companies_cik.json --output_file_path ./data/extraction.csv
```


Input Data Format
------------

Input file example in `./data/sp500_companies_cik.json`.

It has been generated with function `save_sp500_company_cik_json` in `/src/sp500.py`

```python
from src.sp500 import save_sp500_company_cik_json
save_sp500_company_cik_json('./data/sp500_companies_cik.json')
```
