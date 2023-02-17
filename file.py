from flask import Flask,session,render_template,redirect,url_for,request
from datetime import timedelta
app = Flask(__name__)
app.secret_key ="heelo"

@app.route("/")
def home():

    return "hi"

@app.route("/login",methods=["POST","GET"])

def login():
      if request.method =="POST":
          user=request.form["nm"]
          session["user"]=user
          return redirect(url_for("user"))
      else:
          if "user" in session:
              return redirect(url_for("user"))
          return render_template("login.html")
@app.route("/user")
def user():
    if "user" in session:
        user=session["user"]
        return redirect(url_for("prof"))
    else :
        return redirect(url_for("login"))
@app.route("/prof")
def prof():
    return render_template("profile.html")

   
   
if __name__=="__main__":
    app.run(debug=True)