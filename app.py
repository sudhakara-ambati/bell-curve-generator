from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/curve-generator', methods=['POST', 'GET'])
def curve_generator():
    error = None
    if request.method == 'POST':
        mxscore = request.form['mxscore']
        mnscore = request.form['mnscore']
        if mxscore == '' or mnscore == '':
            error = 'Please fill in the forms below'
        else:
            print()

    return render_template('curve-generator.html', error=error)