import json
import csv
import os

from glob import glob
from typing import Dict, Iterable, Union

NUMBER_OF_TESTS = 3


def get_name(f: str) -> str:
    return f.split('/')[-1].replace(".json", "")


def get_filenames(files: Iterable[str]) -> Dict[str, Dict[str, str]]:
    return {get_name(f): {"name": get_name(f)} for f in files}


def load_results() -> Dict[str, Dict[str, Union[str, float]]]:
    files = glob("reports/0/*")
    r = get_filenames(files)
    for t in range(NUMBER_OF_TESTS):
        for f in files:
            fn = f.split('/')[-1]
            d = json.load(open(os.path.join("reports", str(t), fn), "r"))
            r[get_name(f)][str(t + 1)] = d["requests_sec"]
    return r


def store_results(results: Dict[str, Dict[str, Union[str, float]]]):
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', '1', '2', '3'])

        writer.writeheader()
        i: Dict[str, Union[str, float]]
        for i in results.values():
            writer.writerow(i)


def main():
    results = load_results()
    store_results(results)


if __name__ == '__main__':
    main()
