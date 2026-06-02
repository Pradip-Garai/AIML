import matplotlib.pyplot as plt

from matplotlib.lines import lineStyles

from matplotlib import colors
from enum import auto
# Products data visualization in Pia Chart
items = ["Laptops", "Mobiles", "Headphones", "Chargers", "Smartwatches", "Tablets"]
quantity = [150, 420, 380, 290, 175, 95]

colors = ["#FFB7B2", "#FFDAC1", "#E2F0CB", "#B5EAD7", "#C7CEEA", "#F5C6A0"]
plt.pie(quantity, labels=items, autopct='%1.1f%%' , startangle=90, colors=colors)
plt.legend(["Product Details"])
plt.title("Electronics Store Sales by Quantity")
plt.show()