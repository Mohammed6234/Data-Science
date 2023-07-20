class Employee:
    def __init__(self, emp_id, emp_name):
        self.id = emp_id
        self.name = emp_name

# Creating an Employee object
emp = Employee(1, "coder")

# Accessing the attributes
print("Employee ID:", emp.id)
print("Employee Name:", emp.name)

# Deleting the id attribute using del
del emp.id

# Attempting to access the deleted id attribute will raise an AttributeError
try:
    print("Employee ID after deletion:", emp.id)
except AttributeError as e:
    print("AttributeError:", e)

# Deleting the entire emp object using del
del emp

# Attempting to access the deleted emp object will raise a NameError
try:
    print("Employee Name after deletion:", emp.name)
except NameError as e:
    print("NameError:", e)
