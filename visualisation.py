import pandas as pd
import matplotlib.pyplot as plt
from tkinter import ttk
import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue") 


class App(ctk.CTk):

    def produceBarChart(self):
        # Read CSV file into a Pandas DataFrame
        data = pd.read_csv('rotten_tomatoes_top_movies.csv')

        # Create a bar plot of the 'count' column
        plt.bar(data['year'], data['critic_score'])

        # Add labels and title
        plt.xlabel('Year')
        plt.ylabel('Critic Score')
        plt.title('Critic Score over the years.')

        # Show plot
        plt.show()

    def produceScatter(self):

        # Read CSV file into a Pandas DataFrame
        data = pd.read_csv('rotten_tomatoes_top_movies.csv')

        # Create scatter plot
        plt.scatter(data['year'], data['critic_score'])

        # Add labels and title
        plt.xlabel('Year')
        plt.ylabel('Critic Score')
        plt.title('Scatter Plot of Critic score over the years.')

        # Show graph
        plt.show()

    def produceProductionBar(self):
        # Reads CSV file to a Pandas DataFrame
        data = pd.read_csv('rotten_tomatoes_top_movies.csv')

        # Sorts the dataframe by the people score. Default Ascending.
        sortedData = data.sort_values('people_score')

        # Creates a bar chart of the first 5 in the sorted list.
        plt.bar(sortedData['title'].head(), (sortedData['people_score'].head()))
        # Adds labels to chart.
        plt.xlabel('Production Company')
        plt.ylabel('People Score')

        # Adds title to chart
        plt.title('Top 5 worst films based off people score.')

        #Displays chart.
        plt.show()

    def produceBoxPlot(self):
        # Reads CSV file to a Pandas DataFrame
        data = pd.read_csv('rotten_tomatoes_top_movies.csv')

        # Creates a boxplot based off critic score, showing outliers.
        plt.boxplot(data['critic_score'],showfliers=True)

        #Adds labels.
        plt.xlabel('X')
        plt.ylabel('Critic Score')
        plt.title('Boxplot of the critic score')

        # Displays plot.
        plt.show()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.title("Connor's Data Visualisation")
        self.geometry('800x600')

        self.Chart1 = ctk.CTkLabel(self, text="Critic score over the years")
        self.Chart1.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        self.BarChartYear = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Bar Plot",command=self.produceBarChart)
        self.BarChartYear.grid(row = 1, column = 0)

        self.ScatterYear = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Scatter Plot",command=self.produceScatter)
        self.ScatterYear.grid(row = 1, column = 1)

        self.ProdBar = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Bar Plot",command=self.produceProductionBar)
        self.ProdBar.grid(row = 3, column = 0)

        self.ProdBar = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), text="Box Plot",command=self.produceBoxPlot)
        self.ProdBar.grid(row = 5, column = 0)

        self.Chart3 = ctk.CTkLabel(self, text="Boxplot of the critic score.")
        self.Chart3.grid(row=4, column=0, padx=20, pady=20, sticky="ew")

        self.Chart2 = ctk.CTkLabel(self, text="5 Worst titles based off people score.")
        self.Chart2.grid(row=2, column=0, padx=20, pady=20, sticky="ew")



    


if __name__ == "__main__":
    app = App()
    app.mainloop()