[![Python](https://img.shields.io/badge/python-v3-brightgreen.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# cfets: Python interface for China Foreign Exchange Trade System (CFETS) API

Known CFETS data code (series) for API request:  

- LprChrtCSV - Lone Prime Rates (LPR)
- RmbIdxHis - RMB Index
- ShiborPriHis - SHIBOR history

### Functions in _cfets_ package
Loan Prime Rate time series:
 - get_lpr_1y() - one-year loan prime rate (LPR)
 - get_lpr_5y() - five-years loan prime rate (LPR)
