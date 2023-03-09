from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get('/')
def questions():

    return render_template("questions.html",
                           inputs=silly_story.prompts
                           )


@app.get('/results')
def results():

    #     for (key, val) in answers.items():
    #         text = text.replace("{" + key + "}", val)
    generated_story = silly_story.generate(request.args)

    return render_template("results.html", story_text = generated_story)
