from flask import Flask, render_template, jsonify, request, url_for
from calculations import plate_cutting, knee_calculation, embedded_part

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plate-cutting')
def plate_cutting_page():
    return render_template('plate-cutting.html')

@app.route('/knee-calculation')
def knee_calculation_page():
    return render_template('knee-calculation.html')

@app.route('/embedded-part')
def embedded_part_page():
    return render_template('embedded-part.html')

@app.route('/calculate/plate-cutting', methods=['POST'])
def calculate_plate_cutting():
    data = request.json
    result = plate_cutting.calculate(data)
    return jsonify(result)

@app.route('/calculate/knee-calculation', methods=['POST'])
def calculate_knee():
    data = request.json
    result = knee_calculation.calculate(data)
    return jsonify(result)

@app.route('/calculate/embedded-part', methods=['POST'])
def calculate_embedded_part():
    data = request.json
    result = embedded_part.calculate(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)