import os
from allFunctions import *
from flask import Flask, jsonify,request, render_template,make_response,redirect,session
from flask_restful import Api,Resource
from database import db
from resources import routes
from DbHandler import  DBHandler

UPLOAD_FOLDER_PROJECTS = "C:\\Users\\imham\\PycharmProjects\\webTermProject\\Projects"
UPLOAD_FOLDER_PROFILE_PICTURES = "C:\\Users\\imham\\PycharmProjects\\webTermProject\\profile_pictures"

app = Flask(__name__)
app.config.from_object("config")
app.secret_key=app.config["SECRET_KEY"]
app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost:27017/viaduct'
}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER_PROJECTS

api=Api(app)
db.initialize_db(app)
routes.initialize_routes(api)


@app.route('/')
def start():
    return render_template("index.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/loginHandle',methods=["GET","POST"])
def loginHandler():
    loginVal=""
    userId=0
    if request.method == "POST":
        pwd = request.form["pwd"]
        em = request.form["em"]
        log = False
        systemDB = DBHandler()
        cursor = systemDB.conn.cursor()
        loginVal = loginDB(em, pwd, cursor)
        userId = getID(em, pwd, cursor)
        session['id']=userId
    if(loginVal=="Student"):
        return redirect('/feed')
    if(loginVal=="admin"):
        return redirect('/admin')
    else:
        return render_template("login.html")

@app.route('/admin')
def admin():
    systemDB = DBHandler()
    cursor = systemDB.conn.cursor()
    studentCount=getStudentsCount(cursor)
    return render_template("admin.html",count=studentCount)
@app.route('/feed')
def feed():
    systemDB = DBHandler()
    cursor = systemDB.conn.cursor()
    # id=request.cookies.get("id")
    # print(id)
    data = getFeedData(cursor)
    dataS = []
    print(data)
    count = len(data)
    print("Count=",count)
    for i in range(0, count):
        dataStudent = getStudentFeedData(cursor, data[i][3])
        print(dataStudent)
        dataS.append(dataStudent)
    print(dataS)
    print(dataS[1][1])
    dataS.reverse()
    newData = []
    for k in reversed(data):
        newData.append(k)
    print(newData)
    return render_template("feed.html", count=count, data=newData, dataS=dataS)

@app.route('/signupStudent')
def signUPStudent():
    return render_template("signUpStudent.html")



@app.route('/signupHandle',methods=["GET","POST"])
def signupHandle():
    signVal=""
    if request.method=="POST":
        nm=request.form["nm"]
        rn=request.form["rn"]
        pwd=request.form["pwd"]
        em=request.form["em"]
        cgpa=request.form["cgpa"]
        degree=request.form["RadioOptions"]
        semester=request.form["semester"]
        phoneNo=request.form["pn"]
        address=request.form["add"]
        gender=request.form["inlineRadioOptions"]
        signVal = signUP(nm, em, pwd, rn, cgpa, degree, semester, phoneNo, address, gender)
    signup= False
    if signVal == "Created":
        signup=True
    if signup== True:
        return render_template("login.html")
    else:
        return render_template("login.html")

@app.route('/studentcards')
def studentCardData():
    systemDB = DBHandler()
    cursor = systemDB.conn.cursor()
    #id=request.cookies.get("id")
    #print(id)
    data= getStudentCardData(cursor)
    print(data)
    count=len(data)
    print(count)
    return render_template("studentCardView.html",count=count,data=data)

@app.route('/editInfo')
def editInfo():
    systemDB = DBHandler()
    cursor = systemDB.conn.cursor()
    id = session.get("id")
    dataUser= showInfoData(int(id), cursor)

    print(dataUser)
    return render_template("editInfoS.html",data=dataUser)


@app.route('/addSkills')
def addSkills():
    return  render_template("addSkills.html")
# @app.route('/editInfoHandle' ,methods=["GET","POST"])
# def editInfoHandle():
#     if request.method == "POST":
#         nm=request.form["nm"]
#         print(nm)
#
#     return render_template("feed.html")

@app.route('/addProjects')
def addProjects():
    return render_template("addProjects.html")
@app.route('/addProjectsHadle',methods=["GET","POST"])
def addProjectsHandle():
    if request.method == 'POST':
        if 'project' not in request.files:
            return 'there is no file1 in form!'
        file1 = request.files['project']
        id=session.get("id")
        nameFile=file1.filename.split(".")
        newName=nameFile[0]+str(id)+"."+nameFile[1]
        path = os.path.join(app.config['UPLOAD_FOLDER'], newName)
        print(path)
        file1.save(path)
    return redirect("/editInfo")

@app.route('/studentView')
def studentView():
    return render_template("viewInfo.html")


if __name__ == '__main__':
    app.run()
