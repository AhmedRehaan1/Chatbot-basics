import streamlit as st
import json
import sqlite3
from data_base import DataBase 
from chatbot import ChatBot
from student import Student 

# Initialize database and chatbot
db = DataBase("students.db")
chatbot = ChatBot("students.db")

# User data storage
USERS_FILE = "users.json"

# Load users from JSON
def load_users():
    try:
        with open(USERS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"admin": {"password": "admin123", "role": "admin"}, "users": {}}

# Save users to JSON
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f)

# --- Authentication Pages ---
def login_page():
    st.title("Student System Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        users = load_users()
        if username == "admin" and users["admin"]["password"] == password:
            st.session_state["role"] = "admin"
            st.session_state["page"] = "dashboard"
            st.success("Admin login successful!")
        elif username in users["users"] and users["users"][username]["password"] == password:
            st.session_state["role"] = "user"
            st.session_state["page"] = "dashboard"
            st.success("User login successful!")
        else:
            st.error("Invalid credentials")

def register_page():
    st.title("New User Registration")
    username = st.text_input("Choose Username")
    password = st.text_input("Choose Password", type="password")
    
    if st.button("Register"):
        users = load_users()
        if username in users["users"]:
            st.warning("Username already exists")
        else:
            users["users"][username] = {"password": password, "role": "user"}
            save_users(users)
            st.success("Registration successful! Please login.")

# --- Dashboard Pages ---
def admin_dashboard():
    st.title("Admin Dashboard")
    
    # Student Management
    st.header("Student Management")
    name = st.text_input("Student Name")
    age = st.number_input("Age", min_value=1)
    grade = st.text_input("Grade (A-F)")
    
    
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Add Student"):
            student = Student(name=name, age=age, grade=grade)
            db.insert_student(student)

    with col2:
        if st.button("Delete Student"):
            db.delete_student(name)
    with col3:
        if st.button("Update Student"):
            db.update_student(name, age, grade)
    
    students = db.fetch_all_students()
    st.table(students)

def user_dashboard():
    st.title("User Dashboard")
    st.header("Chat with Student Assistant")
    
    # Chatbot Interface
    user_input = st.text_input("Ask a question about students:")
    if user_input:
        response = chatbot.query(user_input)
        st.text_area("Chatbot Response", value=response, height=100)
        

# --- Main App Flow ---
def main():
    if "page" not in st.session_state:
        st.session_state["page"] = "login"
    
    # Navigation
    if st.session_state["page"] == "login":
        login_page()
        if st.button("Go to Register"):
            st.session_state["page"] = "register"
    elif st.session_state["page"] == "register":
        register_page()
        if st.button("Back to Login"):
            st.session_state["page"] = "login"
    elif st.session_state["page"] == "dashboard":
        if st.session_state["role"] == "admin":
            admin_dashboard()
        else:
            user_dashboard()
        if st.button("Logout"):
            st.session_state.clear()
            st.experimental_rerun()

if __name__ == "__main__":
    main()