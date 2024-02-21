"""
A parallel way to scrape *interest over time* data from Google Trends
by using *pytrends* library.
"""

import json
from multiprocessing import Pool
from datetime import datetime

from pytrends.request import TrendReq


def task(country: str, language: str, value: str) -> None:
    startdate = datetime(2013, 1, 1)
    enddate = datetime(2018, 1, 1)

    print(f"{country}, {language}, {value}\n")

    trend: TrendReq = TrendReq(hl=language, geo=country)
    trend.build_payload(
        kw_list=[value], timeframe=f"{startdate.date()} {enddate.date()}"
    )
    df = trend.interest_over_time()
    df.to_json(f"../datasets/json_queries/{value}_{country}.json", orient="index")


if __name__ == "__main__":
    with open("../json/queries.json", "r") as f:
        cqs: dict = json.load(f)

    args: list[tuple[str, str, str]] = []

    for cq in cqs:
        country = cq["country"]
        for query in cq["queries"]:
            language = query["language"]
            for value in query["values"]:
                args.append((country, language, value))

    with Pool() as pool:
        results = pool.starmap(task, args, chunksize=10)
