from pydantic import BaseModel
from typing import Optional
class Student(BaseModel):
    name :str
    age :Optional[str]=None

new_student ={"name":"DIVYANSH"}
student = Student(**new_student)
print(student)