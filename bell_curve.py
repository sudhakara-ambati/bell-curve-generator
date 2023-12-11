import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from scipy.stats import norm

def generate_grade_boundaries(marks: list, num_grades: int):
    percentiles = np.percentile(marks, np.linspace(0, 100, num_grades))
    percentiles = np.append(percentiles, 100)
    percentiles = np.insert(percentiles, 0, 0)
    return percentiles
    
def create_curve(data, mxscore: int, mnscore: int, num_grades: int) -> Figure:
    max_input_marks = int(mxscore)
    input_marks = np.array(data)
    marks = input_marks * (100/max_input_marks)
    multiplier = (100/max_input_marks)
    max_marks = max_input_marks * (100/max_input_marks)
    num_grades = 7
    grade_boundaries = generate_grade_boundaries(marks, num_grades)
    mean = np.mean(marks)
    std_dev = np.std(marks)
    x = np.linspace(min(marks), 100, 1000)
    y = norm.pdf(multiplier * x, mean, std_dev)
    
    fig = Figure(figsize=(8, 6))
    FigureCanvasAgg(fig)  # Create a canvas for the figure
    ax = fig.add_subplot(111)   
    
    ax.plot(x, y, color='black', linestyle='dashed', label='Bell Curve')
    colors = ['darkred', 'red', 'orange', 'yellow', 'yellowgreen', 'lime', 'cyan']
    for i in range(2, len(grade_boundaries)):
        boundary = grade_boundaries[i]/multiplier
        ax.axvline(x=boundary, linestyle='--', color='black')
        if i == 2:
            ax.fill_between(x, 0, y, where=(x <= boundary), color=colors[i - 2], alpha=0.3)
        else:
            prev_boundary = grade_boundaries[i - 1]/multiplier
            ax.fill_between(x, 0, y, where=((x > prev_boundary) & (x <= boundary)), color=colors[i - 2], alpha=0.3)
    for i in range(2, len(grade_boundaries)):
        boundary = grade_boundaries[i]/multiplier
        if i == 2:
            area_percentage = round(np.trapz(y[np.where(x <= boundary)[0]]) / np.trapz(y), 3) * 100
            ax.text((boundary + min(marks)) / 2, 0.00025, f'Grade: {i + 1} | {area_percentage:.1f}%', ha='center', va='bottom', color='black', rotation='vertical')
        else:
            prev_boundary = grade_boundaries[i - 1]/multiplier
            area_percentage = round(np.trapz(y[np.where((x > prev_boundary) & (x <= boundary))[0]]) / np.trapz(y), 3) * 100
            ax.text(prev_boundary + (boundary - prev_boundary) / 2, 0.00025, f'Grade: {i + 1} | {area_percentage:.1f}%', ha='center', va='bottom', color='black', rotation='vertical')
    
    original_interval = 5
    new_distance = original_interval * multiplier

    ax.set_xlim(min(marks), max_input_marks + new_distance)

    ax.set_xlabel('Marks')
    ax.set_ylabel('Probability Density')
    ax.set_title('Bell Curve for Student Marks')
    ax.grid(True)
    ax.margins(0, 0)
    return fig