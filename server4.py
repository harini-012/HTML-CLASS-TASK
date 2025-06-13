from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('11.06.2025.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('fname')
    if not name:   
        return "Name can't be empty"
    return f"Hi, {name}"

if __name__ == '__main__':
    app.run(debug=True)
