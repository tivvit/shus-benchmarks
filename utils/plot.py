import csv

from typing import List, Union, Dict

import pandas
import matplotlib.pyplot as plt


def load_results(filename: str) -> List[Dict[str, Union[str, float]]]:
    with open(filename) as f:
        return [i for i in csv.DictReader(f)]


def boxplot(results: pandas.DataFrame, filename: str):
    # Sort by mean asc
    results = results.reindex(results.median().sort_values(ascending=False).index, axis=1)
    ax = results.boxplot(vert=False)
    plt.xticks(rotation=90)
    plt.savefig(filename, bbox_inches='tight')


def main():
    results = load_results("results.csv")
    df = pandas.DataFrame(results)

    results_transposed = df.set_index("name").T.astype(float)
    boxplot(results_transposed, "../plots/results.svg")

    df["lang"] = df["name"].apply(lambda x: x.split('-')[0])
    for lang in set(df["lang"]):
        plt.figure()
        results_transposed = df[df["lang"] == lang].drop(["lang"], axis=1).set_index("name").T.astype(float)
        boxplot(results_transposed, f"../plots/results-{lang}.svg")


if __name__ == '__main__':
    main()
