

from flask import Blueprint, request, render_template, redirect, url_for
from app.services import UserService

user_routes = Blueprint('users', __name__)

# Homepage
@user_routes.route('/')
def index():
    return render_template('index.html')

# View all users
@user_routes.route('/list', methods=['GET'])
def get_users():
    users = UserService.get_users()
    return render_template('users.html', users=users)

# Add a new user (Form)
@user_routes.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        # Call UserService to save the user
        UserService.create_user({"name": name, "email": email, "password": password})

        # Redirect to the users list page after adding a user
        return redirect(url_for('users.get_users'))

    return render_template('add_user.html')

# Edit user (Form)
@user_routes.route('/edit/<user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = UserService.get_user_by_id(user_id)
    
    if not user:
        # Handle case where user doesn't exist
        return redirect(url_for('users.get_users'))
        
    if request.method == 'POST':
        # Extract updated data from the form
        updated_data = {
            "name": request.form.get("name"),
            "email": request.form.get("email")
        }
        
        # Update the user data
        UserService.update_user(user_id, updated_data)
        
        # Redirect to the user list after successful update
        return redirect(url_for('users.get_users'))
        
    # GET request: show the edit form with user data
    return render_template('edit_user.html', user=user)

# Delete user
@user_routes.route('/delete/<user_id>', methods=['GET'])
def delete_user(user_id):
    UserService.delete_user(user_id)
    return redirect(url_for('users.get_users'))