from Employee import Employee,Manager,Technician,TechManager

class Main:
    employee=Employee('Zorina Oksana Viktrovna','123321')
    manager=Manager('Finance Department')
    technician=Technician('Financial analysys')
    tech_manager=TechManager(employee.name, employee.id, manager.department, technician.specialization)
    employee1 = Employee('Garchenko Alina Vasilievna', '321123')
    manager1 = Manager('Transport Department')
    technician1 = Technician('Logistika')
    tech_manager1 = TechManager(employee1.name, employee1.id, manager1.department, technician1.specialization)
    TechManager.add_employee(tech_manager)
    TechManager.add_employee(tech_manager1)
    print(TechManager.get_info(tech_manager))
    print(TechManager.get_team_info())
