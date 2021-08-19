class Student:
    school_name='St. Anthony\'s High School'
    def __init__(self,sub_1,sub_2,sub_3):
        self.sub_1=sub_1
        self.sub_2=sub_2
        self.sub_3=sub_3
    
    def avg(self):
        return (self.sub_1+self.sub_2+self.sub_3)/3
    
    def get_sub_1(self):
        return self.sub_1        
    
    def set_marks(self):
        self.sub_1=39

    @classmethod
    def name(cls):
        print(f'the school name is {cls.school_name}')

    @staticmethod
    def info():
        print ('Hi how are you all today welcome')

student_1=Student(45,32,12)
student_2=Student(33,42,32)
student_3=Student(15,36,22)

print(student_1.avg())
student_2.set_marks()
print(student_2.avg())
print(student_3.avg())

print(f'{student_1.get_sub_1()}')

Student.name()
Student.info()