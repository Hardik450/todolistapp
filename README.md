# To-Do List App

## Overview
This is a simple yet powerful **To-Do List App** built using **Django**, a high-level Python web framework. The application allows users to **register, log in, and manage their tasks** efficiently.

## Features
- **User Authentication**: Register and log in securely.
- **Task Management**: Add, update, and delete tasks.
- **Intuitive UI**: A user-friendly interface for easy task tracking.
- **Persistent Data**: Tasks are stored in a database for long-term access.
- **Hosted on PythonAnywhere**: Accessible online for convenience.

## Live Demo
You can access the app here: **http://kingkong.pythonanywhere.com/todolistapp/**

## Installation & Setup
To run the project locally, follow these steps:

### Prerequisites
- Python (>=3.8 recommended)
- Django (Install using `pip install django`)
- Git (for cloning the repository)

### Steps to Run Locally
1. **Clone the repository**
   ```sh
   git clone https://github.com/Hardik450/todolistapp.git
   ```
2. **Navigate to the project directory**
   ```sh
   cd todolistapp
   ```
3. **Create a virtual environment and activate it**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
4. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```
5. **Run migrations**
   ```sh
   python manage.py migrate
   ```
6. **Start the development server**
   ```sh
   python manage.py runserver
   ```
7. Open your browser and visit `http://127.0.0.1:8000/` to use the app.

## Deployment on PythonAnywhere
The app is hosted on **PythonAnywhere**, a cloud-based Python hosting platform. The deployment process involves:
- Uploading the project files
- Setting up a virtual environment
- Configuring WSGI and static files
- Mapping the domain to the application

## Contributing
Feel free to fork the repository and submit pull requests if you'd like to contribute!

## License
This project is licensed under the **MIT License**.

---

📧 **Contact:** If you have any questions, feel free to reach out via **[Your Email or GitHub Profile]**.

