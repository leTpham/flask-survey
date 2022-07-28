from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)


# empty list to store the user's responses
responses = []

@app.get("/begin")
def get_begin_survey():

    return render_template("survey_start.html", survey=survey)

# link post to button click link

@app.post("/begin")
def post_begin_survey():

    return redirect("/questions/0")





@app.get("/questions/<int:question_id>")
def show_questions(question_id):
    """for loop over satisfaction survey questions[0].question
    to generate each question per page index 0 - 3 initially """
    # i = 0
    # while i < satisfaction_survey.questions.length
    #     question .question
    #     i = i + 1
    question = survey.questions[question_id]
    
    return render_template("question.html", question=question)

@app.post("/answer")
def take_answer():

    answer = request.form("answer")
    responses.append(answer)














@app.get("/completion")
def lets_open_completion():
    """redirect to this after survey is completed"""
    return render_template("completion.html")