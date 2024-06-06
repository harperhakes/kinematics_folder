from flask import Flask, render_template, request #hello

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculators')
def calculators():
    return render_template('calculators.html')

@app.route('/calculate1', methods=['POST'])
def calculate1():
    v0 = float(request.form['v0'])
    a = float(request.form['a'])
    t = float(request.form['t'])
    v1 = v0 + a * t
    return render_template('calculators.html', v1=v1)

@app.route('/calculate2', methods=['POST'])
def calculate2():
    v0 = float(request.form['v0'])
    v = float(request.form['v'])
    t = float(request.form['t'])
    dx1 = ((v + v0) / (2 * t))
    return render_template('calculators.html', dx1=dx1)

@app.route('/calculate3', methods=['POST'])
def calculate3():
    v0 = float(request.form['v0'])
    a = float(request.form['a'])
    t = float(request.form['t'])
    dx2 = v0 * t + 0.5 * a * t**2
    return render_template('calculators.html', dx2=dx2)

@app.route('/calculate4', methods=['POST'])
def calculate4():
    v0 = float(request.form['v0'])
    a = float(request.form['a'])
    dx = float(request.form['dx'])
    v2 = v0**2 + 2 * a * dx
    return render_template('calculators.html', v2=v2)

if __name__ == '__main__':
    app.run(debug=True)
