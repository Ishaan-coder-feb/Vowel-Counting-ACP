from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/count",methods=["POST"])
def count():
    string=(request.form["string"])
    vowel=0
    for i in string:
        if (i=="a" or i=="e" or i=="i" or i=="o" or i=="u"):
            vowel+=1
    return render_template("index.html",vowel=vowel,string=string)
if __name__=="__main__":
    app.run(debug=True)