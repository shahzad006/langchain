from pydantic import BaseModel
from typing import Optional


class Student(BaseModel):
    name: str = "Muhammad Shahzad"
    age: Optional[int] = None


new_student = {
   
}

new_student_obj = Student(**new_student)

print(new_student_obj)
print(new_student_obj.age) 