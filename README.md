# 343-Project
# Group Project Management System

A Python-based task management system designed for group projects with role-based access control and CSV data persistence.

## Features

- User Management
    - Role-based system (Boss, Manager, Employee)
    - User creation and deletion
    - CSV-based data persistence
- Task Management
    - Create, update, and delete tasks
    - Assign tasks to users
    - Track task status
    - Task commenting system
- Comment System
    - Add comments to tasks
    - View task comment history
    - Timestamp tracking for comments

## System Architecture

The system implements the Singleton pattern for core controllers:

- UserController - Manages user operations and persistence
- TaskManager - Handles task operations and comment management

## Data Storage

All data is stored in CSV files:

- managers.csv - Stores manager information
- employees.csv - Stores employee information
- task_comments.csv - Stores task comments
- users.csv - Store login users info
- projects.csv - Store project info
- tasks.csv - Store task info

## User Roles

- Boss: Can manage both managers and employees
- Manager: Can create and assign tasks
- Employee: Can view and update assigned tasks

## Getting Started

1. Ensure all required CSV files are in the project directory
2. Run the main application file
3. Log in with appropriate credentials

## Dependencies

Standard Python libraries:

- csv - For data persistence
- datetime - For timestamp management

## Error Handling

The system includes comprehensive error handling for:

- File operations
- User management operations
- Task management operations
- Comment system operations
