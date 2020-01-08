from finalcode import *

@app.route('/')
def index():
    if 'username' in session:
        username  = session['username']
        user_id = session['user_id']
        cur=mydb.cursor()
        cur.execute("INSERT INTO resume_details(user_id) VALUES(%s)",(user_id))
        mydb.commit()
        return render_template('index.html')
    return redirect(url_for("login"))

@app.route('/logout')
def logout():
    session.clear()
    return redirect('login')




@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for("index"))

@app.route('/register',methods=["POST","GET"])
def register():
  use={'user':u}
  print("userss",use)
  db_cursor.execute("select user_id from users ORDER BY user_id DESC LIMIT 1")
  data = db_cursor.fetchall()
  if data == []:
    data=1
    data=str(data)
    data='AI'+data
  else:
    data=data[0][0]
    print("data",data)
    B=int(re.search(r'\d+', data).group(0))
    data=1+B
    data=str(data)
    data='VR'+data
  if request.method == "POST":
    name = request.form['name']
    email = request.form['email']
    username = request.form['username'] 
    number = request.form['number']
    password = request.form['password'].encode('utf-8')
    hash_password = bcrypt.hashpw(password,bcrypt.gensalt())
    user_id = data
    cur=mydb.cursor()
    cur.execute("SELECT * FROM users")
    data =cur.fetchall()
    if len(data) == 0:
      cur=mydb.cursor()
      cur.execute("INSERT INTO users(user_id,user_name,name,email,number,password) VALUES(%s,%s,%s,%s,%s,%s)",
      (user_id,username,name,email,number,hash_password))
      mydb.commit()
      return redirect(url_for("login"))
    else:
      cur=mydb.cursor()
      cur.execute("INSERT INTO users(user_id,user_name,name,email,number,password) VALUES(%s,%s,%s,%s,%s,%s)",
        (user_id,username,name,email,number,hash_password))
      mydb.commit()
      return redirect(url_for("login"))
  return render_template("register.html",user=use)

@app.route('/login',methods=["POST","GET"])
def login():
  error = None
  if request.method == "POST":
    username = request.form['username']
    password = request.form['password'].encode('utf-8')
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT * FROM users WHERE username=%s",(username,))
    user = cur.fetchone() 

    if user != None:
      if bcrypt.hashpw(password,user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
      #Create a user login session
        session['user_id'] = user['user_id']
        session['email'] = user['email']
        session['number'] = user['number']
        session['name'] = user['name']
        session['username'] = user['username']
        return redirect(url_for("index"))
      else:
        error = 'Invalid  Password. Please try again!'
        return render_template("login.html",error=error) 
    else:
      error = 'Invalid Email Address. Please try again!'
      return render_template("login.html",error=error)
  else:     
    return render_template('login.html')