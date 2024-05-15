import os
from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from flask_restful import Api, abort

app = Flask(__name__)
app.config["SECRET_KEY"] = 'KOLLOS'
loginmng = LoginManager()
loginmng.init_app(app)


if __name__ == '__main__':
    app.run()
    print('Started')