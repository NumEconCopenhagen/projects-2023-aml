import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets

# autoreload modules when code is run
%load_ext autoreload
%autoreload 2



# Read the Excel sheet into a Pandas DataFrame
df = pd.read_excel('dataprj.xlsx', sheet_name='Sheet 1')

# Access the columns of the DataFrame
Year = df['Year']
S = df['S']
I = df['I']
r = df['r']

print(S)
print(I)
print(r)

# Create a figure with two y-axes
fig, ax1 = plt.subplots()

# Plot S and I on the first y-axis
ax1.plot(Year, S, label='Savings (left-axis)')
ax1.plot(Year, I, label='Investments (left-axis)')


# Set the label and color of the first y-axis
ax1.set_xlabel('Year')
ax1.set_ylabel('Billions')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis
ax2 = ax1.twinx()

# Plot r on the second y-axis
ax2.plot(Year, r, color='red', label='interest rate (right-axis)')

# Set the label and color of the second y-axis
ax2.set_ylabel('pct')
ax2.tick_params(axis='y', labelcolor='red')

# this indicates the time when in intrest rates turn negative.
ax1.axvline(x=Year.iloc[56], color='green')

# Set the x-tick locations and labels
ax1.set_xticks(Year)
ax1.set_xticklabels(Year, rotation=60, ha='right')

# Set the x-tick frequency to every 5th quarter
ax1.xaxis.set_ticks(Year[::5])

# Show legend for both y-axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

ax1.grid(True)
# Show the plot
plt.show()

# Creating the figure for the log
fig, ax1 = plt.subplots()

y1_data = np.log10(df['S'])
y2_data = np.log10(df['I'])

# Plot S and I on the first y-axis
ax1.plot(Year, y1_data, label='log Savings (left-axis)')
ax1.plot(Year, y2_data, label='log Investments (left-axis)')


# Set the label and color of the first y-axis
ax1.set_xlabel('Year')
ax1.set_ylabel('Log growth')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis
ax2 = ax1.twinx()

# Plot r on the second y-axis
ax2.plot(Year, r, color='red', label='interest rate (right-axis)')

# Set the label and color of the second y-axis
ax2.set_ylabel('pct')
ax2.tick_params(axis='y', labelcolor='red')

# this indicates the time when in intrest rates turn negative.
ax1.axvline(x=Year.iloc[56], color='green')

# Set the x-tick locations and labels
ax1.set_xticks(Year)
ax1.set_xticklabels(Year, rotation=60, ha='right')

# Set the x-tick frequency to every 5th quarter
ax1.xaxis.set_ticks(Year[::5])

# Show legend for both y-axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

ax1.grid(True)
# Show the plot
plt.show()

#to find a more precise plot I will take the fourth difference of all the variables.
S_diff = S.diff().diff().diff().diff()
I_diff = I.diff().diff().diff().diff()
r_diff = r.diff().diff().diff().diff()


#I will use this to make a new plot.

fig, ax1 = plt.subplots()

# Plot the fourth difference of S and I on the first y-axis
ax1.plot(Year, S_diff, label='Savings (left-axis)')
ax1.plot(Year, I_diff, label='Investments (left-axis)')

# Set the label and color of the first y-axis
ax1.set_xlabel('Year')
ax1.set_ylabel('Billions difference')
ax1.tick_params(axis='y', labelcolor='blue')

# Create a second y-axis
ax2 = ax1.twinx()

# Plot the fourth difference of r on the second y-axis
ax2.plot(Year, r_diff, color='red', label='interest rate (right-axis)')

# Set the label and color of the second y-axis
ax2.set_ylabel('pct difference')
ax2.tick_params(axis='y', labelcolor='red')

# Set the x-tick locations and labels
ax1.set_xticks(Year.index[::4])
ax1.set_xticklabels(Year[::4], rotation=45, ha='right')

# This indicates the time when in intrest rates turn negative.
ax1.axvline(x=Year.iloc[56], color='green')
ax1.axvline(x=Year.iloc[4], color='black')

# Show legend for both y-axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
ax1.grid(True)
# Show the plot
plt.show()





