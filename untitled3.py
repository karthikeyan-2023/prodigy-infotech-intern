import pandas as pd
import matplotlib.pyplot as plt

# Read the data into a Pandas DataFrame
data = pd.read_csv('your_data_file.csv')

# Get the column you want to plot
data_to_plot = data['your_column_name']

# Create the histogram plot
plt.hist(data_to_plot)

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of your_column_name')

# Show the plot
plt.show()