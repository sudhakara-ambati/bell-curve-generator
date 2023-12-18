import numpy as np
import io, base64
from flask import Flask, request, render_template
from bell_curve import create_curve
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

select_variables = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curve-generator', methods=['POST', 'GET'])
def curve_generator():
    error = None
    pngImageB64String = None
    input_list = None  # Initialize input_list outside the try block

    if request.method == 'POST':
        mxscore = request.form['mxscore']
        mnscore = request.form['mnscore']
        input_list_str = request.form['input_list']
        select_variables = True

        if mxscore == '' or mnscore == '' or input_list_str == '':
            error = 'Please fill in the forms below'
        else:
            try:
                input_list = list(map(int, input_list_str.split(',')))  # map all strs in the list to ints
            except ValueError:
                error = "The input marks are not in the format of a list"
                input_list = None  # Set input_list to None upon exception

        if input_list is not None:  # Check if input_list is not None before proceeding
            fig = create_curve(input_list, mxscore, mnscore, 7)
            # Convert plot to PNG image
            pngImage = io.BytesIO()
            FigureCanvas(fig).print_png(pngImage)

            # Encode PNG image to base64 string
            pngImageB64String = "data:image/png;base64,"
            pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return render_template('curve-generator.html', error=error, image=pngImageB64String)
