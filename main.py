from flask import  *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logreg')
def logreg():
    return render_template('logreg.html')

@app.route('/museum')
def museum():
    return render_template('museum.html')

@app.route('/museumvov')
def museumvov():
    return render_template('museumvov.html')

@app.route('/ar')
def ar():
    return render_template('ar.html')

@app.route('/ar-online')
def aronline():
    return render_template('ar-online.html')

@app.route('/ird/m')
def aronline():
    return render_template('irdm.html')

@app.route('/ird/mvov')
def aronline():
    return render_template('irdmvov.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)