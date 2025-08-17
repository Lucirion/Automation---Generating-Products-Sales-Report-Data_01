# Project Description

This Python project tries to emulate a real life scenario inside a working environment. It generates randomized sales data into one file and then processes it into a clean new report file. It's designed for testing data workflows, Excel output, and basic analytics.

## Features
- Randomized stock and sales generation.
- Excel export of raw and processed data.
- Revenue calculation and remaining stock tracking.
- Already packed .exe files to allow you to run them-
  directly to see the results. Can also be assigned-
  to be run using a task scheduler to generate the-
  raw data and sales data once a day or so for testing.

## Folder Structure
project_name/
    data/
        raw_data/
        sales_data/
    src/
        .py files
    tests/
        leftover test file
    
### How to use
Run the generate_data.py to generate a raw sales data excel file.
Run process_data.py to read the outputted excel file to generate-
a new sales_report file containing the calculated results of-
the revenue.

The .exe files are the packed files and can be run outside of an IDE.

