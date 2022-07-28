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

    return render_template("survey_start.html")






@app.get("/questions")
def show_questions():


    return render_template("question.html")










@app.get("/completion")
def lets_open_completion():
    """redirect to this after survey is completed"""
    return render_template("completion.html")