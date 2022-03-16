import csv
import json
import csv
import os

from collections import defaultdict
from glob import glob
from typing import Dict, Iterable, Union, List

import pandas
import matplotlib.pyplot as plt

FIG_SIZE = (20, 20)


def get_name(f: str) -> str:
    return f.split('/')[-1].replace(".json", "")


def get_filenames(files: Iterable[str]) -> Dict[str, Dict[str, str]]:
    return {get_name(f): {"name": get_name(f)} for f in files}


def load_results(directory: str) -> List[Dict[str, Union[str, float]]]:
    files = glob(f"../reports/{directory}/0/*")
    number_of_tests = len(glob(f"../reports/{directory}/*"))
    r: Dict[str, Dict[str, Union[str, float]]] = get_filenames(files)
    for t in range(number_of_tests):
        for f in files:
            fn = f.split('/')[-1]
            d = json.load(open(os.path.join(f"../reports/{directory}", str(t), fn), "r"))
            r[get_name(f)][str(t + 1)] = float(d["requests_sec"])
    return [v for k, v in r.items()]


def store_results(results: Dict[str, Dict[str, Union[str, float]]]):
    with open('results.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['name', '1', '2', '3'])

        writer.writeheader()
        i: Dict[str, Union[str, float]]
        for i in results.values():
            writer.writerow(i)


def boxplot(results: pandas.DataFrame, filename: str):
    # Sort by mean asc
    results = results.reindex(results.median().sort_values(ascending=False).index, axis=1)
    plt.figure(figsize=FIG_SIZE)
    ax = results.boxplot(vert=False)
    ax.tick_params(axis='both', which='major')
    plt.xticks(rotation=90)
    plt.savefig(filename, bbox_inches='tight')


def all_graphs():
    for path in glob("../reports/*"):
        dirname = os.path.basename(path)
        results = load_results(dirname)
        df = pandas.DataFrame(results)

        plot_path = f"../plots/{dirname}"
        os.makedirs(plot_path, exist_ok=True)
        results_transposed = df.set_index("name").T
        boxplot(results_transposed, os.path.join(plot_path, "results.svg"))

        df["lang"] = df["name"].apply(lambda x: x.split('-')[0])
        for lang in set(df["lang"]):
            results_transposed = df[df["lang"] == lang].drop(["lang"], axis=1).set_index("name").T
            boxplot(results_transposed, os.path.join(plot_path, f"results-{lang}.svg"))


def compare_plots():
    averages = defaultdict(dict)
    for path in glob("../reports/*"):
        dirname = os.path.basename(path)
        results = load_results(dirname)
        df = pandas.DataFrame(results).set_index("name").T.mean()
        for name, avg in df.to_dict().items():
            averages[name].update({dirname: avg})
    results = pandas.DataFrame(averages)
    results = results.reindex(results.sum().sort_values(ascending=False).index, axis=1)
    results.T.plot.barh(figsize=FIG_SIZE)
    plt.savefig("../plots/comparison.svg", bbox_inches='tight')


def main():
    all_graphs()
    compare_plots()


if __name__ == '__main__':
    main()
