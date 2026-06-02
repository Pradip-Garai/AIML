import matplotlib.pyplot as plt

from matplotlib.lines import lineStyles
# Daily step walked
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
steps = [6500, 7700, 5800, 9900, 10500, 11500, 12200]

# Create a Line Graph
plt.plot(days,steps, color="green", marker="o", markerfacecolor="yellow", markeredgecolor='black',
         linestyle="--")
plt.xlabel("Days")
plt.ylabel("Steps")
plt.title("Daily Walking Progress")
plt.legend(["Steps Work"])
plt.grid()
plt.show()