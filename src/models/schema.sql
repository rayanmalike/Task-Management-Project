CREATE SCHEMA IF NOT EXISTS project_plan;

SET search_path TO project_plan;


CREATE TYPE task_status AS ENUM ('Pending', 'In Progress', 'Completed');

-- Create User Table (Shared by Managers and Employees)
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    user_ame VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    role VARCHAR(50) NOT NULL
);

-- Create Manager Table (Inherits from User)
CREATE TABLE Manager (
    manager_id INT PRIMARY KEY,
    FOREIGN KEY (manager_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    manager_role VARCHAR(100) 
);

-- Create Employee Table (Inherits from User)
CREATE TABLE Employee (
    employee_id INT PRIMARY KEY,
    FOREIGN KEY (employee_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    employee_role VARCHAR(100)
);

-- Create Project Table
CREATE TABLE Project (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100) NOT NULL,
    description TEXT,
    created_by INT NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    FOREIGN KEY (created_by) REFERENCES Manager(manager_id) ON DELETE SET NULL
);

-- Create Task Table
CREATE TABLE Task (
    task_id INT PRIMARY KEY,
    task_name VARCHAR(100) NOT NULL,
    task_description TEXT,
    task_priority INT,
    task_category task_status NOT NULL DEFAULT 'Pending',
    due_date DATE NOT NULL,
    assigned_to INT,
    created_by INT,
    project_id INT NOT NULL,
    FOREIGN KEY (assigned_to) REFERENCES Employee(employee_id) ON DELETE SET NULL,
    FOREIGN KEY (created_by) REFERENCES Manager(manager_id) ON DELETE SET NULL,
    FOREIGN KEY (project_id) REFERENCES Project(project_id) ON DELETE CASCADE
);


CREATE INDEX idx_task_assigned_to ON Task(assigned_to);
CREATE INDEX idx_task_project_id ON Task(project_id);
CREATE INDEX idx_users_email ON Users(email);




