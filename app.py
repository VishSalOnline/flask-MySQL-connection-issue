from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
app = Flask(__name__)
# MySQL Configuration
app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "admin"
app.config["MYSQL_DB"] = "practice"
mysql = MySQL(app)
@app.route("/")
def default():
    return render_template("index.html")
@app.route("/data",methods=["GET","POST"])
def data():
    user_data = request.form
    print(user_data)
    name = user_data["name"]
    rollno = user_data["rollno"]
    course = user_data["course"]
    cursor = mysql.connection.cursor()
    query = "CREATE TABLE IF NOT EXISTS pract(name VARCHAR(20),rollno VARCHAR(20),course VARCHAR(20))"
    cursor.execute(query)
    cursor.execute("INSERT INTO pract(name,rollno,course) values(%s,%s,%s)",(name,rollno,course))
    mysql.connection.commit()
    cursor.close()
    return redirect("/")
if __name__=="__main__":
    app.run(debug=True)