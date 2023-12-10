import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def generate_grade_boundaries(marks, num_grades):
    percentiles = np.percentile(marks, np.linspace(0, 100, num_grades)) # evenly distributed percentiles
    percentiles = np.append(percentiles, 100)  # Add the 100th percentile explicitly
    percentiles = np.insert(percentiles, 0, 0)  # Add the 0th percentile explicitly
    return percentiles
    

marks = np.array([72, 41, 63, 71, 81, 68, 60, 74, 52, 67, 33, 65, 78, 59, 70, 82, 55, 75, 48, 72, 25, 71, 67, 63, 70, 89, 63, 58, 45, 72, 70, 88, 42, 68, 76, 62, 73, 64, 77, 73, 54, 65, 78, 82, 67, 79, 50, 70, 85, 71, 65, 58, 63, 61, 84, 71, 73, 65, 70, 48, 64, 71, 76, 65, 77, 79, 72, 69, 64, 73, 68, 74, 65, 78, 85, 59, 70, 62, 68, 71, 82, 59, 67, 70, 82, 65, 63, 63, 70, 71, 54, 64, 73, 65, 76, 67, 77, 64, 58, 72])
num_grades = 7  # grade amount

grade_boundaries = generate_grade_boundaries(marks, num_grades)

mean = np.mean(marks)
std_dev = np.std(marks)

x = np.linspace(min(marks), 100, 1000)
y = norm.pdf(x, mean, std_dev) # student bell curve

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='black', linestyle='dashed', label='Bell Curve')

colors = ['darkred', 'red', 'orange', 'yellow', 'yellowgreen', 'lime', 'cyan']
for i in range(2, len(grade_boundaries)):
    boundary = grade_boundaries[i]
    plt.axvline(x=boundary, linestyle='--', color='black')
    if i == 2:
        plt.fill_between(x, 0, y, where=(x <= boundary), color=colors[i - 2], alpha=0.3)
    else:
        prev_boundary = grade_boundaries[i - 1]
        plt.fill_between(x, 0, y, where=((x > prev_boundary) & (x <= boundary)), color=colors[i - 2], alpha=0.3)

for i in range(2, len(grade_boundaries)):
    boundary = grade_boundaries[i]
    if i == 2:
        area_percentage = round(np.trapz(y[np.where(x <= boundary)[0]]) / np.trapz(y), 3) * 100
        plt.text((boundary + min(marks)) / 2, 0.00025, f'Grade: {i + 1} | {area_percentage:.1f}%', ha='center', va='bottom', color='black', rotation='vertical')
    else:
        prev_boundary = grade_boundaries[i - 1]
        area_percentage = round(np.trapz(y[np.where((x > prev_boundary) & (x <= boundary))[0]]) / np.trapz(y), 3) * 100
        plt.text(prev_boundary + (boundary - prev_boundary) / 2, 0.00025, f'Grade: {i + 1} | {area_percentage:.1f}%', ha='center', va='bottom', color='black', rotation='vertical')


plt.xticks(np.arange(0, 100 + 1, 5))

plt.xlabel('Marks')
plt.ylabel('Probability Density')
plt.title('Bell Curve for Student Marks')
plt.grid(True)
plt.margins(0, 0)
plt.show()