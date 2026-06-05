from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = "quiz_secret"

# Database Connection
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="tiger",
        database="quiz_db"
    )

# Home
@app.route("/")
def home():
    return redirect("/login")


# Register
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO users(username,email,password)
            VALUES(%s,%s,%s)
            """,
            (username, email, password)
        )

        conn.commit()
        conn.close()

        return redirect("/login")

    return render_template("register.html")


# Login
@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute(
            """
            SELECT * FROM users
            WHERE username=%s AND password=%s
            """,
            (username, password)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            session["user_id"] = user["user_id"]
            session["username"] = user["username"]

            return redirect("/subjects")

    return render_template("login.html")


# Subjects Page
@app.route("/subjects")
def subjects():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM subjects")

    subjects = cursor.fetchall()

    conn.close()

    return render_template(
        "subjects.html",
        subjects=subjects
    )


# Quiz Page
@app.route("/quiz", methods=["POST"])
def quiz():

    subject_id = request.form["subject_id"]

    session["subject_id"] = subject_id

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT * FROM questions
        WHERE subject_id=%s
        """,
        (subject_id,)
    )

    questions = cursor.fetchall()

    conn.close()

    return render_template(
        "quiz.html",
        questions=questions
    )


# Submit Quiz
@app.route("/submit", methods=["POST"])
def submit():

    subject_id = session["subject_id"]

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT * FROM questions
        WHERE subject_id=%s
        """,
        (subject_id,)
    )

    questions = cursor.fetchall()

    score = 0

    for q in questions:

        user_answer = request.form.get(
            str(q["question_id"])
        )

        if user_answer == q["correct_answer"]:
            score += 1

    cursor.execute(
        """
        INSERT INTO results
        (user_id,subject_id,score)
        VALUES(%s,%s,%s)
        """,
        (
            session["user_id"],
            subject_id,
            score
        )
    )

    conn.commit()
    conn.close()

    return render_template(
        "result.html",
        score=score,
        total=len(questions)
    )


# Quiz History
@app.route("/history")
def history():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """
        SELECT s.subject_name,
               r.score,
               r.quiz_date
        FROM results r
        JOIN subjects s
        ON r.subject_id = s.subject_id
        WHERE r.user_id=%s
        """,
        (session["user_id"],)
    )

    results = cursor.fetchall()

    conn.close()

    return render_template(
        "history.html",
        results=results
    )


# Logout
@app.route("/logout")
def logout():

    session.clear()

    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)