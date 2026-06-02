# Population data visualization in Bar Graph

import matplotlib.pyplot as plt

from matplotlib.lines import lineStyles

cities = ["Mumbai", "Delhi", "Bengaluru", "Hyderabad", "Ahmedabad",
          "Chennai", "Kolkata", "Surat", "Pune", "Jaipur",
          "Lucknow", "Kanpur", "Nagpur", "Indore", "Thane"]

population = [20411000, 16787941, 8443675, 6772498, 5570585,
              4646732, 4486679, 4467797, 3124458, 3073350,
              2817105, 2768031, 2405565, 1838041, 1812892]

plt.figure(figsize=(20, 5))
plt.bar(cities,population, color="green")
plt.title("Top 15 Most Populous Indian Cities (Metro Area Population)")
plt.xlabel("Cities")
plt.ylabel("Population ( in CR)")
plt.legend(["Population"])
plt.savefig("populationdata.png", dpi=300)
plt.show()