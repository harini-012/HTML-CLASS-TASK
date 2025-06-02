from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route("/",methods=['GET','POST'])
def form():
    if request.method=='POST':
        
        name=request.form['name']
        email=request.form['email']
        gender=request.form.get("gender")
        year=request.form.get("year")
        skills=request.form.get("skills")
        comments=request.form.get("comments")
        
        return f"Received : <br> Name:{name} <br> Email:{email} <br> Gender:{gender}<br> Year:{year}<br> Skills:{skills}<br> Comments:{comments}"
    return render_template("02.06.2025.html")


if __name__=='__main__':
    app.run(debug=True)
        
        
