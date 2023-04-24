import matplotlib.pyplot as plt
import pandas as pd

# Read CSV file
data = pd.read_csv('filename.csv')

# Create figure and axis objects
fig, ax = plt.subplots()

# Plot data on axis object
ax.plot(data['Column1'], data['Column2'], label='Data Label')

# Add labels, title, and legend
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_title('Graph Title')
ax.legend()

# Display graph
plt.show()