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
    function generateTableData
    params  self

    This function generates the data that is displayed in self.tree, or rather displays the movies and their
    corresponding attributes.
    """
    def generateTableData(self, dataFile):

        for item in self.tree.get_children():
            self.tree.delete(item)

        for i in self.dataList:
            self.tree.column(i,width=120,anchor='center')
            self.tree.heading(i,text=str(i))
        
        for i in range(1, len(dataFile.iloc[1:])):
            newdataList = list(dataFile.iloc[i].loc[self.dataList])
            self.tree.insert(parent='',index='end', text='', values=newdataList)
            newdataList.clear()   

    """
    function searchFunction
    params self

    This function grabs the data from the searchEntry CTkEntry widget and returns it to the generateTableData function
    to edit the output of the table.
    """
    def searchFunction(self):
        
        searchEntryData = self.searchEntry.get()
        if searchEntryData == "":
            self.generateTableData(self.dataFile)
        else:
            newDataFrame = self.dataFile.loc[self.dataFile['title'].str.contains(searchEntryData, case=False)]
            self.generateTableData(newDataFrame)
            self.searchEntry.delete(first_index=0 ,last_index=tk.END)
                
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        # Title of the APP
        self.title("Rotten Tomatoes Top Movies Data Searcher")
        self.geometry(f"{appWidth}x{appHeight}")

        #Initialises an empty filter list and creates a pandas DataFrame object from our CSV
        self.filterList = []
        self.dataFile = pd.read_csv("rotten_tomatoes_top_movies.csv")

        # Search Label
        self.searchLabel = ctk.CTkLabel(self, text="Search")
        self.searchLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
 
        # Search Entry Field
        self.searchEntry = ctk.CTkEntry(self, placeholder_text="Enter search query")
        self.searchEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
        
        self.searchButton = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Search", command=self.searchFunction)
        self.searchButton.grid(row = 0, column = 4)
 
        # Filter choice label
        self.choiceLabel = ctk.CTkLabel(self, text="Select Filters")
        self.choiceLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
 
        # Filter check boxes
        self.checkbox1Var = ctk.IntVar(value=0)
        self.checkboxVar = ctk.IntVar(value=0)
         
        self.choice1 = ctk.CTkCheckBox(self, text="Title", variable=self.checkbox1Var, onvalue=1, offvalue=0)
        self.choice1.grid(row=3, column=1, padx=20, pady=20, sticky="ew")
 
        self.choice2 = ctk.CTkCheckBox(self, text="Year", variable=self.checkboxVar, onvalue=1, offvalue=0)                              
        self.choice2.grid(row=3, column=2, padx=20, pady=20, sticky="ew")
        
        self.choice3 = ctk.CTkCheckBox(self, text="Synopsis", variable=self.checkboxVar, onvalue=1, offvalue=0)                              
        self.choice3.grid(row=3, column=3, padx=20, pady=20, sticky="ew")
        
        self.choice4 = ctk.CTkCheckBox(self, text="Critic Score", variable=self.checkboxVar, onvalue=1, offvalue=0)                              
        self.choice4.grid(row=3, column=4, padx=20, pady=20, sticky="ew")
        
        self.choice5 = ctk.CTkCheckBox(self, text="People Score", variable=self.checkboxVar, onvalue=1, offvalue=0)
        self.choice5.grid(row=4, column=1, padx=20, pady=20, sticky="ew")
 
        self.choice6 = ctk.CTkCheckBox(self, text="Rating", variable=self.checkboxVar, onvalue=1, offvalue=0)                              
        self.choice6.grid(row=4, column=2, padx=20, pady=20, sticky="ew")
        
        self.choice7 = ctk.CTkCheckBox(self, text="Genre", variable=self.checkboxVar,onvalue=1, offvalue=0)                              
        self.choice7.grid(row=4, column=3, padx=20, pady=20, sticky="ew")
        
        self.choice8 = ctk.CTkCheckBox(self, text="Language", variable=self.checkboxVar, onvalue=1, offvalue=0)                              
        self.choice8.grid(row=4, column=4, padx=20, pady=20, sticky="ew")
        
        self.choice9 = ctk.CTkCheckBox(self, text="Director", variable=self.checkboxVar, onvalue=1, offvalue=0)                              
        self.choice9.grid(row=5, column=1, padx=20, pady=20, sticky="ew")
        
        self.choice10 = ctk.CTkCheckBox(self, text="Producer", variable=self.checkboxVar, onvalue=1, offvalue=0)                              
        self.choice10.grid(row=5, column=2, padx=20, pady=20, sticky="ew")
        
        self.choice11 = ctk.CTkCheckBox(self, text="Runtime", variable=self.checkboxVar, onvalue=1, offvalue=0)                              
        self.choice11.grid(row=5, column=3, padx=20, pady=20, sticky="ew")
        
        self.choice12 = ctk.CTkCheckBox(self, text="Link", variable=self.checkboxVar, onvalue=1, offvalue=0)                              
        self.choice12.grid(row=5, column=4, padx=20, pady=20, sticky="ew")
         
        # Sort Label
        self.sortLabel = ctk.CTkLabel(self, text="Sort Order")
        self.sortLabel.grid(row=6, column=0, padx=20, pady=20, sticky="ew")
 
        # Sort Option Menu
        self.sortOptionMenu = ctk.CTkOptionMenu(self, values=["Ascending", "Descending"])
        self.sortOptionMenu.grid(row=6, column=1, padx=20, pady=20,  sticky="ew")
        
        #Creates the grid used to display the data.
        self.dataList = ['title','year','synopsis','critic_score','people_score','rating','genre','original_language','director','producer','runtime','link']
        self.tree = ttk.Treeview(self,columns=self.dataList,show='headings')
        self.tree.grid(row=7, column = 1, columnspan=5, rowspan = 3)     
        self.generateTableData(self.dataFile)


if __name__ == "__main__":
    app = App()
    app.mainloop()