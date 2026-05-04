from flask import Flask, render_template , request ,  redirect, url_for


#create app instance
app = Flask(__name__)

#define routes
@app.route("/")
def login():
    return render_template("/html/login.html")

#verify login
@app.route("/" , methods=['POST'])
def verify_login():
    user_typing = request.form['usuario']
    password_typing = request.form['senha']

    
    if user_typing in users and password_typing  == users[user_typing]:
        # login success, redirect to index page
         return  redirect(url_for('index'))
    else:
        # login failed, show error message
        return render_template('/html/login.html', mensagem='Login ou senha incorretos')

#define index route
@app.route("/index")
def index():
    return render_template("/html/index.html")

#define users
users = {
    #username:password
    "saitama":"1234",
    "usuario2":"senha2",
    "user1":"bota00"
}

#define app run
if __name__ == '__main__':
    app.run(debug=True)
