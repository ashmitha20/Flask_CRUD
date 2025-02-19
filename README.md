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

```

## 🚀 Running the Application
Using Docker

Clone the repository
```bash
git clone https://github.com/yourusername/flask-mongo-crud.git
cd flask-mongo-crud
```

Start the containers
```bash
docker-compose up -d
```

Access the application
Web Interface: http://localhost:5000
API Endpoints: http://localhost:5000/api/v1/users



Manual Setup

Clone the repository
```bash
git clone https://github.com/yourusername/flask-mongo-crud.git
cd flask-mongo-crud
```

Set up virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

Configure MongoDB connection

Edit app/config.py with your MongoDB URI


Run the application
```bash
python run.py
```

Access the application

Web Interface: http://localhost:5000
API Endpoints: http://localhost:5000/api/v1/users

---

### 📡 API Testing with Postman
Setup Postman Collection

Download Postman
Import the provided collection file: Flask_MongoDB_CRUD.postman_collection.json
Or create a new collection with the following endpoints:

Testing in Postman
Create a user:

Select POST method
Enter URL: http://localhost:5000/api/v1/users
Go to "Body" tab, select "raw" and "JSON"
Add the JSON payload with user details:
```json{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepass123"
}
```

Click "Send"


Get all users:

Select GET method
Enter URL: http://localhost:5000/api/v1/users
Click "Send"


Get a specific user:

Select GET method
Enter URL: http://localhost:5000/api/v1/users/{user_id}
Click "Send"


Update a user:

Select PUT method
Enter URL: http://localhost:5000/api/v1/users/{user_id}
Add the JSON with updated fields:
```json
{
  "name": "John Smith",
  "email": "john.smith@example.com"
}
```

Click "Send"


Delete a user:

Select DELETE method
Enter URL: http://localhost:5000/api/v1/users/{user_id}
Click "Send"



Sample API Responses
Successful User Creation (201 Created)
```json
{
  "message": "User created successfully",
  "user_id": "65f3b2c8a97e5d12340abcde"
}
```

Successful User Retrieval (200 OK)
```json
{
  "users": [
    {
      "_id": "65f3b2c8a97e5d12340abcde",
      "name": "John Doe",
      "email": "john@example.com",
      "created_at": "2025-02-19T10:15:23.456Z"
    }
  ]
}
```
