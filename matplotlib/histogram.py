import matplotlib.pyplot as plt

from matplotlib.lines import lineStyles

# Histogram 
electricity_bills = [1200, 1350, 1420, 1580, 1650, 1720, 1850, 1920, 2100,
                     2250, 2350, 2480, 2600, 2750, 2900, 3100, 3250, 3400,
                     1800, 1950, 2050, 2200, 2400, 2550, 2700]
plt.hist(electricity_bills, bins=5, color="yellow", edgecolor="black")
plt.title("Monthly Electricity Bills (25 households)")
plt.xlabel("Bill Amount")
plt.ylabel("Months")
plt.show()