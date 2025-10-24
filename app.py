from flask import Flask, render_template, request

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
@app.route('/payments')
def payments():
    return render_template('payments.html')

# Contact page with form handling
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    sent = False
    name = None
    if request.method == 'POST':
        name = request.form['name']
        sent = True
    return render_template('contact.html', sent=sent, name=name)

if __name__ == "__main__":
    app.run(debug=True)


