from StudentDBHandle import studentDBHandler


def signUP(name, email, password, rollNo, cgpa, degree, semester, phoneNo, address, gender):
    try:
        sDBHandler = studentDBHandler()
        sDBHandler.insert(name, email, password, rollNo, cgpa, degree, semester, phoneNo, address, gender)
        return "Created"
    except Exception as e:
        return (str(e))
def showInfoData(id,cursor):
    try:
        query = "select S_NAME,S_EMAIL,S_ROLLNO,S_CGPA,S_DEGREE,S_SEMESTER,S_PHONENO,S_ADDRESS,S_GENDER from student where S_ID=%s"
        args=(id)
        cursor.execute(query,args)
        data=cursor.fetchall()
        return data
    except Exception as e:
        print(str(e))

def getID(email,password,cursor):
    try:
        query = "select S_ID from student where S_PASSWORD=%s and S_EMAIL=%s"
        args = (password, email)
        cursor.execute(query, args)
        dataS = cursor.fetchall()
        if (len(dataS) > 0):
            return dataS[0][0]
        query = "select A_ID from admin where A_PASSWORD=%s and A_EMAIL=%s"
        args = (password, email)
        cursor.execute(query, args)
        dataA = cursor.fetchall()
        if (len(dataA) > 0):
            return dataA[0][0]
        return -1
    except Exception as e:
        print(str(e))
def checkStudent(id,cursor):
    try:
        query="select S_ID from student where S_ID=%s"
        args=(id)
        cursor.execute(query,args)
        data=cursor.fetchall()
        if len(data) >0:
            return True
        else:
            return False
    except Exception as e:
        print(str(e))

def loginDB(email,password,cursor):
    # emailCheck=checkEmail(email,cursor)
    # if emailCheck==0:
    #     return ("Email doesn't Exists!!")
    userId = getID(email, password, cursor)
    # if checkTeacher(userId,cursor):
    #     return "Teacher"
    if checkStudent(userId,cursor):
        return "Student"
    else:
        return "admin"
    return "Incorrect Password"
def getStudentsCount(cursor):
    try:
        query = "select * from student"
        cursor.execute(query)
        dataS = cursor.fetchall()
        return len(dataS)
    except Exception as e:
        print(str(e))
def getStudentCardData(cursor):
    try:
        query = "select S_NAME,S_FOLLOWERS_COUNT,S_CGPA,S_SKILLS_COUNT,S_PROJECT_COUNT from student"
        cursor.execute(query)
        dataS = cursor.fetchall()
        if (len(dataS) > 0):
            return dataS
        return -1
    except Exception as e:
        print(str(e))
def getFeedData(cursor):
    try:
        query = "select * from Feed"
        cursor.execute(query)
        dataF = cursor.fetchall()
        if (len(dataF) > 0):
            return dataF
        return -1
    except Exception as e:
        print(str(e))

def getStudentFeedData(cursor,id):
    try:

        query = "select S_NAME, S_ROLLNO from student where S_ID=%s"
        args=(id)
        cursor.execute(query,args)
        dataS = cursor.fetchall()
        if (len(dataS) > 0):
            return dataS[0]
        return -1
    except Exception as e:
        print(str(e))