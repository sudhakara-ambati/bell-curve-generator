import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from scipy.stats import norm
import app

def generate_grade_boundaries(marks: list, num_grades: int):
    percentiles = np.percentile(marks, np.linspace(0, 100, num_grades))
    percentiles = np.append(percentiles, 100)
    percentiles = np.insert(percentiles, 0, 0)
    return percentiles
    
def create_curve(data, mxscore: int, mnscore: int, num_grades: int) -> Figure:
    if app.select_variables == True:
        max_input_marks = int(mxscore)
        input_marks = np.array(data)
        marks = input_marks * (100/max_input_marks)
        max_marks = max_input_marks * (100/max_input_marks)
        num_grades = 7
        grade_boundaries = generate_grade_boundaries(marks, num_grades)
        mean = np.mean(marks)
        std_dev = np.std(marks)
        x = np.linspace(min(marks), 100, 1000)
        y = norm.pdf(x, mean, std_dev)
        
        fig = Figure(figsize=(8, 6))
        FigureCanvasAgg(fig)  # Create a canvas for the figure
        ax = fig.add_subplot(111)   
        
        ax.plot(x, y, color='black', linestyle='dashed', label='Bell Curve')
        colors = ['darkred', 'red', 'orange', 'yellow', 'yellowgreen', 'lime', 'cyan']
        for i in range(2, len(grade_boundaries)):
            boundary = grade_boundaries[i]
            ax.axvline(x=boundary, linestyle='--', color='black')
            if i == 2:
                ax.fill_between(x, 0, y, where=(x <= boundary), color=colors[i - 2], alpha=0.3)
            else:
                prev_boundary = grade_boundaries[i - 1]
                ax.fill_between(x, 0, y, where=((x > prev_boundary) & (x <= boundary)), color=colors[i - 2], alpha=0.3)
        for i in range(2, len(grade_boundaries)):
            boundary = grade_boundaries[i]
            if i == 2:
                area_percentage = round(np.trapz(y[np.where(x <= boundary)[0]]) / np.trapz(y), 3) * 100
                ax.text((boundary + min(marks)) / 2, 0.00025, f'Grade: {i + 1} | {area_percentage:.1f}%', ha='center', va='bottom', color='black', rotation='vertical')
            else:
                prev_boundary = grade_boundaries[i - 1]
                area_percentage = round(np.trapz(y[np.where((x > prev_boundary) & (x <= boundary))[0]]) / np.trapz(y), 3) * 100
                ax.text(prev_boundary + (boundary - prev_boundary) / 2, 0.00025, f'Grade: {i + 1} | {area_percentage:.1f}%', ha='center', va='bottom', color='black', rotation='vertical')
        ax.set_xticks(np.arange(0, 100 + 1, 5))
        ax.set_xlabel('Marks')
        ax.set_ylabel('Probability Density')
        ax.set_title('Bell Curve for Student Marks')
        ax.grid(True)
        ax.margins(0,0)
        ax.matshow(fig)

create_curve([10, 4, 18, 7, 20, 15, 3, 11, 6, 12, 2, 16, 9, 5, 19, 8, 1, 14, 0, 13, 17, 9, 5, 18, 11, 20, 8, 12, 6, 15, 3, 16, 7, 14, 1, 13, 10, 0, 19, 2, 17, 4, 15, 7, 11, 20, 4, 17, 6, 14, 3, 10, 12, 8, 18, 9, 1, 13, 0, 19, 16, 5, 2, 8, 12, 7, 14, 11, 1, 18, 4, 20, 10, 15, 0, 17, 6, 9, 3, 13, 5, 19, 16, 2, 10, 8, 14, 1, 18, 6, 12, 9, 5, 11, 0, 15, 4, 20, 7, 16, 3, 19, 6, 12, 1, 14, 11, 8, 17, 3, 9, 5, 18, 13, 2, 7, 15, 0, 20, 10, 16, 4, 19, 12, 6, 11, 3, 14, 7, 10, 1, 18, 5, 9, 2, 15, 8, 20, 13, 0, 17, 4, 16, 6, 12, 9, 14, 3, 19, 11, 1, 18, 5, 10, 7, 13, 0, 15, 8, 20, 2, 17, 4, 16, 9, 6, 12, 1, 18, 5, 11, 7, 14, 3, 19, 0, 15, 8, 20, 10, 17, 4, 16, 6, 12, 2, 18, 5, 11, 7, 14, 3, 19, 0, 15, 8, 20, 10, 17, 4, 16, 6, 12, 2, 18, 5, 11, 7, 14, 3, 19, 0, 15, 8, 20], 30, 0, 7)
    

