import csv
import sys

# Read PSV file with csv
def read_csv(fname: str) -> list[tuple]:
    with open(fname) as file:
        data = [row for row in csv.reader(file, delimiter="|")]
    return data

# Read PSV file with tabulate
from tabulate import tabulate
def read_tabulate(fname: str) -> list[tuple]:
    with open(fname) as file:
        data = [row for row in csv.reader(file, delimiter="|")]
    return data

# Read PSV file with Pandas
import pandas
def read_pandas(fname: str) -> pandas.DataFrame:
    data = pandas.read_csv(fname, sep="|")
    return data

if __name__ == "__main__":
    data = read_csv(sys.argv[1])
    for row in data[0:5]:
        print(row)

    data = read_tabulate(sys.argv[1])
    print(tabulate(data[0:5]))

    data = read_pandas(sys.argv[1])
    print(data.head(5))

