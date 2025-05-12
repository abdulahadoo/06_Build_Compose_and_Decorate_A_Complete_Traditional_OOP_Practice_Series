class Employee:
    name = "Ahad"

    _salary = 30000

    _ssn = "12345-56425-1"

emp = Employee()
print("Name:",emp.name)

print("Salary:",emp._salary)

try:
    print("SSN:",emp.__ssn)
except AttributeError as e:
    print("Error:",e)

print("SSN (Via name mangling):",emp._Emplyee__ssn)    