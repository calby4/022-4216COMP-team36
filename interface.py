# Interface for data sorting program

# Import required libraries
 
import customtkinter as ctk
import tkinter as tk
import pandas as pd
from tkinter import ttk
 
 # Setting the theme of the UI
ctk.set_appearance_mode("dark")
 
ctk.set_default_color_theme("green")   
 
 # Dimensions of the app are set
appWidth, appHeight = 1600, 700

Data = pd.read_csv("rotten_tomatoes_top_movies.csv")

dataList = ['title','year','synopsis','critic_score','people_score','rating','genre','original_language','director','producer','runtime','link']

# App Class
class App(ctk.CTk):

    """
    function getColumnsForTable
    params self

    This function generates the columns for the tree Table. It works by first checking if all values are set to 0,
    if so, return the default columnList (dataList) otherwise, go through the list and add the correct columns
    (where the value in checkboxData == 1)
    """

    def getColumnsForTable(self):
        
        #if all values are equal to 0, then display all columns
        total = -1
        for i in range(0, len(self.checkboxData)):
            total += self.checkboxData[i].get()

        if total == -1:
            return self.dataList
        else:
            newColumnList = []
            for i in range(0, len(self.checkboxData)):
                if self.checkboxData[i].get() == 1:
                    newColumnList.append(self.dataList[i])
            
            return newColumnList

    """
    function generateTableData
    params  self

    This function generates the data that is displayed in self.tree, or rather displays the movies and their
    corresponding attributes.
    """
    def generateTableData(self, dataFile, columns):

        for item in self.tree.get_children():
            self.tree.delete(item)

        for i in columns:
            self.tree.heading(i, text=str(i))
            self.tree.column(i, width=120, stretch=False)
        
        for i in range(1, len(dataFile.iloc[1:])):
            newdataList = list(dataFile.iloc[i].loc[columns])
            self.tree.insert(parent='',index='end', text='', values=newdataList)
            newdataList.clear()   

    """
    function generateTable
    params self

    Generates a treeview named self.tree. 
    """

    def generateTable(self):

        columns = self.getColumnsForTable()
        self.tree = ttk.Treeview(self,columns=columns,show='headings')
        self.tree.grid(row=7, column = 1, columnspan=5, rowspan = 3)
        return columns


    """
    function searchFunction
    params self

    This function grabs the data from the searchEntry CTkEntry widget and returns it to the generateTableData function
    to edit the output of the table.
    """
    def searchFunction(self):
        
        searchEntryData = self.searchEntry.get()
        columns = self.getColumnsForTable()
        if searchEntryData == "":
            self.generateTableData(self.dataFile, columns)
        else:
            newDataFrame = self.dataFile.loc[(self.dataFile['title'].str.contains(searchEntryData)) | (self.dataFile['title'].str == searchEntryData)]
            self.generateTableData(newDataFrame, columns)
            self.searchEntry.delete(first_index=0 ,last_index=tk.END)

    def fillCheckboxData(self):
        for i in range(0, 12):
            self.checkboxData.append(tk.IntVar(value=0))
    """
    function refreshFunction
    params self

    This function clears all filters from the table by destroying the table and re-creating it.
    """
    def refreshFunction(self):
        
        #Clear all filters
        self.choice1.deselect()
        self.choice2.deselect()
        self.choice3.deselect()
        self.choice4.deselect()
        self.choice5.deselect()
        self.choice6.deselect()
        self.choice7.deselect()
        self.choice8.deselect()
        self.choice9.deselect()
        self.choice10.deselect()
        self.choice11.deselect()
        self.choice12.deselect()

        #destroy tree and regenerate as new.
        self.tree.destroy()
        columns = self.generateTable()
        self.generateTableData(self.dataFile, columns)

    def updateFunction(self):
        
        #destroy tree and regenerate as new.
        self.tree.destroy()
        columns = self.generateTable()
        self.generateTableData(self.dataFile, columns)


    """
    function init
    params self, *args, **kwargs

    This function initialises our tk application. 
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        # Title of the APP
        self.title("Rotten Tomatoes Top Movies Data Searcher")
        self.geometry(f"{appWidth}x{appHeight}")
        self.dataList = ['title','year','synopsis','critic_score','people_score','rating','genre','original_language','director','producer','runtime','link']
        self.checkboxData = []

        #Initialises an empty filter list and creates a pandas DataFrame object from our CSV
        self.dataFile = pd.read_csv("rotten_tomatoes_top_movies.csv")

        # Search Label
        self.searchLabel = ctk.CTkLabel(self, text="Search")
        self.searchLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
 
        # Search Entry Field
        self.searchEntry = ctk.CTkEntry(self, placeholder_text="Enter search query")
        self.searchEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
        
        self.searchButton = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Search", command=self.searchFunction)
        self.searchButton.grid(row = 0, column = 4)

        #Refresh Table button.
        self.refreshTableButton = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Clear Filters", command=self.refreshFunction)
        self.refreshTableButton.grid(row = 0, column = 5)
 
        # Filter choice label
        self.choiceLabel = ctk.CTkLabel(self, text="Select Filters")
        self.choiceLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
 
        self.fillCheckboxData()

        # Filter check boxes
         
        self.choice1 = ctk.CTkCheckBox(self, text="Title", variable=self.checkboxData[0], onvalue=1, offvalue=0, command=self.updateFunction)
        self.choice1.grid(row=3, column=1, padx=20, pady=20, sticky="ew")
 
        self.choice2 = ctk.CTkCheckBox(self, text="Year", variable=self.checkboxData[1], onvalue=1, offvalue=0, command=self.updateFunction)                              
        self.choice2.grid(row=3, column=2, padx=20, pady=20, sticky="ew")
        
        self.choice3 = ctk.CTkCheckBox(self, text="Synopsis", variable=self.checkboxData[2], onvalue=1, offvalue=0, command=self.updateFunction)                              
        self.choice3.grid(row=3, column=3, padx=20, pady=20, sticky="ew")
        
        self.choice4 = ctk.CTkCheckBox(self, text="Critic Score", variable=self.checkboxData[3], onvalue=1, offvalue=0, command=self.updateFunction)                              
        self.choice4.grid(row=3, column=4, padx=20, pady=20, sticky="ew")
        
        self.choice5 = ctk.CTkCheckBox(self, text="People Score", variable=self.checkboxData[4], onvalue=1, offvalue=0, command=self.updateFunction) 
        self.choice5.grid(row=4, column=1, padx=20, pady=20, sticky="ew")
 
        self.choice6 = ctk.CTkCheckBox(self, text="Rating", variable=self.checkboxData[5], onvalue=1, offvalue=0, command=self.updateFunction)                               
        self.choice6.grid(row=4, column=2, padx=20, pady=20, sticky="ew")
        
        self.choice7 = ctk.CTkCheckBox(self, text="Genre", variable=self.checkboxData[6],onvalue=1, offvalue=0, command=self.updateFunction)                              
        self.choice7.grid(row=4, column=3, padx=20, pady=20, sticky="ew")
        
        self.choice8 = ctk.CTkCheckBox(self, text="Language", variable=self.checkboxData[7], onvalue=1, offvalue=0, command=self.updateFunction)                              
        self.choice8.grid(row=4, column=4, padx=20, pady=20, sticky="ew")
        
        self.choice9 = ctk.CTkCheckBox(self, text="Director", variable=self.checkboxData[8], onvalue=1, offvalue=0, command=self.updateFunction)                              
        self.choice9.grid(row=5, column=1, padx=20, pady=20, sticky="ew")
        
        self.choice10 = ctk.CTkCheckBox(self, text="Producer", variable=self.checkboxData[9], onvalue=1, offvalue=0, command=self.updateFunction)                             
        self.choice10.grid(row=5, column=2, padx=20, pady=20, sticky="ew")
        
        self.choice11 = ctk.CTkCheckBox(self, text="Runtime", variable=self.checkboxData[10], onvalue=1, offvalue=0, command=self.updateFunction)                              
        self.choice11.grid(row=5, column=3, padx=20, pady=20, sticky="ew")
        
        self.choice12 = ctk.CTkCheckBox(self, text="Link", variable=self.checkboxData[11], onvalue=1, offvalue=0, command=self.updateFunction)                               
        self.choice12.grid(row=5, column=4, padx=20, pady=20, sticky="ew")
         
        # Sort Label
        #self.sortLabel = ctk.CTkLabel(self, text="Sort Order")
       # self.sortLabel.grid(row=6, column=0, padx=20, pady=20, sticky="ew")
 
        # Sort Option Menu
        #self.sortOptionMenu = ctk.CTkOptionMenu(self, values=["Ascending", "Descending"])
        #self.sortOptionMenu.grid(row=6, column=1, padx=20, pady=20,  sticky="ew")
        
        #Creates the grid used to display the data.
        columns = self.generateTable()
        self.generateTableData(self.dataFile, columns)


if __name__ == "__main__":
    app = App()
    app.mainloop()