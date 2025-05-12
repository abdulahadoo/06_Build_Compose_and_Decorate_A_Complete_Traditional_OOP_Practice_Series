class Student:
    def __init__(self,name,marks):
        self.name = name 
        self.mark = marks

    def display(self):
        print("Student Name: ",self.name)
        print("Marks",self.marks)

# Example of 

Student1 = Student("Abdul ahad", 95)
Student1.display()

Student2 = Student("Adii",96)
Student2.display()