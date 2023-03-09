from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def questions():

    return render_template("questions.html",
                        # use silly_story
                            inputs = silly_story.prompts
                           )

@app.get('/results')
def results():

    results = request.args.get(input)
    return render_template("results.html")