from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample user data for validation (for demonstration purposes)
users = {
    'doctor': {'username': 'doc1', 'password': 'pass123'},
    'patient': {'username': 'pat1', 'password': 'pass123'},
    'management': {'username': 'man1', 'password': 'pass123'}
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form['role']
        if role == 'doctor':
            return redirect(url_for('doctor_login'))
        elif role == 'patient':
            return redirect(url_for('patient_login'))
        elif role == 'management':
            return redirect(url_for('management_login'))
    return render_template('login.html')

@app.route('/doctor_login', methods=['GET', 'POST'])
def doctor_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == users['doctor']['username'] and password == users['doctor']['password']:
            return redirect(url_for('doctor_dashboard'))
        else:
            return "Invalid credentials for Doctor"
    return render_template('login_form.html', role="Doctor")

@app.route('/patient_login', methods=['GET', 'POST'])
def patient_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == users['patient']['username'] and password == users['patient']['password']:
            return redirect(url_for('patient_dashboard'))
        else:
            return "Invalid credentials for Patient"
    return render_template('login_form.html', role="Patient")

@app.route('/management_login', methods=['GET', 'POST'])
def management_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == users['management']['username'] and password == users['management']['password']:
            return redirect(url_for('management_dashboard'))
        else:
            return "Invalid credentials for Management"
    return render_template('login_form.html', role="Management")

# Dummy dashboards for each role
@app.route('/doctor_dashboard')
def doctor_dashboard():
    return "Welcome to Doctor's Dashboard"

@app.route('/patient_dashboard')
def patient_dashboard():
    return "Welcome to Patient's Dashboard"

@app.route('/management_dashboard')
def management_dashboard():
    return "Welcome to Management's Dashboard"

if __name__ == '__main__':
    app.run(debug=True)
