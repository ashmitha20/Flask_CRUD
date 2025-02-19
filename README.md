# 🚀 Flask MongoDB CRUD Application  

A simple yet powerful **Flask-based CRUD (Create, Read, Update, Delete) application** that manages user data using **MongoDB** as the database. The application allows users to **add, view, update, and delete** records efficiently.  

---

## 📌 Features  
- ✅ **Create Users** - Add users with name, email, and securely hashed passwords.  
- ✅ **Read Users** - View all users in an elegant table format.  
- ✅ **Update Users** - Modify user details while maintaining data integrity.  
- ✅ **Delete Users** - Remove users when they are no longer needed.  
- ✅ **Dockerized Deployment** - Run the app effortlessly with Docker.  
- ✅ **REST API Support** - Perform CRUD operations using HTTP requests.  

---

## 🛠 Technology Stack  

| Technology       | Description                      |
|-----------------|----------------------------------|
| **Backend**     | Flask (Python)                   |
| **Database**    | MongoDB (NoSQL)                  |
| **Authentication** | Bcrypt for password hashing  |
| **Frontend**    | HTML5, CSS3, Jinja2 Templates    |
| **Deployment**  | Docker Containerization         |

---

## 📂 Project Structure  

```bash
flask-mongo-crud/
│── app/
│   ├── __init__.py        # Initializes Flask app
│   ├── config.py          # App configuration (DB connection)
│   ├── models.py          # MongoDB models
│   ├── routes.py          # API endpoints & HTML views
│   ├── services.py        # Business logic for CRUD operations
│   ├── templates/         # HTML templates
│   ├── static/            # CSS and static files
│── Dockerfile             # Docker setup
│── docker-compose.yml     # Container management
│── requirements.txt       # Python dependencies
│── run.py                 # Main entry point for the Flask app
│── README.md              # Project documentation
