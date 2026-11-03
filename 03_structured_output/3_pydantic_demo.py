from pydantic import BaseModel


class Student(BaseModel):
    name: str = "Muhammad Shahzad"


new_student = {
   
}

new_student_obj = Student(**new_student)

print(new_student_obj)