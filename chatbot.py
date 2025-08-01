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
        elif query.startswith("insert"):
            _, name, age, grade = query.split()
            student = Student(name=name, age=age, grade=grade)
            self.database.insert_student(student)
            status="insertion is successful"
            return status
            
        elif query.startswith("delete"):
            _, name = query.split()
            self.database.delete_student(name)
            status=" successfully deleted"
            return status
        elif query.startswith("update"):
            _, name, age, grade = query.split()
            self.database.update_student(name, age, grade)
            status="updated succesfull"
            return status
        elif query.startswith("average age"):
            avg_age = self.database.avgerage_age()
            print(f"Average age of students: {avg_age}")
            status=avg_age
            return status
        else:
            status="unknown query"
            return status