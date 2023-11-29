#First Commit
print("Hello World")
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.run()

# Import libraries and packages, they contain additional functions.
from flask import Flask, render_template
# Create web application using Flask
app = Flask(__name__)
# Create our routes
@app.route('/')
def home():
 return render_template('index.html')
# Start the web application
app.run(
 debug=True
)