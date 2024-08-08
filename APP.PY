from flask import Flask, render_template, request, jsonify

app = Flask(__pharmarcy__)

# Sample data
drugs = [
    {"name": "Paracetamol", "price": 50},
    {"name": "Ibuprofen", "price": 100},
    {"name": "Amoxicillin", "price": 200},
]

@app.route('/')
def index():
    return render_template('index.html', drugs=drugs)

@app.route('/prescribe', methods=['POST'])
def prescribe():
    prescription = request.json
    # Process prescription here (e.g., save to database)
    return jsonify({"status": "success", "message": "Prescription received!"})

if __pharmarcy__ == '__main__':
    app.run(debug=True)
