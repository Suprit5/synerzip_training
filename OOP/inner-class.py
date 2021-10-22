class Employee:
    def __init__(self,name,emp_id,lap_name):
        self.name = name
        self.emp_id = emp_id
        self.lap_name=lap_name
        print(f'Name of the employee is "{name}" and employee id is "{emp_id}"')
        #self.lap=self.Laptop(self.lap_name,self.emp_id)


    class Laptop:
        def __init__(self,name,emp_id):
            self.emp_id=emp_id
            self.name=name
            print(f'Employee ID "{self.emp_id}" has "{self.name}" laptop')
emp1=Employee('Rahul',"i306",'lenovo')

emp2=Employee('Suprit',"i304","Dell")


