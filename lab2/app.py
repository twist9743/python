from flask import Flask, render_template, url_for, request, make_response, redirect



app = Flask(__name__)
application = app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/args')
def args():
    return render_template('args.html')


@app.route('/headers')
def headers():
    return render_template('headers.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/cookies', methods=['GET', 'POST'])
def cookies():
    resp = make_response(render_template('cookies.html'))
    if 'username' in request.cookies:
        resp.set_cookie('username' , 'some name', expires=0)
    else:
        resp.set_cookie('username', 'some name')
    return resp


@app.route('/tel_form', methods=['GET', 'POST'])
def tel_form():
    if request.method=='POST':
        phone=request.form.get('tel')
        phone_number=''
        error_tel_num=''
        for symbol in phone:
            if symbol in [' ', '(',')','-','.','+']:
                continue
            elif symbol.isdigit():
                phone_number+=symbol
            else:
                error_tel_num="Недопустимый ввод. В номере телефона встречаются недопустимые символы."
                return render_template('tel_form.html',error_tel_num=error_tel_num)
        if len(phone_number)==11:
            tel_num='8-{}-{}-{}-{}'.format(phone_number[1:4],phone_number[4:7],phone_number[7:9],phone_number[9:11])
            return render_template('tel_form.html',tel_num=tel_num)
        elif len(phone_number)==10:
            tel_num='8-{}-{}-{}-{}'.format(phone_number[0:3],phone_number[3:6],phone_number[6:8],phone_number[8:])
            return render_template('tel_form.html',tel_num=tel_num)
        else:
            error_tel_num="Недопустимый ввод. Неверное количество цифр."
            return render_template('tel_form.html',error_tel_num=error_tel_num)
    return render_template('tel_form.html')
    
