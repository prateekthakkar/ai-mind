from flask import Flask,render_template,url_for,request,redirect,session
import os
import mysql.connector
import bcrypt
from werkzeug.utils import secure_filename

import re

app = Flask(__name__)
# login_manager = LoginManager(app)
app.secret_key = 'super-secret-key'

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin1234",
  database="video_resume",
  use_pure = True
)


mycursor = mydb.cursor()

from views import *
if __name__ == "__main__":
	app.run()