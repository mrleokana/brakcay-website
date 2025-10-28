from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Lessons page
@app.route('/lessons')
def lessons():
    return render_template('lessons.html')

# Payments page
@app.route('/payments', methods=['GET', 'POST'])
def payments():
    result = None
    if request.method == 'POST':
        method = request.form.get('payment-method')
        amount = request.form.get('amount')

        # Dummy payment success simulation
        result = {
            'status': 'success',
            'method': method.title(),
            'amount': f"${amount}",
            'tx_id': f"TX{random.randint(100000, 999999)}",
            'time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    return render_template('payments.html', result=result)

# Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')  # Make sure contact.html exists

if __name__ == '__main__':
    app.run(debug=True)
