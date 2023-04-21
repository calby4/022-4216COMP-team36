#Data Visualisation Program for Lewis

import matplotlib.pyplot as plt
import pandas as pd
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk

# Setting the theme of the UI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")   
 
# Dimensions of the app are set
appWidth, appHeight = 800, 800

class App(ctk.CTk):

    def produceBarChart(self):
        
        newDataFrame = self.dataFrame.sort_values(by=['critic_score'], ascending=True)
        df = plt.bar(newDataFrame['title'].head(10), newDataFrame['critic_score'].head(10))
        plt.xlabel("Title")
        plt.ylabel("Critic Score")
        plt.title("Top Ten Worst Films by Critics")
        plt.show()

    def produceBarChart2(self):
        
        newDataFrame = self.dataFrame.sort_values(by=['critic_score'], ascending=False)
        df = plt.bar(newDataFrame['title'].head(10), newDataFrame['critic_score'].head(10))
        plt.xlabel("Title")
        plt.ylabel("Critic Score")
        plt.title("Top Ten Worst Films by Critics")
        plt.show()


    def __init__(self):
        super().__init__()
        self.title("Lewis' Data Visualisation")
        self.geometry(f"{appWidth}x{appHeight}")
        self.dataFrame = pd.read_csv("rotten_tomatoes_top_movies.csv")

        self.titleLabel = ctk.CTkLabel(self, text="Lewis' Data Visualisations", font=("Arial", 18))
        self.titleLabel.grid(row=0, column=1, padx=20, pady=20)

        self.criticScoreLabel = ctk.CTkLabel(self, text="Top Ten Worst Movies by Critic Score")
        self.criticScoreLabel.grid(row=1, column=0, padx=20, pady=20)

        self.criticScoreButton = ctk.CTkButton(self, text="Produce Bar Chart", command=self.produceBarChart)
        self.criticScoreButton.grid(row=1, column=1, padx=20, pady=20)

        self.criticScoreLabel2 = ctk.CTkLabel(self, text="Top Ten Best Movies by Critic Score")
        self.criticScoreLabel2.grid(row=2, column=0, pady=20, padx=20)

        self.criticScoreButton2 = ctk.CTkButton(self, text="Produce Bar Chart", command=self.produceBarChart2)
        self.criticScoreButton2.grid(row=2, column=1, pady=20, padx=20)

        self.peopleScoreLabel = ctk.CTkLabel(self, text="Top Ten Worst Movies by People Score")
        self.peopleScoreLabel.grid(row=3, column=0, pady=20, padx=20)

        self.peopleScoreButton = ctk.CTkButton(self, text="Produce Bar Chart")
        self.peopleScoreButton.grid(row=3, column=1, pady=20, padx=20)

        self.peopleScoreLabel2 = ctk.CTkLabel(self, text="Top Ten Best Films by People Score")
        self.peopleScoreLabel2.grid(row=4, column=0, pady=20, padx=20)

        self.peopleScoreButton2 = ctk.CTkButton(self, text="Produce Bar Chart")
        self.peopleScoreButton2.grid(row=4, column=1, pady=20, padx=20)

if __name__ == '__main__':
    app = App()
    app.mainloop()
