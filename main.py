import pandas as pd

read = pd.read_csv("rotten_tomatoes_top_movies.csv")

#def outputData(values):
#    newdata = read[values]
#    print(newdata)

#outputData(['title','year','critic_score'])



def obtainFilter():
    # This will take in inputs for which columns the user would like to see.
    # It will check if the input is a valid input comparing to the csv file.
    # If not in the list, it will ask for input again
    # If q is entered, the data will be displayed with the appropriate values that were inputted. 

    currentfilter = []
    userinput = ""

    while userinput != "q":
        try:
            datasetList = ['title','year','synopsis','critic_score','people_score','rating','genre','original_language','director','producer','runtime','link']
            userinput = input("Enter filter data:")
            if userinput == "q":
                break
            elif userinput in datasetList:
                currentfilter.append(str(userinput))
                print(currentfilter)
            else:
                print("Invalid input, try again")

        except (ValueError,IndexError):
            print("Not valid input, try again.")
    print(read[currentfilter])

obtainFilter()