import bcrypt
from app import app
from app.models.tables import User
from bottle import template, static_file, request, redirect
import logging

# static routes


@app.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='app/static/css')


@app.get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='app/static/js')


@app.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    logging.info(filename)
    return static_file(filename, root='app/static/img')


@app.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='app/static/fonts')


@app.route('/')
@app.route('/user/<nome>')
def index(nome='Desconhecido'):
    return template('index')


@app.route('/usuarios')
def usuarios(db, session):
    if session.get('name'):
        acesso = True
    else:
        acesso = False
    usuarios = db.query(User).all()
    return template('lista-usuarios', usuarios=usuarios, acesso=acesso)


@app.route('/artigo/<id>')
def artigo(id):
    return '<h1>Você está lendo o artigo ' + id + '</h1>'


@app.route('/pagina/<id>/<nome>')
def pagina(id, nome):
    return ('<h1> Você está vendo a página do id ' + id +
            ' com o nome ' + nome)


@app.route('/login')
def login():
    return template('login', sucesso=True)


@app.route('/login', method='POST')
def acao_login(db, session):
    username = request.forms.get('username')
    password = request.forms.get('password')
    password_bytes = str.encode(password)
    existe_username = False
    try:
        user = db.query(User).filter(User.username == username).one()
        existe_username = True
    except Exception:
        existe_username = False
    if existe_username:
        salt_bytes = str.encode(user.salt)
        hashed_bytes = bcrypt.hashpw(password_bytes, salt_bytes)
        hashed = hashed_bytes.decode()
        if user.hashed == hashed:
            session['name'] = username
            return redirect('/usuarios')

    return template('login', sucesso=False)


@app.route('/cadastro')
def acao_cadastro():
    return template('cadastro', existe_username=False)


@app.route('/cadastro', method='POST')
def cadastro(db, session):
    username = request.forms.get('username')
    try:
        db.query(User).filter(User.username == username).one()
        existe_username = True
    except Exception:
        existe_username = False

    if not existe_username:
        password = request.forms.get('password')
        password_bytes = str.encode(password)
        salt_bytes = bcrypt.gensalt()
        hashed_bytes = bcrypt.hashpw(password_bytes, salt_bytes)

        hashed = hashed_bytes.decode()
        salt = salt_bytes.decode()
        new_user = User(username, hashed, salt)
        db.add(new_user)
        session['name'] = username
        return redirect('/usuarios')
    return template('cadastro', existe_username=existe_username)


@app.error(404)
def error(error):
    return template('404.html')
