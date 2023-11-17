from flask import  *
import sqlite3
import hashlib
app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logreg123', methods=['GET','POST'])
def logreg123():
    if request.method == 'POST':
        username = request.form['username']
        h = hashlib.md5(request.form['password'].encode('utf-8'))
        password = h.hexdigest()
        lrp = int(request.form['lr'])
        con = sqlite3.connect("database.db")

        cursor = con.cursor()
        if lrp == 2:
            rights = 0
            datatosend = (username, password, rights)
            cursor.execute("INSERT INTO main (username, password, rights) VALUES (?,?,?)", datatosend)
            con.commit()
            return redirect("/")
        else:
            cursor.execute("SELECT password, rights FROM main WHERE username='"+username+"'")
            passworddb, rightsdb = cursor.fetchone()
            if (str(passworddb) == str(password)):
                return redirect("/")
            else:
                statuspas = 'Неверный пароль'
                return render_template('logreg.html', statuspas=statuspas)
    else:
        statuspas = ''
        return render_template('logreg.html', statuspas=statuspas)

@app.route('/logreg123', methods=['GET','POST'])
def logreg123():
    if request.method == 'POST':
        pass
    statuspas = ''
    return render_template('logreg.html', statuspas=statuspas)
@app.route('/museum', methods=['GET'])
def museum():
    if request.method == 'GET':
        but=1
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