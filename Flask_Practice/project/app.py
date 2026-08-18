from flask import Flask, render_template, request, flash, url_for, redirect
from forms import RegistrationForm

app = Flask(__name__)
app.secret_key = "shubham"

@app.route("/", methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        flash(f" Welcome {name}! You have successfully registered with the email {email}.", "success")
        return redirect(url_for("success"))
    return render_template("register.html", form=form)

@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)