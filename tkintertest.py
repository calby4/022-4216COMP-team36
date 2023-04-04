# Python program to create a basic GUI
# application using the customtkinter module
 
import customtkinter as ctk
import tkinter as tk
import pandas as pd
from tkinter import ttk
 
ctk.set_appearance_mode("dark")
 
ctk.set_default_color_theme("green")   
 
appWidth, appHeight = 800, 700

global num
dataList = ['title','year','synopsis','critic_score','people_score','rating','genre','original_language','director','producer','runtime','link']

# App Class
class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.title("DataSorterz")
        self.geometry(f"{appWidth}x{appHeight}")
        dataList = ['title','year','synopsis','critic_score','people_score','rating','genre','original_language','director','producer','runtime','link']
        tree = ttk.Treeview(self,columns=dataList,show='headings')
        tree.pack()

        df = pd.read_csv("rotten_tomatoes_top_movies.csv")

        for i in dataList:
            tree.column(i,width=90,anchor='center')
            tree.heading(i,text=str(i))
        for i in range(1, len(df.iloc[1:])):
            dataList = ['title','year','synopsis','critic_score','people_score','rating','genre','original_language','director','producer','runtime','link']
            newdataList = list(df.iloc[i].loc[dataList])
            tree.insert(parent='',index='end', text='', values=newdataList)
            newdataList.clear()          
            





if __name__ == "__main__":
    app = App()
    app.mainloop()
