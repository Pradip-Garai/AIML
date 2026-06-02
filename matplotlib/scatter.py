import matplotlib.pyplot as plt

from matplotlib.lines import lineStyles

# Scatter Plot
study_hours = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_scores = [35, 45, 52, 58, 65, 72, 78, 85, 90, 95]

plt.scatter(study_hours,exam_scores, color="green", marker='.')
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.title("Study Performance Analysis")
plt.grid()
plt.show()