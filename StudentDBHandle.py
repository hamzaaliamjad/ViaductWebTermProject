from DbHandler import DBHandler


class studentDBHandler(DBHandler):
    def __init__(self, name="", email="", password="", id=0, rollNumber="", resume="", profile_pic="", phoneNo="",
                 address="", degree="", semester=0, cgpa=0.0, current_state="", followers_Count=0, following_count=0,
                 skills_count=0,
                 projects_count=0, call_status=True):
        super(studentDBHandler, self).__init__()
        self.name = name
        self.email = email
        self.password = password
        self.id = id
        self.rollNumber = rollNumber
        self.resume = resume
        self.profile_pic = profile_pic
        self.phoneNo = phoneNo
        self.address = address
        self.degree = degree
        self.semester = semester
        self.cgpa = cgpa
        self.current_state = current_state
        self.followers_count = followers_Count
        self.following_count = following_count
        self.skills_count = skills_count
        self.projects_count = projects_count
        self.call_status = call_status

    def insert(self, name, email, password, rollNo, cgpa, degree, semester, phoneNo, address, gender):
        try:
            query = "INSERT INTO student (S_NAME,S_EMAIL,S_PASSWORD,S_ROLLNO, S_CGPA,S_DEGREE,S_SEMESTER,S_PHONENO,S_ADDRESS,S_GENDER) Values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            args = (name, email, password, rollNo, cgpa, degree, semester, phoneNo, address, gender)
            self.cursor.execute(query, args)
            self.cursor.connection.commit()
        except Exception as e:
            print(str(e))

    def __del__(self):
        super(studentDBHandler, self).__del__()
