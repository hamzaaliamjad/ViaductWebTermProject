from flask import request, Response, jsonify,session
from StudentDBHandle import studentDBHandler
from DbHandler import DBHandler
from flask_restful import Resource
from datetime import date
from database.models import Student

systemDB = DBHandler()
cursor = systemDB.conn.cursor()

class StudentApi(Resource):
    def get(self):
        try:
            query = "select S_NAME,S_EMAIL,S_ROLLNO,S_CGPA,S_DEGREE,S_SEMESTER,S_PHONENO,S_ADDRESS,S_GENDER from student where S_ID=%s"
            args = (id)
            cursor.execute(query, args)
            data = cursor.fetchall()
            dict={'S_NAME':data[0][0],'S_EMAIL':data[0][1],'S_ROLNO':data[0][2],'S_CGPA':data[0][3],'S_DEGREE':data[0][4],
                    'S_SEMESTER':data[0][5],'S_PHONENO':data[0][6],'S_ADDRESS':data[0][7],'S_GENDER':data[0][8]}
            return Response(dict)
        except Exception as e:
            print(str(e))
    def post(self):
        data=request.get_json()
        print("here")
        print(data)
        jobData=(())
        try:
            id = session.get("id")
            print(id)
            queryGet="select S_CURRENT_STATE,S_CURRENT_PLACE from student where S_ID=%s"
            argsGet=(id)
            cursor.execute(queryGet, argsGet)
            jobData=cursor.fetchall()
        except Exception as e:
            print(e)
        try:
            query = "UPDATE student SET S_NAME=%s,S_EMAIL=%s,S_CGPA=%s,S_DEGREE=%s,S_SEMESTER=%s,S_PHONENO=%s,S_ADDRESS=%s,S_GENDER=%s,S_INTRODUCTION=%s,S_CURRENT_STATE=%s,S_CURRENT_PLACE=%s where S_ID=%s"
            print(data['intro'])
            print("-----------------")
            args = (data['nm'],data['em'],data['cgpa'],data['degree'],data['sem'],data['phno'],data['address'],data['gender'],data['intro'],data['inlineRadioOptions'],data['jobPlace'],id)
            cursor.execute(query, args)
            cursor.connection.commit()
            if(jobData[0][0] != data['inlineRadioOptions'] or jobData[0][1] != data['jobPlace']):
                tDate = date.today()
                queryInsert="INSERT INTO FEED (P_TYPE,F_TITLE,S_ID,P_DATE) values(%s,%s,%s,%s)"
                argsInsert=(jobData[0][0],jobData[0][1],id,tDate)
                print("**********************")
                print(argsInsert)
                cursor.execute(queryInsert, argsInsert)
                cursor.connection.commit()

            return {'S_NAME':data[0][0],'S_EMAIL':data[0][1],'S_ROLNO':data[0][2],'S_CGPA':data[0][3],'S_DEGREE':data[0][4],
                    'S_SEMESTER':data[0][5],'S_PHONENO':data[0][6],'S_ADDRESS':data[0][7],'S_GENDER':data[0][8]}
        except Exception as e:
            print(str(e))

class addSkills(Resource):
    def get(self):
        pass
    def post(self):
        data = request.get_json()
        print("here")
        print(data)
        try:
            id = session.get("id")
            print(id)
            queryGet = "INSERT INTO skills (SK_NAME,SK_LEVEL,SK_EXPERIENCE,SK_INTEREST,S_ID) values(%s,%s,%s,%s,%s)"
            argsGet = (data['soft_skill'],data['soft_subskillset'],data['soft_subskill_year'],data['soft_skill_intrest_level'],id)
            cursor.execute(queryGet, argsGet)
            cursor.connection.commit()
        except Exception as e:
            print(e)
