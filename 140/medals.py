from urllib.request import urlretrieve
import pandas as pd

data = "https://bites-data.s3.us-east-2.amazonaws.com/summer.csv"


def athletes_most_medals(data=data):
    file, _ = urlretrieve(data)
    csv_data = pd.read_csv(file)

    male_medals = csv_data[csv_data["Gender"] == "Men"]
    female_medals = csv_data[csv_data["Gender"] == "Women"]

    out = dict()
    out[male_medals["Athlete"].value_counts().index[0]] = male_medals["Athlete"].value_counts()[0]
    out[female_medals["Athlete"].value_counts().index[0]] = female_medals["Athlete"].value_counts()[0]
    return out
