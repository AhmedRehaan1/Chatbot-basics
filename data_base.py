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

    def delete_student(self, student: Student):
        """Delete a student record by student object name."""
        try:
            c = self.conn.cursor()
            c.execute("DELETE FROM STUDENTS WHERE Name = ?", (student.name,))
            self.conn.commit()
            if c.rowcount > 0:
                print(f"Deleted student with name: {student.name}")
            else:
                print(f"No student found with name: {student.name}")
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
    def best_student(self):
        """Fetch the student with the highest grade."""
        try:
            c = self.conn.cursor()
            c.execute("SELECT Name, Grade FROM STUDENTS ORDER BY Grade DESC LIMIT 1")
            best_student = c.fetchone()
            return best_student if best_student else None
        except sq.Error as e:
            print(f"Error fetching best student: {e}")
            return None
    def fetch_students_by_grade(self, grade: str):
        """Fetch all students with a specific grade."""
        try:
            c = self.conn.cursor()
            c.execute("SELECT * FROM STUDENTS WHERE Grade = ?", (grade,))
            students = c.fetchall()
            return students
        except sq.Error as e:
            print(f"Error fetching students by grade {grade}: {e}")
            return []
    def oldest_student(self):
        """Fetch the oldest student."""
        try:
            c = self.conn.cursor()
            c.execute("SELECT Name, Age FROM STUDENTS ORDER BY CAST(Age AS REAL) DESC LIMIT 1")
            oldest_student = c.fetchone()
            return oldest_student if oldest_student else None
        except sq.Error as e:
            print(f"Error fetching oldest student: {e}")
            return None
    def youngest_student(self):
        """Fetch the youngest student."""
        try:
            c = self.conn.cursor()
            c.execute("SELECT Name, Age FROM STUDENTS ORDER BY CAST(Age AS REAL) ASC LIMIT 1")
            youngest_student = c.fetchone()
            return youngest_student if youngest_student else None
        except sq.Error as e:
            print(f"Error fetching youngest student: {e}")
            return None
    def average_grade(self):
        """Calculate the average grade of all students."""
        try:
            c = self.conn.cursor()
            c.execute("SELECT AVG(CASE Grade WHEN 'A' THEN 4 WHEN 'B' THEN 3 WHEN 'C' THEN 2 WHEN 'D' THEN 1 ELSE 0 END) FROM STUDENTS")
            avg_grade = c.fetchone()[0]
            return avg_grade if avg_grade is not None else 0
        except sq.Error as e:
            print(f"Error calculating average grade: {e}")
            return 0
    def count_students(self):
        """Count the total number of students."""
        try:
            c = self.conn.cursor()
            c.execute("SELECT COUNT(*) FROM STUDENTS")
            count = c.fetchone()[0]
            return count
        except sq.Error as e:
            print(f"Error counting students: {e}")
            return 0
    def update_student(self, student: Student):
        """Update a student's age and grade by student object name."""
        try:
            c = self.conn.cursor()
            c.execute(
                "UPDATE STUDENTS SET Age = ?, Grade = ? WHERE Name = ?",
                (student.age, student.grade, student.name)
            )
            self.conn.commit()
            if c.rowcount > 0:
                print(f"Updated student {student.name} successfully.")
            else:
                print(f"No student found with name: {student.name}")
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

