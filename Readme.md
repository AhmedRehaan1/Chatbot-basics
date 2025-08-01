# Student Management System with Chatbot




## Project Overview

This project implements a Student Management System with an interactive chatbot interface, built using Python and Streamlit. It allows for efficient management of student records, including adding, deleting, updating, and fetching student information. The system also provides an administrative dashboard for full control and a user dashboard with a chatbot for querying student data.

## Features

- **User Authentication:** Secure login and registration for both administrators and regular users.
- **Admin Dashboard:**
    - Add new student records (Name, Age, Grade).
    - Delete existing student records.
    - Update student age and grade.
    - View all student records in a tabular format.
- **User Dashboard:**
    - Interactive chatbot for querying student data.
    - Supported queries include:
        - Fetch all students.
        - Calculate average age of students.
        - Count total number of students.
        - Identify the youngest and oldest students.
        - Fetch students by specific grade (e.g., 'A' grade students).
        - Identify the best student (based on grade).
- **SQLite Database:** Persistent storage of student data using `sqlite3`.
- **Modular Design:** Code is organized into separate modules (`Student`, `DataBase`, `ChatBot`, `App`) for better maintainability and scalability.




## Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git
    cd YOUR_REPOSITORY_NAME
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```




## Usage

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2.  **Access the application:**

    Open your web browser and navigate to `http://localhost:8501` (or the address provided by Streamlit).

3.  **Login/Register:**

    -   **Admin Login:** Use `username: admin` and `password: admin123`.
    -   **User Registration:** Register a new user account to access the user dashboard.

4.  **Interact with the system:**

    -   **Admin:** Use the admin dashboard to add, delete, or update student records.
    -   **User:** Use the chatbot interface to query student information using the suggested prompts or your own questions.




## Project Structure

-   `student.py`: Defines the `Student` class.
-   `data_base.py`: Handles SQLite database operations, including creating tables, inserting, fetching, updating, and deleting student records.
-   `chatbot.py`: Implements the `ChatBot` class, which processes user queries and interacts with the `DataBase`.
-   `app.py`: The main Streamlit application, handling user authentication, admin and user dashboards, and integrating the chatbot.
-   `users.json`: Stores user authentication data (created on first run).
-   `students.db`: SQLite database file (created on first run).
-   `logo.png`: Placeholder for the school logo (if used).
-   `requirements.txt`: Lists all Python dependencies required to run the project.



