import matplotlib.pyplot as plt
import pandas as pd

# Reads the CSV file
data = pd.read_csv('rotten_tomatoes_top_movies.csv')

# Create figure and axis objects
fig, ax = plt.subplots()

# Plot data on axis object
ax.plot(data['total_reviews'], data['year'], )

# Add labels, title, and legend
ax.set_xlabel('Total Reviews')
ax.set_ylabel('Year')
ax.set_title('Total reviews by Year')
ax.legend()

# Display graph
plt.show()