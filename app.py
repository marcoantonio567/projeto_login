from flask import Flask, render_template , request ,  redirect, url_for

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("/html/login.html")


@app.route("/" , methods=['POST'])
def verificar_login():
    usuario_digitado = request.form['usuario']
    senha_digitada = request.form['senha']

    
    if usuario_digitado in usuarios and senha_digitada  == usuarios[usuario_digitado]:
        # Login bem-sucedido, redireciona para outra página

         return  redirect(url_for('index'))
    else:
        # Login falhou, exibe uma mensagem de erro
        return render_template('/html/login.html', mensagem='Login ou senha incorretos')


@app.route("/index")
def index():
    return render_template("/html/index.html")


usuarios = {
    "saitama":"1234",
    "usuario2":"senha2",
    "user1":"bota00"
}


if __name__ == '__main__':
    app.run(debug=True)
