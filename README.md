# Project Management Web Application

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)

## Description

This is a web-based project management tool developed for a school assignment. It allows users to manage projects, tasks, and documents in a collaborative environment. The application is built using Python's Flask framework and integrates with a MySQL database for data storage. Additionally, it leverages the Mammoth library for converting documents to HTML.

## Features

- User authentication and role-based access control (login and user roles).
- Project and task management with status tracking (e.g., started, in progress, completed).
- File upload and document conversion to HTML for easy viewing.
- Display of project and task details, including user-specific tasks.
- Integration with a MySQL database for data persistence.


## Project Background

This project was developed as part of a school assignment focused on learning project management principles. The assignment aimed to simulate the real-world scenario of initiating a project, and I took on the role of a project manager. The primary goal was to develop a project management tool that could serve as the foundation for project planning and execution.

### Assignment Objectives

- Gain practical experience in project management.
- Apply project management concepts and methodologies.
- Collaborate with a team of developers, designers, and testers.


## My Role as Project Manager

As the project manager, my responsibilities included:

- Defining project objectives, scope, and requirements.
- Leading the project planning phase, including task breakdown, scheduling, and resource allocation.
- Assigning roles and responsibilities to team members.
- Monitoring project progress and ensuring that tasks were completed on time.
- Facilitating communication among team members and stakeholders.
- Handling project documentation, including project plans, status reports, and meeting minutes.
- Managing risks and issues that arose during the project.



## PRINCE2 Project Management

During the course of this assignment, we applied the PRINCE2 (PRojects IN Controlled Environments) project management methodology. PRINCE2 is a structured approach to project management that emphasizes effective control, organization, and governance of projects.

### Key PRINCE2 Principles Applied

1. **Continued Business Justification:** We ensured that every project stage remained justifiable and aligned with the business goals and objectives throughout the project's lifecycle.

2. **Learn from Experience:** Regular retrospectives and reviews allowed us to learn from our experiences, both positive and negative, and make necessary improvements to our project processes.

3. **Defined Roles and Responsibilities:** Clear roles and responsibilities were established for each team member, ensuring accountability and efficient collaboration.


These PRINCE2 principles played a crucial role in maintaining control and organization throughout the project.
## Technologies Used
- Flask
- MySQL
- Mammoth
- HTML/CSS
- Python
- JavaScript

## Key Takeaways

Working as the project manager for this assignment provided me with valuable insights and skills, including:

- Effective project planning and execution.
- Team leadership and collaboration.
- Communication and stakeholder management.
- Problem-solving and risk mitigation.
- Time management and task prioritization.

This project not only served as a learning experience but also resulted in the creation of a functional project management tool that can be further developed and expanded for real-world applications.

## Database Schema

### Users Table

- **Table Name**: users
- **Description**: This table stores information about users of the application, including their usernames, passwords, and roles.

| Column Name  | Data Type    | Description             |
|--------------|--------------|-------------------------|
| idUsers      | INT          | Unique user identifier  |
| username     | VARCHAR(50)  | User's username         |
| password     | VARCHAR(255) | User's hashed password  |
| role         | VARCHAR(20)  | User's role (e.g., admin, member) |

### Projects Table

- **Table Name**: projects
- **Description**: This table contains details about the projects being managed by the application.

| Column Name  | Data Type    | Description                   |
|--------------|--------------|-------------------------------|
| idProjects   | INT          | Unique project identifier     |
| projectName  | VARCHAR(100) | Name of the project           |
| projectDesc  | TEXT         | Description of the project    |
| startDate    | DATE         | Start date of the project     |
| endDate      | DATE         | End date of the project       |

### Tasks Table

- **Table Name**: tasks
- **Description**: This table tracks individual tasks associated with projects.

| Column Name  | Data Type    | Description                      |
|--------------|--------------|----------------------------------|
| idTasks      | INT          | Unique task identifier           |
| taskName     | VARCHAR(100) | Name of the task                  |
| taskDesc     | TEXT         | Description of the task           |
| status       | VARCHAR(20)  | Task status (e.g., started, done) |
| projectID    | INT          | Foreign key to the projects table |

### UserTasks Table

- **Table Name**: usertasks
- **Description**: This table links users to the tasks they are assigned to and tracks the status of their involvement.

| Column Name  | Data Type    | Description                             |
|--------------|--------------|-----------------------------------------|
| idUserTasks  | INT          | Unique user-task relationship identifier|
| idUsers      | INT          | Foreign key to the users table          |
| idTasks      | INT          | Foreign key to the tasks table          |
| status       | VARCHAR(20)  | User's status for the assigned task     |

## Project Team and Contributions

### Development Team

- **Project Manager:** Amjad Ashour
- **Developer:** Amjad Ashour

### Role and Contributions

For this project, I served as both the project manager and the sole developer. In this dual role, my responsibilities included:

  - Writing the entire codebase for the application.
  - Designing the user interface and user experience.
  - Integrating the database and implementing data persistence.
  - Handling front-end and back-end development.
  - Conducting testing and debugging.
  - Deploying (temporarily) and maintaining the application.
In addition to my role as the project manager.

I took on this dual role to gain a comprehensive understanding of the project management and development processes, which allowed me to deliver a successful project.
