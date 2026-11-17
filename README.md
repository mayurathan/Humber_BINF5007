# Assignment 2: Descriptive Statistics in Python

This project reads tab-delimited data files and calculates descriptive statistics for the numeric values in a selected column. The command-line interface is `CLI.py`; the statistics and file-loading functions are provided by `stats_in_python.py`.

## Features

- Choose one of the three included data files from a menu.
- Select a column using a zero-based column number.
- Store valid numeric values as floats and ignore non-numeric entries and `NaN` values.
- Report an error when the selected column has no valid numbers or the column index is out of range.
- Calculate the count, valid number count, average, maximum, minimum, variance, standard deviation, and median.

## Requirements

- Python 3
- The assignment restricts the statistics program to Python's `sys` and `math` modules.
- `pytest` is needed only to run the provided tests.

Install pytest if needed:

```bash
python -m pip install pytest
```

## Run the program

From the repository root, start the menu-driven command-line interface:

```bash
python CLI.py
```

Choose a data file when prompted, then enter the column number to analyze. Column numbers start at `0`, so column `3` is the fourth column. The files are expected in the `./files` directory:

- `data_file.txt`
- `data_file2.txt`
- `data_file3.txt`

## Run the tests

From the repository root, run:

```bash
pytest stats_test.py
```

## Statistics

The program reports:

- **Count:** number of values/rows encountered in the selected column.
- **ValidNum:** number of numeric, non-`NaN` values used in the calculations.
- **Average:** arithmetic mean.
- **Maximum / Minimum:** largest and smallest valid values.
- **Variance:** sample variance, using the assignment's denominator of `n - 1`.
- **Std Dev:** square root of the variance.
- **Median:** middle value after sorting; for an even number of values, the average of the two middle values.