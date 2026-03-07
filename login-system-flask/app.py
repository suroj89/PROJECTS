from flask import Flask, render_template, request, redirect, session
from db import conn, cursor
from datetime import datetime

app = Flask(__name__)
app.secret_key = "secretkey"


# HOME
@app.route("/")
def home():
    return redirect("/login")


# REGISTER
@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        register_time = datetime.now()

        query = "INSERT INTO users(name,email,password,register_time) VALUES(%s,%s,%s,%s)"
        cursor.execute(query,(name,email,password,register_time))
        conn.commit()

        return redirect("/login")

    return render_template("register.html")


# USER LOGIN
@app.route("/login", methods=["GET","POST"])
def login():

    if request.method == "POST":

        email = request.form['email']
        password = request.form['password']

        query = "SELECT * FROM users WHERE email=%s AND password=%s"
        cursor.execute(query,(email,password))

        user = cursor.fetchone()

        if user:

            session['user_id'] = user['id']

            login_time = datetime.now()

            query = "INSERT INTO login_logs(user_id,login_time) VALUES(%s,%s)"
            cursor.execute(query,(user['id'],login_time))
            conn.commit()

            return redirect("/dashboard")

    return render_template("login.html")


# USER DASHBOARD
@app.route("/dashboard")
def dashboard():

    if 'user_id' not in session:
        return redirect("/login")

    return render_template("user_dashboard.html")


# ADMIN LOGIN
@app.route("/admin", methods=["GET","POST"])
def admin():

    if request.method == "POST":

        username = request.form['username']
        password = request.form['password']

        query = "SELECT * FROM admin WHERE username=%s AND password=%s"
        cursor.execute(query,(username,password))

        admin = cursor.fetchone()

        if admin:
            session['admin'] = admin['username']
            return redirect("/admin_dashboard")

    return render_template("admin_login.html")


# ADMIN DASHBOARD
@app.route("/admin_dashboard")
def admin_dashboard():

    if 'admin' not in session:
        return redirect("/admin")


    # Users + last login + weekly login
    cursor.execute("""
    SELECT 
    u.id,
    u.name,
    u.email,
    u.register_time,
    MAX(l.login_time) AS last_login,
    COUNT(l.login_time) AS week_login
    FROM users u
    LEFT JOIN login_logs l
    ON u.id = l.user_id
    GROUP BY u.id
    """)

    users = cursor.fetchall()


    # Daily login count
    cursor.execute("""
        SELECT DATE(login_time) as day, COUNT(*) as total
        FROM login_logs
        GROUP BY day
        ORDER BY day DESC
    """)
    daily = cursor.fetchall()


    # Weekly login count
    cursor.execute("""
        SELECT WEEK(login_time) as week, COUNT(*) as total
        FROM login_logs
        GROUP BY week
    """)
    weekly = cursor.fetchall()


    # Total users
    cursor.execute("SELECT COUNT(*) AS total FROM users")
    total_users = cursor.fetchone()


    return render_template(
        "admin_dashboard.html",
        users=users,
        daily=daily,
        weekly=weekly,
        total_users=total_users
    )


# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


app.run(debug=True)