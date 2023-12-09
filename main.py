import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

marks = np.array([72, 41, 63, 71, 81, 68, 60, 74, 52, 67, 33, 65, 78, 59, 70, 82, 55, 75, 48, 72, 25, 71, 67, 63, 70, 89, 63, 58, 45, 72, 70, 88, 42, 68, 76, 62, 73, 64, 77, 73, 54, 65, 78, 82, 67, 79, 50, 70, 85, 71, 65, 58, 63, 61, 84, 71, 73, 65, 70, 48, 64, 71, 76, 65, 77, 79, 72, 69, 64, 73, 68, 74, 65, 78, 85, 59, 70, 62, 68, 71, 82, 59, 67, 70, 82, 65, 63, 63, 70, 71, 54, 64, 73, 65, 76, 67, 77, 64, 58, 72, 100, 0])

percentiles = np.percentile(marks, [7, 13.5, 45, 80, 95, 99.2, 100]) #the percentiles for the different grades
grade_boundaries = percentiles

mean = np.mean(marks) #mean
std_dev = np.std(marks) #standard deviation

x = np.linspace(min(marks), max(marks), 1000) #makes a list of evenly distributed numbers

y = norm.pdf(x, mean, std_dev) #bell curve

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='black', linestyle='dashed', label='Bell Curve')

colors = ['purple', 'blue', 'green', 'yellow', 'orange', 'red', 'brown']
for i in range(3, 10):
    boundary = grade_boundaries[i - 3]
    plt.axvline(x=boundary, linestyle='--', color='black')
    if i == 3:
        plt.fill_between(x, 0, y, where=(x <= boundary), color=colors[i - 3], alpha=0.3)
    else:
        prev_boundary = grade_boundaries[i - 4]
        plt.fill_between(x, 0, y, where=((x > prev_boundary) & (x <= boundary)), color=colors[i - 3], alpha=0.3)

for i in range(3, 10):
    boundary = grade_boundaries[i - 3]
    if i == 3:
        area_percentage = round(np.trapz(y[np.where(x <= boundary)[0]]) / np.trapz(y), 3) * 100
        plt.text((boundary + min(marks)) / 2, 0.00025, f'Grade: {i} | {area_percentage:.1f}%', ha='center', va='bottom', color='black', rotation='vertical')
    else:
        prev_boundary = grade_boundaries[i - 4]
        area_percentage = round(np.trapz(y[np.where((x > prev_boundary) & (x <= boundary))[0]]) / np.trapz(y), 3) * 100
        plt.text(prev_boundary + (boundary - prev_boundary) / 2, 0.00025, f'Grade: {i} | {area_percentage:.1f}%', ha='center', va='bottom', color='black', rotation='vertical')

plt.xticks(np.arange(0, max(marks) + 1, 5))

plt.xlabel('Marks')
plt.ylabel('Probability Density')
plt.title('Bell Curve for Student Marks')
plt.grid(True)
plt.margins(0,0)
plt.show()
