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

    def generateTableData(self,newData):
        self.tree.delete(*self.tree.get_children())
        num = 0
        if self.filtered:
            for i in dataList:
                self.tree.heading(i,text="")
            for i in self.filterList:
                self.tree.column(i,anchor='center',width=120)
                self.tree.heading(i,text=str(i))
            self.tree.delete(*self.tree.get_children())
            for i in range(1, len(newData)):
                newdataList = list(self.dataFile.iloc[i].loc[self.filterList])
                self.tree.insert(parent='',index='end', text='', values=newdataList)
                newdataList.clear()
        else:
            for i in dataList:
                self.tree.column(i,width=120,anchor='center')
                self.tree.heading(i,text=str(i))
            for i in range(1, len(self.dataFile.iloc[1:])):
                newdataList = list(self.dataFile.iloc[i].loc[dataList])
                self.tree.insert(parent='',index='end', text='', values=newdataList)
                newdataList.clear()  
             
             

 

    def searchFunction(self):
        
        titleToGet = self.searchEntry.get()
        print(titleToGet)
        self.searchEntry.configure(textvariable="Enter search query")

    def filterTitle(self):
        if(self.titleVar.get() == 1):
            print("yes")
            self.filterList.append("title")
            self.filtered = True
            print(self.filterList)
            print(self.filtered)

    def filterYear(self):
        if(self.yearVar.get() == 1):
            print("yes")
            self.filterList.append("year")
            self.filtered = True
            print(self.filterList)
            print(self.filtered)

    def filterSynopsis(self):
        if(self.synopsisVar.get() == 1):
            print("yes")
            self.filterList.append("synopsis")
            self.filtered = True
            print(self.filterList)
            print(self.filtered)

    def filterCritic(self):
        if(self.criticScoreVar.get() == 1):
            print("yes")
            self.filterList.append("critic_score")
            self.filtered = True
            print(self.filterList)
            print(self.filtered)

    def filterPeople(self):
        if(self.peopleScoreVar.get() == 1):
            print("yes")
            self.filterList.append("people_score")
            self.filtered = True
            print(self.filterList)
            print(self.filtered)

    def filterRating(self):
        if(self.ratingVar.get() == 1):
            print("yes")
            self.filterList.append("rating")
            self.filtered = True
            print(self.filterList)
            print(self.filtered)

    def filterGenre(self):
        if(self.genreVar.get() == 1):
            print("yes")
            self.filterList.append("genre")
            self.filtered = True
            print(self.filterList)
            print(self.filtered)

    def filterLanguage(self):
        if(self.languageVar.get() == 1):
            print("yes")
            self.filterList.append("language")
            self.filtered = True
            print(self.filterList)
            print(self.filtered)

    def filterDirector(self):
        if(self.directorVar.get() == 1):
            print("yes")
            self.filterList.append("director")
            self.filtered = True
            print(self.filterList)
            print(self.filtered)

    def filterProducer(self):
        if(self.producerVar.get() == 1):
            print("yes")
            self.filterList.append("producer")
            self.filtered = True
            print(self.filterList)
            print(self.filtered)

    def filterRuntime(self):
        if(self.runtimeVar.get() == 1):
            print("yes")
            self.filterList.append("runtime")
            self.filtered = True
            print(self.filterList)
            print(self.filtered)
        elif(self.runtimeVar.get == 0):
            self.filterList.remove("runtime")

    def filterLink(self):
        if(self.linkVar.get() == 1):
            print("yes")
            self.filterList.append("link")
            self.filtered = True
            print(self.filterList)
            print(self.filtered)
        
    def updateTable(self):
                newData = self.dataFile[self.filterList]
                self.generateTableData(newData)

            

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        # Title of the APP
        self.title("DataSorterz")
        self.geometry(f"{appWidth}x{appHeight}")
        self.filterList = []
        self.dataFile = pd.read_csv("rotten_tomatoes_top_movies.csv") 
        self.filtered = False
 
        # Search Label
        self.searchLabel = ctk.CTkLabel(self, text="Search")
        self.searchLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")
 
        # Search Entry Field
        self.searchEntry = ctk.CTkEntry(self, placeholder_text="Enter search query")
        self.searchEntry.grid(row=0, column=1, columnspan=3, padx=20, pady=20, sticky="ew")
        
        self.searchButton = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Search", command=self.searchFunction)
        self.searchButton.grid(row = 0, column = 5)

        self.updateField = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Update Field", command=self.updateTable)
        self.updateField.grid(row = 0, column = 6)
        

 
        # Genre choice label
        self.choiceLabel = ctk.CTkLabel(self, text="Select Genre")
        self.choiceLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")
 
        # Genre check boxes
        self.titleVar = ctk.IntVar(value=0)
         
        self.choice1 = ctk.CTkCheckBox(self, text="Title", variable=self.titleVar, onvalue=1, offvalue=0,command=self.filterTitle)
        self.choice1.grid(row=3, column=1, padx=20, pady=20, sticky="ew")

        self.yearVar = ctk.IntVar(value=0)
 
        self.choice2 = ctk.CTkCheckBox(self, text="Year", variable=self.yearVar, onvalue=1, offvalue=0,command=self.filterYear)                              
        self.choice2.grid(row=3, column=2, padx=20, pady=20, sticky="ew")

        self.synopsisVar = ctk.IntVar(value=0)
        
        self.choice3 = ctk.CTkCheckBox(self, text="Synopsis", variable=self.synopsisVar, onvalue=1, offvalue=0, command=self.filterSynopsis)                              
        self.choice3.grid(row=3, column=3, padx=20, pady=20, sticky="ew")

        self.criticScoreVar = ctk.IntVar(value=0)
        
        self.choice4 = ctk.CTkCheckBox(self, text="Critic Score", variable=self.criticScoreVar, onvalue=1, offvalue=0,command=self.filterCritic)                              
        self.choice4.grid(row=3, column=4, padx=20, pady=20, sticky="ew")

        self.peopleScoreVar = ctk.IntVar(value=0)
        
        self.choice5 = ctk.CTkCheckBox(self, text="People Score", variable=self.peopleScoreVar, onvalue=1, offvalue=0,command=self.filterPeople)
        self.choice5.grid(row=4, column=1, padx=20, pady=20, sticky="ew")

        self.ratingVar = ctk.IntVar(value=0)
 
        self.choice6 = ctk.CTkCheckBox(self, text="Rating", variable=self.ratingVar, onvalue=1, offvalue=0,command=self.filterRating)                              
        self.choice6.grid(row=4, column=2, padx=20, pady=20, sticky="ew")

        self.genreVar = ctk.IntVar(value=0)
        
        self.choice7 = ctk.CTkCheckBox(self, text="Genre", variable=self.genreVar,onvalue=1, offvalue=0,command=self.filterGenre)                              
        self.choice7.grid(row=4, column=3, padx=20, pady=20, sticky="ew")

        self.languageVar = ctk.IntVar(value=0)
        
        self.choice8 = ctk.CTkCheckBox(self, text="Language", variable=self.languageVar, onvalue=1, offvalue=0,command=self.filterLanguage)                              
        self.choice8.grid(row=4, column=4, padx=20, pady=20, sticky="ew")
        
        self.directorVar = ctk.IntVar(value=0)

        self.choice9 = ctk.CTkCheckBox(self, text="Director", variable=self.directorVar, onvalue=1, offvalue=0,command=self.filterDirector)                              
        self.choice9.grid(row=5, column=1, padx=20, pady=20, sticky="ew")

        self.producerVar = ctk.IntVar(value=0)
        
        self.choice10 = ctk.CTkCheckBox(self, text="Producer", variable=self.producerVar, onvalue=1, offvalue=0,command=self.filterProducer)                              
        self.choice10.grid(row=5, column=2, padx=20, pady=20, sticky="ew")

        self.runtimeVar = ctk.IntVar(value=0)
        
        self.choice11 = ctk.CTkCheckBox(self, text="Runtime", variable=self.runtimeVar, onvalue=1, offvalue=0,command=self.filterRuntime)                              
        self.choice11.grid(row=5, column=3, padx=20, pady=20, sticky="ew")

        self.linkVar = ctk.IntVar(value=0)
        
        self.choice12 = ctk.CTkCheckBox(self, text="Link", variable=self.linkVar, onvalue=1, offvalue=0,command=self.filterLink)                              
        self.choice12.grid(row=5, column=4, padx=20, pady=20, sticky="ew")
         
        # Sort Label
        self.sortLabel = ctk.CTkLabel(self, text="Sort Order")
        self.sortLabel.grid(row=6, column=0, padx=20, pady=20, sticky="ew")
 
        # Sort Option Menu
        self.sortOptionMenu = ctk.CTkOptionMenu(self, values=["Ascending", "Descending"])
        self.sortOptionMenu.grid(row=6, column=1, padx=20, pady=20,  sticky="ew")
        
        #Creates the grid used to display the data.
        self.dataList = ['title','year','synopsis','critic_score','people_score','rating','genre','original_language','director','producer','runtime','link']
        self.tree = ttk.Treeview(self,columns=dataList,show='headings')
        self.tree.grid(row=7, column = 1, columnspan=5)     
        self.generateTableData(self.dataFile)

 
if __name__ == "__main__":
    app = App()
    app.mainloop()