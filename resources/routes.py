from .resources import  StudentApi,addSkills

def initialize_routes(api):
    api.add_resource(StudentApi, '/api/student')
    api.add_resource(addSkills,'/api/addSkills')
