## pip install pydantic

from pydantic import BaseModel

class Student(BaseModel):
    name:str

new_student={'name':'Omkar'}

student=Student(**new_student)

print(student)


