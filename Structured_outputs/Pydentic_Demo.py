from pydantic import BaseModel,Field

class Student(BaseModel):
    name:  str = 'nachiket'
    cgpa: float = Field(gt=0, lt=10, default=6, description="rank of the student")

new_student: Student = {'cgpa': '12'}

student = Student(**new_student)
print(student.model_dump_json('name'))