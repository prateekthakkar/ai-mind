mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="admin1234",
  database="video_resume",
  use_pure = True
)

app.secret_key = 'super-secret-key'