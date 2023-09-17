from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
debug = DebugToolbarExtension(app)

@app.route('/')
def story_form():
    story_prompts = story.prompts
    return render_template('story_form.html', story_prompts=story_prompts)    

@app.route('/story')
def show_story():
    story_text = story.generate(request.args)
    return render_template('display-story.html', story_text=story_text)
    