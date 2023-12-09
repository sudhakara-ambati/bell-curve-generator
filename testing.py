import numpy as np
import matplotlib.pyplot as plt

def pdf(x, data):
    mean = np.mean(data)
    std_dev = np.std(data)
    y = 1 / (std_dev * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
    return y

# Generate random marks
marks = np.array([72, 41, 63, 71, 81, 68, 60, 74, 52, 67, 33, 65, 78, 59, 70, 82, 55, 75, 48, 72, 25, 71, 67, 63, 70, 89, 63, 58, 45, 72, 70, 88, 42, 68, 76, 62, 73, 64, 77, 73, 54, 65, 78, 82, 67, 79, 50, 70, 85, 71, 65, 58, 63, 61, 84, 71, 73, 65, 70, 48, 64, 71, 76, 65, 77, 79, 72, 69, 64, 73, 68, 74, 65, 78, 85, 59, 70, 62, 68, 71, 82, 59, 67, 70, 82, 65, 63, 63, 70, 71, 54, 64, 73, 65, 76, 67, 77, 64, 58, 72])
print(marks)

# Calculate grade boundaries
percentiles = np.percentile(marks, [0, 12, 24, 36, 48, 60, 72, 84, 96, 100])
grade_boundaries = [percentiles[0], percentiles[1], percentiles[2], percentiles[3], percentiles[4], percentiles[5], percentiles[6], percentiles[7], percentiles[8], percentiles[9]]

# Assign grades based on boundaries
grades = np.zeros(len(marks), dtype=int)
for i, mark in enumerate(marks):
    if mark <= grade_boundaries[0]:
        grades[i] = 1
    elif grade_boundaries[0] < mark <= grade_boundaries[1]:
        grades[i] = 2
    elif grade_boundaries[1] < mark <= grade_boundaries[2]:
        grades[i] = 3
    elif grade_boundaries[2] < mark <= grade_boundaries[3]:
        grades[i] = 4
    elif grade_boundaries[3] < mark <= grade_boundaries[4]:
        grades[i] = 5
    elif grade_boundaries[4] < mark <= grade_boundaries[5]:
        grades[i] = 6
    elif grade_boundaries[5] < mark <= grade_boundaries[6]:
        grades[i] = 7
    elif grade_boundaries[6] < mark <= grade_boundaries[7]:
        grades[i] = 8
    else:
        grades[i] = 9

x = np.linspace(0, 100, 1000)
y = pdf(x, marks)

plt.figure(figsize=(8, 6))
plt.plot(x, y, color='black', linestyle='dashed', label='Bell Curve')

# Calculate mean and adjust boundaries if necessary
mean = np.mean(marks)
if grade_boundaries[5] <= mean <= grade_boundaries[6]:
    pass  # The mean is already in the desired grade range
else:
    # Adjust the grade boundaries to ensure the mean falls within the 6/7 range
    delta = mean - (grade_boundaries[5] + grade_boundaries[6]) / 2
    grade_boundaries[5] += delta
    grade_boundaries[6] += delta

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'cyan', 'magenta', 'brown']
for i in range(1, 10):
    boundary = grade_boundaries[i]
    plt.axvline(x=boundary, linestyle='--', color='black')
    if i == 1:
        plt.fill_between(x, 0, y, where=(x <= boundary), color=colors[i - 1], alpha=0.3)
        area_percentage = round(np.trapz(y[np.where(x <= boundary)[0]]) / np.trapz(y), 3) * 100
        plt.text(boundary - 3, 0.00025, f'Grade: {i} | {area_percentage:.1f}%', ha='center', va='bottom', color='black', rotation='vertical')
    else:
        prev_boundary = grade_boundaries[i - 1]
        plt.fill_between(x, 0, y, where=((x > prev_boundary) & (x <= boundary)), color=colors[i - 1], alpha=0.3)
        area_percentage = round(np.trapz(y[np.where((x > prev_boundary) & (x <= boundary))[0]]) / np.trapz(y), 3) * 100
        plt.text(prev_boundary + (boundary - prev_boundary) / 2, 0.00025, f'Grade: {i} | {area_percentage:.1f}%', ha='center', va='bottom', color='black', rotation='vertical')

plt.xlabel('Marks')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.margins(0,0)
plt.show()

print(mean)

