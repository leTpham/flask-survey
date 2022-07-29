from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


# empty list to store the user's responses

# responses = []

@app.get("/")
def start_route():
    session["responses"] = []
    return redirect("/begin")


@app.get("/begin")
def get_begin_survey():

    return render_template("survey_start.html", survey=survey)


@app.post("/begin")
def post_begin_survey():

    return redirect("/questions/0")


@app.get("/questions/<int:question_id>")
def show_questions(question_id):
    """for loop over satisfaction survey questions[0].question
    to generate each question per page index 0 - 3 initially """

    responses = session["responses"]

    if question_id != len(responses):
        flash("You're not supposed to go there!")
        return redirect(f"/questions/{len(responses)}")

    if len(responses) == len(survey.questions):
        return redirect("/completion")

    question = survey.questions[question_id]
    return render_template("question.html", question=question)


@app.post("/answer")
def take_answer():

    answer = request.form["answer"]

    responses = session["responses"]

    responses.append(answer)
    session["responses"] = responses
    # set variable (answers_collected) for session["responses"]

    # append answer from form to answers_collected
    # reset session["responses"] to be equal to answers_collected

    if len(responses) < len(survey.questions):
        return redirect(f"/questions/{len(responses)}")
    return redirect("/completion")


@app.get("/completion")
def lets_open_completion():
    """redirect to this after survey is completed"""
    return render_template("completion.html")
