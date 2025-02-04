from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load data from file
with open('data.json') as f:
    data = json.load(f)

@app.route('/')
def hello_world():
    return 'Hello, World!'  # Return 'Hello World' in response

@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref')  # Get parameter from URL
    if pref:
        for student in data:  # Iterate dataset
            if student['pref'] == pref:  # Select only students with the given meal preference
                result.append(student)  # Add matched student to result
        return jsonify(result)  # Return filtered dataset if parameter is supplied
    return jsonify(data)  # Return entire dataset if no parameter supplied

@app.route('/students/<id>')
def get_student(id):
    for student in data:
        if student['id'] == id:  # Match student ID as a string
            return jsonify(student)
    return jsonify({'error': 'Student not found'}), 404  # Return 404 if no match found

@app.route('/stats')
def get_stats():
    pref_count = {}
    programme_count = {}

    for student in data:
        pref = student['pref']
        programme = student['programme']

        pref_count[pref] = pref_count.get(pref, 0) + 1
        programme_count[programme] = programme_count.get(programme, 0) + 1

    return jsonify({
        'pref_count': pref_count,
        'programme_count': programme_count
    })

@app.route('/add/<a>/<b>')
def add(a, b):
    try:
        a = int(a)
        b = int(b)
        return jsonify({'result': a + b})
    except ValueError:
        return jsonify({'error': 'Invalid input for addition'}), 400

@app.route('/subtract/<a>/<b>')
def subtract(a, b):
    try:
        a = int(a)
        b = int(b)
        return jsonify({'result': a - b})
    except ValueError:
        return jsonify({'error': 'Invalid input for subtraction'}), 400

@app.route('/multiply/<a>/<b>')
def multiply(a, b):
    try:
        a = int(a)
        b = int(b)
        return jsonify({'result': a * b})
    except ValueError:
        return jsonify({'error': 'Invalid input for multiplication'}), 400

@app.route('/divide/<a>/<b>')
def divide(a, b):
    try:
        a = int(a)
        b = int(b)
        if b == 0:
            return jsonify({'error': 'Cannot divide by zero'}), 400
        return jsonify({'result': a / b})
    except ValueError:
        return jsonify({'error': 'Invalid input for division'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
