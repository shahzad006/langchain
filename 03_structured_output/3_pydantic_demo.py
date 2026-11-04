from pydantic import BaseModel , Field
from typing import Optional


class Student(BaseModel):
    name: str = "Muhammad Shahzad"
    age: Optional[int] = None
    cgps: float = Field(..., gt=0 , lt=10, description="Cumulative Grade Point Score must be greater than 0 and less than 5.0")


new_student = {
    "name": "Ali Raza",
    "age": 20,
    "cgps": 3
}

new_student_obj = Student(**new_student)

print(new_student_obj)
print(new_student_obj.age) 
print(new_student_obj.cgps)