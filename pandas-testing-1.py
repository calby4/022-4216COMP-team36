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

def filterData(dataset, filterList):

    filteredData = dataset[filterList]
    return filteredData

def getFilterList():
     
    filterList = []
    userInput = ""
    while True:
        userInput = input("Filter: ")

        if userInput == "!!!":
            break

        filterList.append(userInput)

    return filterList 


def main():

    data = pd.read_csv("rotten_tomatoes_top_movies.csv")

    filterList = getFilterList()

    fD = filterData(data, filterList)
    print(fD.head())

if __name__ == "__main__":
    main()