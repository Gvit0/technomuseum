from flask import  *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logreg', methods=['GET','POST'])
def logreg():
    if request.method == 'POST':
        usenname = request.form['username']
        password = request.form['password']
        lr = int(request.form['lr'])
        print(usenname,password,lr)
        return redirect("/")
    else:
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
def irdm():
    return render_template('irdm.html')

@app.route('/ird/mvov')
def irdmvov():
    return render_template('irdmvov.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)