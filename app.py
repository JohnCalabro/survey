from flask import Flask, request, render_template, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def view_home():
    title = satisfaction_survey.title
    directions = satisfaction_survey.instructions
    return render_template("home.html", title = title, rules=directions)

@app.route('/questions/0')
def view_q1():
    q = satisfaction_survey.questions[0].question
    choice_a = satisfaction_survey.questions[0].choices[0]
    choice_b = satisfaction_survey.questions[0].choices[1]
    return render_template("question1.html", q1=q, yes=choice_a, no=choice_b)

@app.route('/questions/1')
def view_q2():
    q = satisfaction_survey.questions[1].question
    choice_a = satisfaction_survey.questions[1].choices[0]
    choice_b = satisfaction_survey.questions[1].choices[1]
    return render_template("question2.html", q2=q, yes=choice_a, no=choice_b)

@app.route('/questions/2')
def view_q3():
    
    q = satisfaction_survey.questions[2].question
    choice_a = satisfaction_survey.questions[2].choices[0]
    choice_b = satisfaction_survey.questions[2].choices[1]
    return render_template("question3.html", q3=q, yes=choice_a, no=choice_b)

@app.route('/questions/3')
def view_q4():
    
    q = satisfaction_survey.questions[3].question
    choice_a = satisfaction_survey.questions[3].choices[0]
    choice_b = satisfaction_survey.questions[3].choices[1]
    return render_template("question4.html", q4=q, yes=choice_a, no=choice_b)


@app.route('/thanks')
def thank_you():
    return render_template("thanks.html")

# @app.route('/session', methods=["POST"])
# def store_in_session():
#     start = request.form['save']
#     res = []


@app.route('/answer', methods=["POST"])
def post_answ():
    answer = request.form['answ']
    test = False

    responses.append(answer)
    # return render_template('test_answer.html', r=responses)
    # if len(responses) == 2:
    #     return redirect('/questions/2')
    # elif len(responses) == 1:
    if len(responses) >3: # I add to cookies here I think in this condional block
        session['user_results'] = responses
        return redirect('/thanks')
    if len(responses) == 3:
        return redirect('/questions/3')

    if len(responses) == 2:
        return redirect('/questions/2')

    elif len(responses) == 1:

        return redirect('/questions/1')
   
    

    
    
# @app.route('/answer', methods=["POST"])
# def post_answ2():
    
#     answer2 = request.form['answ2']
#     responses.append(answer2)
    
#     return redirect('/questions/2')