import io, base64
from flask import Flask, request, render_template
from bell_curve import create_curve
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curve-generator', methods=['POST', 'GET'])
def curve_generator():
    error = None
    pngImageB64String = None
    if request.method == 'POST':
        mxscore = request.form['mxscore']
        mnscore = request.form['mnscore']
        if mxscore == '' or mnscore == '':
            error = 'Please fill in the forms below'
        else:
            fig = create_curve([0], mxscore, mnscore, 9)
            # Convert plot to PNG image
            pngImage = io.BytesIO()
            FigureCanvas(fig).print_png(pngImage)
            
            # Encode PNG image to base64 string
            pngImageB64String = "data:image/png;base64,"
            pngImageB64String += base64.b64encode(pngImage.getvalue()).decode('utf8')

    return render_template('curve-generator.html', error=error, image=pngImageB64String)