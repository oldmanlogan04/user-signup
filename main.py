from flask import Flask, request, redirect, render_template
import re


app = Flask(__name__)
app.config['DEBUG'] = True 

username = ""
password = ""
verify = ""
email = ""


@app.route('/')
def index():
    return render_template("index.html")

#---signup page-------
@app.route("/signup", methods=["GET","POST"])
def user_signup():
    username = request.form["username"]
    password = request.form["password"]
    verify = request.form["verify"]
    email = request.form["email"]

    fail_user = ""
    fail_password = ""
    fail_verify = ""
    fail_email = ""

    if username == "":
        fail_user = "enter a username"

    if (len(username) > 0 and len(username) <= 3) or len(username) > 20:
        fail_user = "username must be 3 characters but not more than 20"

    if password == "":
        fail_password = "enter a password"
        fail_verify = "no password to verify"

    if (len(password) > 0 and len(password) <= 3) or len(password) > 20:
        fail_password = "Password must be 3 characters but not more than 20"   

    if " " in username:
        fail_user = "username cannot contain spaces"

    if " " in password:
        fail_password = "password cannot contain spaces"

    if password != "":
        if verify == "" or verify != password:
            fail_verify = "passwords do not match"

    if email != "":

        if not re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email):
            fail_email = "please enter a valid email"

    if not fail_user and not fail_password and not fail_verify and not fail_email:
        return render_template("index-wel.html", username = username)

    else:
        return render_template(
            "index.html", 
            username = username,
            fail_user = fail_user,
            fail_password = fail_password,
            fail_verify = fail_verify,
            email = email, 
            fail_email = fail_email,
    )                                 


app.run()
