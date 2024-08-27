from sqlmodel import Field, SQLModel, Session, create_engine, select
from typing import Optional

class Student(SQLModel, table = True):
    id: Optional[int] = Field(default = None, primary_key = True)
    name: str
    age: int
    class_name: str

student_1 = Student(name = "Daniel", age = 33, class_name = "B")
student_2 = Student(name = "Balázs", age = 34, class_name = "B")
student_3 = Student(name = "Viola", age = 34, class_name = "C")

engine = create_engine("sqlite:///students.db")

SQLModel.metadata.create_all(engine)

#with Session(engine) as session:
#    session.add(student_1)
#    session.add(student_2)
#    session.add(student_3)
#    session.commit()

with Session(engine) as session:
    statement = select(Student).where(Student.name == "Daniel")
    student = session.exec(statement).first()
    print(student)
