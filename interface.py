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
appWidth, appHeight = 800, 700

Data = pd.read_csv("rotten_tomatoes_top_movies.csv")

dataList = ['title','year','synopsis','critic_score','people_score','rating','genre','original_language','director','producer','runtime','link']

# App Class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        # Title of the APP
        self.title("DataSorterz")
        self.geometry(f"{appWidth}x{appHeight}")
 
        # Search Label
        self.searchLabel = ctk.CTkLabel(self,
                                      text="Search")
        self.searchLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Search Entry Field
        self.searchEntry = ctk.CTkEntry(self,
                         placeholder_text="Enter search query")
        self.searchEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
        
        self.main_button_1 = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Search")
        self.main_button_1.place(x=525, y=20)
        

 
        # Genre choice label
        self.choiceLabel = ctk.CTkLabel(self,
                                        text="Select Genre")
        self.choiceLabel.grid(row=3, column=0,
                              padx=20, pady=20,
                              sticky="ew")
 
        # Genre check boxes
        self.checkboxVar = ctk.IntVar(value=0)
         
        self.choice1 = ctk.CTkCheckBox(self, text="Title",
                                       variable=self.checkboxVar,
                                       onvalue=1,
                                       offvalue=0,
                                       )
        self.choice1.grid(row=3, column=1, padx=20,
                          pady=20, sticky="ew")
 
        self.choice2 = ctk.CTkCheckBox(self, text="Year",
                                       variable=self.checkboxVar,
                                       onvalue="choice2",
                                       offvalue="c2")                              
        self.choice2.grid(row=3, column=2, padx=20, pady=20,
                          sticky="ew")
        
        self.choice3 = ctk.CTkCheckBox(self, text="Synopsis",
                                       variable=self.checkboxVar,
                                       onvalue="choice3",
                                       offvalue="c3")                              
        self.choice3.grid(row=3, column=3, padx=20, pady=20,
                          sticky="ew")
        
        self.choice4 = ctk.CTkCheckBox(self, text="Critic Score",
                                       variable=self.checkboxVar,
                                       onvalue="choice4",
                                       offvalue="c4")                              
        self.choice4.grid(row=3, column=4, padx=20, pady=20,
                          sticky="ew")
        
        self.choice5 = ctk.CTkCheckBox(self, text="People Score",
                                       variable=self.checkboxVar,
                                       onvalue="choice5",
                                       offvalue="c5")
        self.choice5.grid(row=4, column=1, padx=20,
                          pady=20, sticky="ew")
 
        self.choice6 = ctk.CTkCheckBox(self, text="Rating",
                                       variable=self.checkboxVar,
                                       onvalue="choice6",
                                       offvalue="c6")                              
        self.choice6.grid(row=4, column=2, padx=20, pady=20,
                          sticky="ew")
        
        self.choice7 = ctk.CTkCheckBox(self, text="Genre",
                                       variable=self.checkboxVar,
                                       onvalue="choice7",
                                       offvalue="c7")                              
        self.choice7.grid(row=4, column=3, padx=20, pady=20,
                          sticky="ew")
        
        self.choice8 = ctk.CTkCheckBox(self, text="Language",
                                       variable=self.checkboxVar,
                                       onvalue="choice8",
                                       offvalue="c8")                              
        self.choice8.grid(row=4, column=4, padx=20, pady=20,
                          sticky="ew")
        
        self.choice9 = ctk.CTkCheckBox(self, text="Director",
                                       variable=self.checkboxVar,
                                       onvalue="choice9",
                                       offvalue="c9")                              
        self.choice9.grid(row=4, column=4, padx=20, pady=20,
                          sticky="ew")
        
        self.choice10 = ctk.CTkCheckBox(self, text="Producer",
                                       variable=self.checkboxVar,
                                       onvalue="choice10",
                                       offvalue="c10")                              
        self.choice10.grid(row=4, column=4, padx=20, pady=20,
                          sticky="ew")
        
        self.choice11 = ctk.CTkCheckBox(self, text="Runtime",
                                       variable=self.checkboxVar,
                                       onvalue="choice11",
                                       offvalue="c11")                              
        self.choice11.grid(row=4, column=4, padx=20, pady=20,
                          sticky="ew")
        
        self.choice12 = ctk.CTkCheckBox(self, text="Link",
                                       variable=self.checkboxVar,
                                       onvalue="choice12",
                                       offvalue="c12")                              
        self.choice12.grid(row=4, column=4, padx=20, pady=20,
                          sticky="ew")
         
        # Sort Label
        self.sortLabel = ctk.CTkLabel(self,
                                    text="Sort Order")
        self.sortLabel.grid(row=6, column=0,
                                  padx=20, pady=20,
                                  sticky="ew")
 
        # Sort Option Menu
        self.sortOptionMenu = ctk.CTkOptionMenu(self,
                                       values=["Ascending",
                                       "Descending"])
        self.sortOptionMenu.grid(row=6, column=1,
                                       padx=20, pady=20,
                                       columnspan=2, sticky="ew")
        

        dataList = ['title','year','synopsis','critic_score','people_score','rating','genre','original_language','director','producer','runtime','link']
        tree = ttk.Treeview(self,columns=dataList,show='headings')
        tree.grid()

        df = pd.read_csv("rotten_tomatoes_top_movies.csv")

        for i in dataList:
            tree.column(i,width=120,anchor='center')
            tree.heading(i,text=str(i))
        for i in range(1, len(df.iloc[1:])):
            dataList = ['title','year','synopsis','critic_score','people_score','rating','genre','original_language','director','producer','runtime','link']
            newdataList = list(df.iloc[i].loc[dataList])
            tree.insert(parent='',index='end', text='', values=newdataList)
            newdataList.clear()          
            

 
if __name__ == "__main__":
    app = App()
    app.mainloop()