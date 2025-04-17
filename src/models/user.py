import csv
import os
import hashlib

class User:
    def __init__(self, user_id, username, email, password, role):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password  # Store hashed password for security
        self.role = role

    def __str__(self):
        return f"User({self.user_id}, {self.username}, {self.email}, {self.role})"

    # Getter and Setter methods
    def get_user_id(self):
        return self.user_id
    
    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
    
    def get_role(self):
        return self.role

    def set_password(self, new_password):
        self.password = new_password

    def set_role(self, new_role):
        self.role = new_role

        return f"User({self.user_id}, {self.username}, {self.email}, {self.role})"

    # Getter and Setter methods
    def get_user_id(self):
        return self.user_id
    
    def get_username(self):
        return self.username
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
    
    def get_role(self):
        return self.role

    def set_password(self, new_password):
        self.password = new_password
