from flask import Flask, request, url_for, render_template
from caesar import rotate_string


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    content = render_template('form.html', textarea_content = "", style_sheet = url_for('static', filename='style.css'))

    return content


@app.route("/", methods=['POST'])
def encrypt():
    rotation = request.form['rot']
    textstr = request.form['text']
    encrypted = rotate_string(textstr, int(rotation))
    
    return render_template('form.html', textarea_content = encrypted, style_sheet = url_for('static', filename='style.css'))
    #return "<h1>" + encrypted + "</h1>"


app.run()