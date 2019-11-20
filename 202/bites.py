import csv
from pathlib import Path
from urllib.request import urlretrieve

tmp = Path('/tmp')
stats = tmp / 'bites.csv'

if not stats.exists():
    urlretrieve('https://bit.ly/2MQyqXQ', stats)


def get_most_complex_bites(N=10, stats=stats):
    """Parse the bites.csv file (= stats variable passed in), see example
       output in the Bite description.
       Return a list of Bite IDs (int or str values are fine) of the N
       most complex Bites.
    """
    def get_bite_id(s):
        return s[5:s.index(".")]

    with open(stats, encoding="utf-8-sig") as csv_file:
        reader = csv.DictReader(csv_file, delimiter=";")
        filtered_list = [bite for bite in reader if bite["Difficulty"] != "None"]
        filtered_list.sort(key=lambda x: x["Difficulty"], reverse=True)
        return [get_bite_id(bite["Bite"]) for bite in filtered_list[:N]]


if __name__ == '__main__':
    res = get_most_complex_bites()
    print(res)
