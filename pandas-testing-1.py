import pandas as pd
import numpy as np


"""
function filterData
params  dataset (pandas DataFrame), *filters (tuple)
returns filteredData (pandas DataFrame)

The purpose of this function is to return a subset of the inital DataFrame.
It determines this subset by using filters and returns only the information where
it satisfies those conditions.
"""

def filterData(dataset, *filters):

    filterList = []
    for i in filters:
        filterList.append(i)

    filteredData = dataset[filterList]
    return filteredData

def main():

    data = pd.read_csv("rotten_tomatoes_top_movies.csv")

    fD = filterData(data, "title", "synopsis", "people_score", "critic_score")
    print(fD)

if __name__ == "__main__":
    main()