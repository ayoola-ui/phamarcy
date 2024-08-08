from flask import Flask, render_template

app = Flask(__Pharmarcy__)

@app.route('/')
def home():
    data = {
        'title': 'Pharmacy Prescription App',
        'welcome_message': 'Welcome to PharmaCare',
        'drugs': [
            {'name': 'Paracetamol', 'price': 50},
            {'name': 'Ibuprofen', 'price': 100},
            {'name': 'Amoxicillin', 'price': 200}
        ]
    }
    return render_template('index.html', data=data)

if __pharmarcy__ == '__main__':
    app.run(debug=True)
