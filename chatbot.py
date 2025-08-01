from data_base import DataBase
from student import Student
import streamlit as st
class ChatBot:
    def __init__(self, db_name):
        self.db_name = db_name
        self.database = DataBase(db_name)

    def query(self, query:str):
        """Process a query and interact with the database."""
        if query == "fetch all students":
            list_of_tuples = self.database.fetch_all_students()
        
            return list_of_tuples
        # elif query.startswith("insert"):
        #     _, name, age, grade = query.split()
        #     student = Student(name=name, age=age, grade=grade)
        #     self.database.insert_student(student)
        #     status="insertion is successful"
        #     return status
            
        # elif query.startswith("delete"):
        #     _, name = query.split()
        #     student = Student(name=name)
        #     self.database.delete_student(student)
        #     status=" successfully deleted"
        #     return status
        # elif query.startswith("update"):
        #     _, name, age, grade = query.split()
        #     student = Student(name=name, age=age, grade=grade)
        #     self.database.insert_student(student)
        #     status="updated succesfull"
        #     return status
        elif query.startswith("what is the average age?"):
            avg_age = self.database.avgerage_age()
            print(f"Average age of students: {avg_age}")
            status=avg_age
            return status
        elif query.startswith("please count students"):
            count = self.database.count_students()
            print(f"Total number of students: {count}")
            status=count
            return status
        elif query.startswith("who is the youngest student?"):
            youngest = self.database.youngest_student()
            print(f"Youngest student: {youngest}")
            status=youngest
            return status
        elif query.startswith("who is the oldest student?"):
            oldest = self.database.oldest_student()
            print(f"Oldest student: {oldest}")
            status=oldest
            return status
        elif query.startswith("fetch A grade students"):
            a_students = self.database.fetch_students_by_grade("A")
            print(f"Students with A grade: {a_students}")
            status=a_students
            return status
        elif query.startswith("who is the best student?"):
            best_student = self.database.best_student()
            print(f"Best student: {best_student}")
            status=best_student
            return status
        else:
            status="unknown query"
            return status