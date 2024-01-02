import os.path

from flask import  *
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
import sqlite3
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = ('qwertyuiopasdfghjklzxcvbnm')
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'database.db')))
login_manager = LoginManager()

class User(UserMixin):
    def __init__(self, username, tm_role=False):
        self.id = username
        self.tm_role = tm_role


users = {
    'user1': User('user1'),
    'user2': User('user2', tm_role=True),
    'qwes': User('user2', tm_role=True)
}




buttons= ['это кнопка', 'это тоже', 'ТАм парам пам это тоже кнопка','А это нет', 'я пошитил это тоже кнопка','Это MaxiMax9055']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logreg', methods=['GET','POST'])
def logreg():
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
            login_user(username)
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



@app.route('/museum', methods=['GET'])
def museum():
    if request.method == 'GET':
        but=request.args.get('but')
        if but == None:
            but=-1
        else:
            print("Data:")
            print(but)

    return render_template('museum.html', buttons=buttons)

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


@app.route('/logout')
@login_required
def logout():
    logout_user()

@login_manager.user_loader
def load_user(username):
    print("load_user")
    #return UserLogin().fromDB(username,dbase)


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()

def get_db():
    if not hasattr(g,'link_db'):
        g.link_db = connect_db()
    return g.link_db

@app.context_processor
def context_processor():
    def is_tm_role():
        return current_user.tm_role if current_user.is_authenticated else False
    return dict(is_tm_role=is_tm_role)





if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)