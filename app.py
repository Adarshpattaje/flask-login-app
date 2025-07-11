from flask import Flask, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'my-super-secret-key-123'

USERNAME = "admin123"
PASSWORD = "password123"

@app.route('/')
def home(): 
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def index():
    userName = request.form['username']
    userPassword = request.form['password']
    
    if userName == USERNAME and userPassword == PASSWORD:
        session['users'] = []
        return redirect(url_for('dashboard'))
    else:
        return "Login failed. Please check your username and password."
    
@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'users' not in session:
        session['users'] = []

    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        role = request.form.get('role')

        if name and email and role:
            # Add to session
            user_entry = {'name': name, 'email': email, 'role': role}
            users = session['users']
            users.append(user_entry)
            session['users'] = users  # Save back to session

        return redirect(url_for('dashboard'))

    return render_template('dashboard.html', users=session['users'])


if __name__ == '__main__':
    app.run(debug=True)