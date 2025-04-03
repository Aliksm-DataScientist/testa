from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():

    
    return f"<h1>Hello CI / CD 111111</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)