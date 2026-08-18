from flask import Blueprint, render_template, request, session, flash, url_for, redirect

auth_bp = Blueprint('auth', __name__)

USER_CREDENTIALS = {
    'username': 'admin',
    'password': '1234'
}

@auth_bp.route('/login', methods=['GET', 'POST'])  # Fixed typo here
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        if username == USER_CREDENTIALS['username'] and password == USER_CREDENTIALS['password']:
            session['username'] = username
            flash('Login successful!', 'success')
            return redirect(url_for('auth.login'))  # You can change this to your dashboard or home route
        else:
            flash('Invalid credentials, please try again.', 'danger')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))