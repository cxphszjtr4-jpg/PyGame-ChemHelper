from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''<!DOCTYPE html>
<html>
<head>
    <title>Test</title>
</head>
<body style="background: #1a1a2e; color: white; font-size: 3rem; text-align: center; padding: 50px;">
    <h1>ChemHelper Menu</h1>
    <button onclick="alert('ChemHelper')">ChemHelper</button>
    <button onclick="alert('Calculator')">Calculator</button>
    <button onclick="alert('Quiz')">Quiz</button>
    <button onclick="alert('Settings')">Settings</button>
</body>
</html>'''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
