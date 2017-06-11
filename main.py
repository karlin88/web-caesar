from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin 0 auto;
                    width: 540px;
                    font: 16px 'Arial', sans-serif;
                    border-radius: 10px;
                }
                textarea {
                    marin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
    <body>
        <!--create yoru form here-->
        <form action="/" method="post">
            Rotate by:
            <input type="text" name="rot" value ="0"/>
            <textarea name="text"></textarea>
            <input type="submit" value="Submit Query" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    content = form

    return content


@app.route("/", methods=['POST'])
def encrypt():
    rotation = request.form['rot']
    textstr = request.form['text']
    content = "<h1>" + rotate_string(textstr, int(rotation)) + "</h1>"
    
    return content


app.run()