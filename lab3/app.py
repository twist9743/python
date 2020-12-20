from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from mysql_db import MySQL
import mysql.connector as connector
login_manager=LoginManager()

app = Flask(__name__)
application = app



app.config.from_pyfile('config.py')

mysql = MySQL(app)

login_manager.init_app(app)
login_manager.login_view='login'
login_manager.login_message='Для доступа к данной странице нужно аутенцифицироваться'
login_manager.login_message_category='warning'



class User(UserMixin):
    def __init__(self,user_id,login):
        super().__init__()
        self.id=user_id
        self.login=login

@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM users WHERE id=%s;', (user_id,))
    db_user = cursor.fetchone()
    cursor.close()
    if db_user:
            return User(user_id=db_user.id, login=db_user.login)
    return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method=='POST':
        login=request.form.get('login')
        password=request.form.get('password')
        remember_me=request.form.get('remember_me')=='on'
        if login and password:
            cursor = mysql.connection.cursor(named_tuple=True)
            cursor.execute('SELECT * FROM users WHERE login = %s and password_hash = SHA2(%s, 256);', (login, password))
            db_user = cursor.fetchone()
            cursor.close()
            if db_user:
                    user= User(user_id=db_user.id, login=db_user.login)
                    login_user(user, remember=remember_me)


                    flash('Вы успешно аутентифицированны','success')
                    
                    next=request.args.get('next')
                    
                    return redirect(next or url_for('index'))
        flash('Введены неверные логин и/или пароль.','danger')    
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/users')
def users():
    cursor = mysql.connection.cursor(named_tuple=True)
    cursor.execute('SELECT * FROM users;')
    users = cursor.fetchall()
    cursor.close()
    return render_template('users/index.html', users=users)



@app.route('/users/new')
@login_required
def new():
    return render_template('users/new.html', user={})

@app.route('/users/create', methods=['POST'])
@login_required
def create():
    login = request.form.get('login') or None
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    middle_name = request.form.get('middle_name')
    query = '''
        INSERT INTO users (login, password_hash, first_name, last_name, middle_name)
        VALUES (%s,SHA2(%s, 256),%s,%s,%s);
    '''
    cursor = mysql.connection.cursor(named_tuple=True)
    try:
        cursor.execute(query, (login, password, first_name, last_name, middle_name))
    except connector.errors.DatabaseError as err:
        flash('Введены некорректные данные. Ошибка сохранения.', 'danger')
        user = {
            'login' : login,
            'password' : password,
            'first_name' : first_name,
            'last_name' : last_name,
            'middle_name' : middle_name
        }
        return render_template('users/new.html', user=user)
    mysql.connection.commit()
    cursor.close()
    flash(f'Пользователь {login} был успешно создан','success')
    return redirect(url_for('users'))





if __name__ == "__main__":
    app.run(debug=True)
