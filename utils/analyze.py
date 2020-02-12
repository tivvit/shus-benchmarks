import json
import csv
import os

from glob import glob


def get_name(f):
    return f.split('/')[-1].replace(".json", "")


if __name__ == '__main__':
    files = glob("reports/0/*")
    r = {get_name(f): {"name": get_name(f)} for f in files}
    for t in range(3):
        for f in files:
            fn = f.split('/')[-1]
            d = json.load(open(os.path.join("reports", str(t), fn), "r"))
            r[get_name(f)][str(t + 1)] = d["requests_sec"]

    with open('results.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', '1', '2', '3']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in r.values():
            writer.writerow(i)
