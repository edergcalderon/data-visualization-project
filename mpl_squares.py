import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()    ### generates one or more plots in the same figure
ax.plot(squares, linewidth=3)   ### controls thickness of line that plot() generates

# Set chart title and level axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis='both', labelsize=14)   ### tick_params() styles the tick marks

plt.show()