from flask import Flask, request, redirect, Response, session, url_for

app = Flask(__name__)
# app.secret_key = "supersecret"

@app.route("/", methods=["GET", "POST"])
@app.route("/submit", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials. Try again.", mimetype="text/plain")

    return '''
        <h2>Login Page</h2>
        <form method="POST">
            username: <input type="text" name="username"><br>
            password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''


@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
            <h2>Welcome, {session["user"]}!</h2>
            <a href="{url_for('logout')}">Logout</a>
        '''
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return '''
        <h2>You have been logged out successfully.</h2>
        <a href="/submit">Login again</a>
    '''

# # ❌ Fix the condition here:
if __name__ == "__main__":
    app.run(debug=True)
