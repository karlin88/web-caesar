from flask import Flask, request
from caesar import rotate_string
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template_form = jinja_env.get_template('form.html')    
    content = template_form.render(textarea_content = "")

    return content


@app.route("/", methods=['POST'])
def encrypt():
    rotation = request.form['rot']
    textstr = request.form['text']
    encrypted = rotate_string(textstr, int(rotation))
    template_form = jinja_env.get_template('form.html')
    
    return template_form.render(textarea_content = encrypted)
    #return "<h1>" + encrypted + "</h1>"


app.run()