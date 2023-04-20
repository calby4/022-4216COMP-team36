import matplotlib.pyplot as plt
import pandas as pd
import customtkinter as ctk

def plot_critic_score_by_year():
    # Load the data
    data = pd.read_csv('rotten_tomatoes_top_movies.csv')

    # Group the data by year and calculate the mean critic score
    grouped_data = data.groupby('year')['critic_score'].mean()

    # Set the size of the figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create the bar chart
    ax.bar(grouped_data.index, grouped_data.values)

    # Set the title and axis labels
    ax.set_title('Critic Score by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Critic Score')

    # Set the x-axis limits
    ax.set_xlim(left=2000, right=2025)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add gridlines
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)

    # Show the plot
    plt.show()

def plot_people_score_by_year():
    # Load the data
    data = pd.read_csv('rotten_tomatoes_top_movies.csv')

    # Group the data by year and calculate the mean critic score
    grouped_data = data.groupby('year')['people_score'].mean()

    # Set the size of the figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create the bar chart
    ax.bar(grouped_data.index, grouped_data.values)

    # Set the title and axis labels
    ax.set_title('People score by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('People Score')

    # Set the x-axis limits
    ax.set_xlim(left=2000, right=2025)
    ax.set_ylim(top=100, bottom=0)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add gridlines
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)

    # Show the plot
    plt.show()

def scatter_plot_critic_score_by_year():
    # Load the data
    data = pd.read_csv('rotten_tomatoes_top_movies.csv')

    # Group the data by year and calculate the mean critic score
    grouped_data = data.groupby('year')['critic_score'].mean()

    # Set the size of the figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create the scatter plot
    ax.scatter(grouped_data.index, grouped_data.values)

    # Set the title and axis labels
    ax.set_title('Critic Score by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('Critic Score')

    # Set the x-axis limits
    ax.set_xlim(left=2000, right=2025)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add gridlines
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)

    # Show the plot
    plt.show()

def scatter_plot_people_score_by_year():
    # Load the data
    data = pd.read_csv('rotten_tomatoes_top_movies.csv')

    # Group the data by year and calculate the mean people score
    grouped_data = data.groupby('year')['people_score'].mean()

    # Set the size of the figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create the scatter plot
    ax.scatter(grouped_data.index, grouped_data.values)

    # Set the title and axis labels
    ax.set_title('People score by Year')
    ax.set_xlabel('Year')
    ax.set_ylabel('People Score')

    # Set the x-axis and y-axis limits
    ax.set_xlim(left=2000, right=2025)
    ax.set_ylim(bottom=0, top=100)

    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Add gridlines
    ax.grid(True, axis='y', linestyle='--', alpha=0.5)

    # Show the plot
    plt.show()


# Create a tkinter window
window = ctk.CTk()
window.title("Data Visualisations By Callum")
window.geometry("400x200")  # Width x Height in pixels

# Setting the theme of the UI
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")   

# Create a button that calls the plot_critic_score_by_year function when clicked
plotButton1 = ctk.CTkButton(window, text="Plot Critic Score by Year", command=plot_critic_score_by_year)
plotButton1.pack(pady=10)

# Create a button that calls the plot_rating_by_genre function when clicked
plotButton2 = ctk.CTkButton(window, text="Plot People Score by Year", command=plot_people_score_by_year)
plotButton2.pack(pady=10)

plotButton3 = ctk.CTkButton(window, text="Scatter Plot Critic Score by Year", command=scatter_plot_critic_score_by_year)
plotButton3.pack(pady=10)

plotButton4 = ctk.CTkButton(window, text="Scatter Plot People Score by Year", command=scatter_plot_people_score_by_year)
plotButton4.pack(pady=10)

# Start the tkinter event loop
window.mainloop()