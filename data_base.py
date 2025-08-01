import sqlite3 as sq
from student import Student

class DataBase:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.create_connection()

    def create_connection(self):
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sq.connect(self.db_file)
            print("Connection established to", self.db_file)
        except sq.Error as e:
            print(f"Error connecting to database: {e}")
        return conn

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            print("Connection closed")
            self.conn = None
        else:
            print("No connection to close")

    def create_table(self):
        """Create a table in the database."""
        try:
            c = self.conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS STUDENTS (
                Name TEXT,
                Age TEXT,
                Grade TEXT
            )""")
            print("Table created successfully")
        except sq.Error as e:
            print(f"Error creating table: {e}")

    def insert_student(self, student: Student):
        """Insert a new student into the STUDENTS table."""
        try:
            c = self.conn.cursor()
            c.execute("INSERT INTO STUDENTS (Name, Age, Grade) VALUES (?, ?, ?)", 
                    (student.name, student.age, student.grade))
            self.conn.commit()
            print("Student inserted successfully.")
        except sq.Error as e:
            print(f"Error inserting student: {e}")

    def insert_multiple_students(self, student_list: list[Student]):
        """Insert multiple Student objects into the STUDENTS table."""
        try:
            c = self.conn.cursor()
            data = [(s.name, s.age, s.grade) for s in student_list]
            c.executemany("INSERT INTO STUDENTS (Name, Age, Grade) VALUES (?, ?, ?)", data)
            self.conn.commit()
            print(f"{len(data)} students inserted successfully.")
        except sq.Error as e:
            print(f"Error inserting multiple students: {e}")

    def fetch_all_students(self):
        """Fetch all records from the STUDENTS table."""
        try:
            c = self.conn.cursor()
            c.execute("SELECT * FROM STUDENTS")
            rows = c.fetchall()
        except sq.Error as e:
            print(f"Error fetching records: {e}")
            rows = []
        return rows

    def delete_student(self, name: str):
        """Delete a student record by name."""
        try:
            c = self.conn.cursor()
            c.execute("DELETE FROM STUDENTS WHERE Name = ?", (name,))
            self.conn.commit()
            if c.rowcount > 0:
                print(f"Deleted student with name: {name}")
            else:
                print(f"No student found with name: {name}")
        except sq.Error as e:
            print(f"Error deleting student: {e}")
    def avgerage_age(self):
        """Calculate the average age of all students."""
        try:
            c = self.conn.cursor()
            c.execute("SELECT AVG(CAST(Age AS REAL)) FROM STUDENTS")
            avg_age = c.fetchone()[0]
            return avg_age if avg_age is not None else 0
        except sq.Error as e:
            print(f"Error calculating average age: {e}")
            return 0
    def update_student(self, name: str, age: str, grade: str):
        """Update a student's age and grade by name."""
        try:
            c = self.conn.cursor()
            c.execute("UPDATE STUDENTS SET Age = ?, Grade = ? WHERE Name = ?", (age, grade, name))
            self.conn.commit()
            if c.rowcount > 0:
                print(f"Updated student {name} successfully.")
            else:
                print(f"No student found with name: {name}")
        except sq.Error as e:
            print(f"Error updating student: {e}")
    def main(self):
        self.create_table()
        std1 = Student(name="Alice", age="20", grade="A")
        self.insert_student(std1)
        #.delete_student("Alice")
        # self.insert_multiple_students([...])
        ewaw = self.fetch_all_students()
        print("All students:", ewaw)
        self.close_connection()

