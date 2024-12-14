class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def get_info(self):
        return "Name: {}, Id: {}".format(self.name,self.id)
class Manager:
    def __init__(self,department):
        self.department=department
    def manage_project(self):
        return "Department: {}".format(self.department)
class Technician:
    def __init__(self,specialization):
        self.specialization=specialization
    def perform_maintenance(self):
        return "Specialization: {}".format(self.specialization)
class TechManager(Employee, Manager, Technician):
    def __init__(self, name, id, department, specialization):
        Employee.__init__(self, name, id)
        Manager.__init__(self, department)
        Technician.__init__(self, specialization)
    team=[]

    def get_info(self):
        return "Name: {}, ID:{}, Department: {}, Specialization: {} ".format(self.name, self.id, self.department, self.specialization)

    def add_employee(self):
        self.team.append(self)
    def get_team_info():
        result=""
        for joiner in TechManager.team:
            result += f'{joiner.get_info()}'
        return result
