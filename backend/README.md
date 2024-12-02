# Waste Management Backend

This repository contains the backend API for a **Waste Management App**. It is built using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL** with **PostGIS** extension for handling geospatial data like addresses, collection points, and locations among other essential packages in the Pipfile 

## Table of Contents

1. [Project Overview](#project-overview)
2. [Setup Instructions](#setup-instructions)
3. [Usage](#usage)
4. [Database Setup](#database-setup)
5. [Running Tests](#running-tests)
6. [API Documentation](#api-documentation)
7. [Folder Structure](#folder-structure)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview

The **Waste Management Backend** API helps in managing waste collection schedules, user information, and geospatial data. The key features include:

- **User authentication and registration**
- **Scheduling waste collection**
- **Tracking waste collection locations using geospatial data (PostGIS)**
- **Admin dashboard for managing users and schedules**

---

## Setup Instructions

### Prerequisites

- **Python 3.10** (Ensure Python is installed on your machine)
- **PostgreSQL** (Ensure PostgreSQL is installed and running)
- **PostGIS** (PostgreSQL extension for geospatial data)
- **Pipenv** for dependency management
  - Install Pipenv if you don't have it:
    ```bash
    pip install pipenv
    ```
  - To activate the environment 
    ```bash
    pipenv shell 
    ```
  - To install the packages 
    ```bash
    pipenv install
    ```

### 1. Clone the Repository

Start by cloning the repository:

```bash
git clone https://github.com/yourusername/waste-management-backend.git
cd waste-management-backend
```

### To run the server
Run the command below to start the backend at port 8000
```bash
python manage.py runserver

```
